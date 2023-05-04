from random import randint
from .models import ScrapedRace, VolunteerOpportunity

def random_emoji():
    emoji = [
        ":person_running:",
        ":athletic_shoe:",
        ":running_shirt_with_sash:",
        ":dash:",
        ":woman_running:",
        ":man_running:",
        ":rainbow:",
        ":palm_tree:",
        ":sunflower:",
        ":sunny: ",
    ]

    return emoji[randint(0, len(emoji)-1)]

class MessageGenerator:
    human_keys = {
        "url": "Registration Link",
    }

    """
    Each method on this class named with the convention of `generate_{name}_message`
    will be called for its corresponding scraper to generate a message to send
    to the Discord webhook. These methods receive the following arguments:

    new_records <list[dict]>
        A list of records added to the JSON database
        since the last time the file was generated.

    updates <dict[str, dict[str, tuple]]>
        This is data that has changed in existing records
        since the last time the file was generated.

        For example, using NYRR race schedule data:
        {
            "NYRR Al Gordon 4M": {
                "title": ("Old Title", "New Title"),
                "url": ("https://oldurl", "https://newurl"),
            }
        }
    """
    @classmethod
    def generate_nyrr_message(cls, new_records: list[ScrapedRace], updates: dict[str, dict[str, tuple]]) -> str:
        if not new_records and not updates:
            return ""

        message = ":rotating_light: NYRR schedule updated :rotating_light:\n\n"
        if new_records:
            race_or_races = "Races" if len(new_records) > 1 else "Race"
            message += f"**New {race_or_races} Added**\n\n"

            for race in new_records:
                emoji = random_emoji()
                message += f"{emoji} **{race.title}** ({race.status})\n{race.start_date} @ {race.start_time} - {race.location}"

                if race.url:
                    message += f"\nSign up: {race.url}"
                else:
                    message += "\nRegistration link not yet available."

                message += "\n\n"

        if updates:
            race_or_races = "Races" if len(updates.keys()) > 1 else "Race"
            message += f"**Updated {race_or_races}**\n\n"
            for race_name, changeset in updates.items():
                emoji = random_emoji()
                message += f"{emoji} **{race_name}**\n"
                for key, (previous_value, current_value) in changeset.items():
                    human_key = cls.humanize_key(key)

                    if previous_value and not current_value:
                        message += f"{human_key} was removed. Was previously {previous_value}."
                    elif not previous_value  and current_value:
                        message += f"{human_key} was added: {current_value}"
                    else:
                        message += f"{human_key} changed from ~~{previous_value}~~ to {current_value}"

                    message += "\n"

                message += "\n\n"

        return message

    @classmethod
    def generate_volunteer_opportunities_message(cls, opportunities: list[VolunteerOpportunity]) -> str:
        if not opportunities:
            return ""

        message = ":rotating_light: New 9+1 Volunteer Opportunities :rotating_light:\n\n"

        for opportunity in opportunities:
            emoji = random_emoji()
            message += f"{emoji} **{opportunity.event} - {opportunity.title}**\n{opportunity.start_date} @ {opportunity.start_time} - {opportunity.location}\n{opportunity.description}\n\n"

        signup_url = "https://www.nyrr.org/getinvolved/volunteer/opportunities?available_only=true&limit=8&offset=0&opportunity_type=9%2B1%20Qualifier&totalItemLoaded=8"
        message += f"View Opportunities: {signup_url}"
        return message

    @classmethod
    def humanize_key(cls, key):
        def default_transform(key):
            return key.replace("_", " ").title()

        return cls.human_keys.get(key, default_transform(key))