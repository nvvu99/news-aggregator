# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class TapChiMatTranSpider(BaseSpider):
    name = 'tapchimattran'
    allowed_domains = ['tapchimattran.vn']
    start_urls = [
        'http://tapchimattran.vn/thoi-su/',
        None,
        'http://tapchimattran.vn/the-gioi/',
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
    main_xpath = '//div[@class="l-container__main"]'
    articles_xpath = './div[has-class("list-region")]/article'
    thumb_xpath = './a/figure/img/@src'
    url_xpath = './a/@href'
    title_xpath = './a/h2/text()'
    sapo_xpath = './p[@class="story__summary"]/text()'
    paging_xpath = './div[@class="pagination"]'
    nextpage_xpath = './div[@class="pagination__pages"]/span/a[@class="next"]/@href'
    
    MAX_PAGE = 3 # 10 per page
    PUBLISHER_ID = 4