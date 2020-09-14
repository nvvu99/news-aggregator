# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from news.models import Article, Category, Publisher
from .items import ArticleItem
from django.utils.text import slugify


class NewsScraperPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ArticleItem):
            article = Article.objects.update_or_create(
                title = item['title'],
                sapo = item['sapo'],
                thumb = item['thumb'],
                original_url = item['original_url'],
                slug = slugify(item['title']),
                category = Category.objects.get(id = item['category_id']),
                publisher = Publisher.objects.get(id = item['publisher_id'])
            )
        return item


