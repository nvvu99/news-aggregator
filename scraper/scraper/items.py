# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    sapo = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    thumb = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    original_url = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    category_id = scrapy.Field()
    publisher_id = scrapy.Field()

