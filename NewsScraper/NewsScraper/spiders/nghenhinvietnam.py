# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class NgheNhinVietNamSpider(BaseSpider):
    name = 'nghenhinvietnam'
    allowed_domains = ['nghenhinvietnam.vn']
    start_urls = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        'https://nghenhinvietnam.vn/khoa-hoc/',
    ]
    main_xpath = '//main/div[@class="main-content"]'
    articles_xpath = './ul/li/article'
    thumb_xpath = './figure/a/img/@src'
    url_xpath = './h2/a/@href'
    title_xpath = './h2/a/text()'
    sapo_xpath = './div[@class="summary"]/text()'
    paging_xpath = './div[has-class("pagination")]/span/ul'
    nextpage_xpath = './li[last()]/a/@href'
    
    MAX_PAGE = 3 # 12 per page
    PUBLISHER_ID = 10