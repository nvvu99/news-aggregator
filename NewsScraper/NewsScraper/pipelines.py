# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from news.models import Feed, Article, Category, Publisher
from NewsScraper.items import FeedItem
from django.utils.text import slugify


class NewsscraperPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, FeedItem):
            feed = Feed(
                title = item['title'],
                sapo = item['sapo'],
                thumb = item['thumb'],
                original_url = item['original_url'],
                slug = slugify(item['title']),
                category = Category.objects.get(id = item['category_id']),
                publisher = Publisher.objects.get(id = item['publisher_id'])
                )
            feed.save()
        return item


class DuplicatePipeline(object):
    def process_item(self, item, spider):
        try:
            Feed.objects.get(original_url = item['original_url'])
        except Feed.DoesNotExist:
            # return item if not exist at database
            return item