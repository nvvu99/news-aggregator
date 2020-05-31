# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from NewsScraper.items import ArticleItem


class BaseSpider(scrapy.Spider):
    start_urls = []

    main_xpath = ''
    articles_xpath = ''
    thumb_xpath = ''
    url_xpath = ''
    title_xpath = ''
    sapo_xpath = ''
    paging_xpath = ''
    nextpage_xpath = ''
    MAX_PAGE = 2
    PUBLISHER_ID = 0

    def start_requests(self):
        for i, url in enumerate(self.start_urls, start=1):
            if url is not None:
                yield scrapy.Request(
                    url = url,
                    callback = self.parse_category_page,
                    meta = {
                        'category_id': i,
                        'current_page': 1,
                    }
                )

    def parse_category_page(self, response):
        main = response.xpath(self.main_xpath)
        articles = main.xpath(self.articles_xpath)
        meta = response.meta
        for article in articles:
            thumb = response.urljoin(article.xpath(self.thumb_xpath).extract_first())
            url = response.urljoin(article.xpath(self.url_xpath).extract_first())
            
            feed_loader = ItemLoader(item=ArticleItem(), selector=article)
            feed_loader.default_output_processor = TakeFirst()
            feed_loader.add_value('thumb', thumb)
            feed_loader.add_xpath('title', self.title_xpath)
            feed_loader.add_xpath('sapo', self.sapo_xpath)
            feed_loader.add_value('original_url', url)
            feed_loader.add_value('category_id', meta['category_id'])
            feed_loader.add_value('publisher_id', self.PUBLISHER_ID)
            yield feed_loader.load_item()

        # To next page
        paging = main.xpath(self.paging_xpath)
        current_page = meta['current_page']

        if (current_page < self.MAX_PAGE):
            next_page = paging.xpath(self.nextpage_xpath).extract_first()
            meta['current_page'] += 1
            yield scrapy.Request(
                url = response.urljoin(next_page),
                callback = self.parse_category_page,
                meta = meta,
            )