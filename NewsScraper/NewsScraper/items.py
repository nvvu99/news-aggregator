# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from news.models import Feed
import re


def full_vov_url(short_url):
    return 'https://vov.vn' + short_url

def full_btt_url(short_url):
    return 'https://baotintuc.vn' + short_url

def full_tcmt_url(short_url):
    return 'https://tapchimattran.vn' + short_url

def full_vh_url(short_url):
    return 'http://vanhien.vn' + short_url

def full_nd_url(short_url):
    return 'https://nhandan.com.vn' + short_url


class FeedItem(scrapy.Item):
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


class BTTFeedItem(FeedItem):
    original_url = scrapy.Field(
        input_processor = MapCompose(full_btt_url)
        )


class VOVFeedItem(FeedItem):
    original_url = scrapy.Field(
        input_processor = MapCompose(full_vov_url),
        )


class TCMTFeedItem(FeedItem):
    original_url = scrapy.Field(
        input_processor = MapCompose(full_tcmt_url),
        )


class VHFeedItem(FeedItem):
    thumb = scrapy.Field(
        input_processor = MapCompose(full_vh_url),
        )
    original_url = scrapy.Field(
        input_processor = MapCompose(full_vh_url),
        )


class NDFeedItem(FeedItem):
    thumb = scrapy.Field(
        input_processor = MapCompose(full_vh_url),
        )
    original_url = scrapy.Field(
        input_processor = MapCompose(full_vh_url),
        )

    
class ArticleItem(scrapy.Item):
    body = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    original_url = scrapy.Field(
        input_processor = MapCompose(str.strip),
        )
    published_date = scrapy.Field()

