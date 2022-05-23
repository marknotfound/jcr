import logging
from time import time
import requests
from django.conf import settings
from django.core.management import BaseCommand

from discord.scrapers import scrapers
from discord.messages import MessageGenerator
from discord.models import ScrapedRace

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options) -> str:
        for scraper_name, Scraper in scrapers:
            start = time()
            logger.info("Started scraping", extra={'scraper': scraper_name})
            races = Scraper().scrape_full_dataset()

            if not bool(races):
                logger.info("Scraper returned empty dataset, skipping", extra={'scraper': scraper_name})
                continue

            if not ScrapedRace.objects.exists():
                logger.info("Database is empty. Setting initial data and skipping messaging.", extra={'scraper': scraper_name})
                for race in races.values():
                    ScrapedRace.objects.create(**race, scraper=scraper_name, raw=race)

            new_races = []
            changed_races: dict[str, dict[str, tuple]] = {}
            for title, raw_race in races.items():
                race, created = ScrapedRace.objects.get_or_create(title=title, scraper=scraper_name, defaults={
                    **raw_race,
                    "raw": raw_race,
                    "scraper": scraper_name,
                })
                logger.debug("Got race object", extra={"race": race, "raw_race": raw_race, "created?": created})

                if created:
                    logger.debug("Appended race object", extra={"race": race, "raw_race": raw_race, "created?": created})
                    new_races.append(race)

                elif race.raw != raw_race:
                    logger.debug("Raw doesnt match", extra={"race": race, "raw_race": raw_race, "created?": created})
                    changes = {}

                    for key, value in raw_race.items():
                        stored_value = race.raw[key]

                        if value != stored_value:
                            changes[key] = (stored_value, value)

                        setattr(race, key, value)

                    if changes:
                        changed_races[race.title] = changes
                        logger.debug("Set changes", extra={"changed_races": changed_races})

                    race.raw = raw_race
                    race.save()

            message_generator = getattr(MessageGenerator, f"generate_{scraper_name}_message")
            message = message_generator(new_races, changed_races)

            logger.debug(message)

            if message:
                webhook_url = getattr(settings, f"{scraper_name.upper()}_WEBHOOK")
                SUPPRESS_EMBEDS = 1 << 2
                requests.post(webhook_url, { "content": message, "flags": SUPPRESS_EMBEDS })
                logger.info("Sent message to channel", extra={'scraper': scraper_name, 'discord_message': message})

            logger.info("Completed scraping", extra={'scraper': scraper_name, 'elapsed': time() - start})
