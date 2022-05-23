import requests
from abc import abstractmethod
from bs4 import BeautifulSoup
from . import exceptions

class BaseScraper:
    root_url = None

    def fetch_root(self) -> BeautifulSoup:
        response = requests.get(self.root_url)

        if not response.ok:
            raise exceptions.FailedScraperException(f"Request to root URL failed: {self.root_url=} {response.status_code=}")

        return BeautifulSoup(response.content, features="html.parser")

    def find_all_by_class(self, parent_node, class_name):
        return parent_node.find_all(attrs={"class": class_name})

    def find_by_class(self, parent_node, class_name):
        return parent_node.find(attrs={"class": class_name})

    def find_text_by_class(self, parent_node, class_name):
        node = self.find_by_class(parent_node, class_name)

        if node:
            return node.text.strip()

        return ""

    @abstractmethod
    def scrape_full_dataset(self) -> dict:
        """
        Returns a dict containing the full dataset for the scraped property.
        This data should match the format in the JSON key/value store for
        the concrete scraper implementation.
        """
        pass