from .abc import BaseScraper

NYRR_HOST = "https://www.nyrr.org"
STATUS_EXCLUDE_LIST = ("Completed", "Partner Race",)

class NYRRScraper(BaseScraper):
    root_url = f"{NYRR_HOST}/fullraceyearindex?year=2022"

    def scrape_full_dataset(self) -> dict:
        root = self.fetch_root()
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