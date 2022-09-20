import requests
from .abc import BaseScraper

NYRR_HOST = "https://www.nyrr.org"
STATUS_EXCLUDE_LIST = ("Completed", "Partner Race",)

class NYRRScraper(BaseScraper):
    root_url = NYRR_HOST
    paths = (
        "/fullraceyearindex?year=2022",
        "/fullraceyearindex?year=2023",
    )

    def scrape_full_dataset(self) -> dict:
        races = {}

        for path in self.paths:
            race_chunk = self.scrape_path(path)
            races = races | race_chunk

        return races

    def scrape_path(self, path) -> dict:
        root, _ = self.fetch_root(path)
        races = {}

        for row in self.find_all_by_class(root, "index_listing__inner"):
            status = self.find_text_by_class(row, "home_race_calendar_item__status")
            if status in STATUS_EXCLUDE_LIST:
                continue

            title_node = self.find_by_class(row, "index_listing__title")
            anchor_node = title_node.find("a")
            url = NYRR_HOST + anchor_node.attrs["href"] if anchor_node else ""
            title = title_node.text.strip()

            races[title] = {
                "title": title,
                "url": url,
                "start_date": self.find_text_by_class(row, "index_listing__date"),
                "start_time": self.find_text_by_class(row, "index_listing__time"),
                "location": self.find_text_by_class(row, "index_listing__location"),
                "status": status,
            }

        return races

class NYRRNinePlusOneVolunteerScraper(BaseScraper):
    root_url = NYRR_HOST
    paths = (
        "/getinvolved/volunteer/opportunities?available_only=true&itemId=3EB6F0CC-0D76-4BAF-A894-E2AB244CEB44&limit=8&offset=0&opportunity_type=9%2B1%20Qualifier&totalItemLoaded=8",
    )

    def scrape_full_dataset(self) -> dict:
        opportunities = []
        _, response = self.fetch_root()
        cookies = response.cookies

        for path in self.paths:
            root, _ = self.fetch_root(path, cookies=cookies)

            for node in self.find_all_by_class(root, "role_listing"):
                opportunities.append({
                    "title": self.find_text_by_class(node, "role_listing__title"),
                    "event": self.find_text_by_class(node, "role_listing__event"),
                    "date": self.find_text_by_class(node, "role_listing__date"),
                    "time": self.find_text_by_class(node, "role_listing__time"),
                    "location": self.find_text_by_class(node, "role_listing__location"),
                })
        import json
        print(json.dumps(opportunities, indent=2))
