# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class LatnaPipeline(ImagesPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("\n\n PIPELINE INITIALIZED \n\n")

    def get_media_requests(self, item, info):
        print("\n\n\n MEDIA REQUEST!! \n\n\n")
        adapter = ItemAdapter(item)
        for url in adapter['image_urls']:
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]

        if not image_path:
            raise DropItem("You fucked up with the img download somehow")

        adapter = ItemAdapter(item)
        adapter['image_path'] = image_path
        print("\n\n\n DOWNLOAD PIPELINE REACHED \n\n\n")
        return item
