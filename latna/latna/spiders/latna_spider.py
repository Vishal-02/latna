from pathlib import Path
from urllib.parse import urljoin
from ..items import LatnaItem

import scrapy

class LatnaSpider(scrapy.Spider):
    name = "latna"

    async def start(self):
        urls = [
            # You have to add the chapter and page number at the end like 266/14.jpg
            "https://cdn2.ravenscans.com/survival-story-of-a-sword-king-in-a-fantasy-world/"
        ]

        for url in urls:
            #TODO: chapter number just for testing, gonna have to change this later using
            # some sort of persistent variable. Making a db for this seems to be a waste.
            yield scrapy.Request(url=urljoin(url, "chapter-266/14.jpg"), callback=self.parse)

    def parse(self, response):
        print(f"\n\n {response.status} \n\n")
        yield LatnaItem(image_urls=[response.url])