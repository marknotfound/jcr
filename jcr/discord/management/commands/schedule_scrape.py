from time import sleep
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                call_command("scrape_races")
            except Exception as e:
                print(e)

            sleep(60 * 60) # 1 hour