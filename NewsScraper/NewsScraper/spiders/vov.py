# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class VOVSpider(BaseSpider):
    name = 'vov'
    allowed_domains = ['vov.vn']

    start_urls = [
        None,
        'https://vov.vn/the-thao/',
        'https://vov.vn/the-gioi/',
        None,
        'https://vov.vn/van-hoa/am-nhac/',
        'https://vov.vn/du-lich/',
        'https://vov.vn/viec-lam/',
        'https://vov.vn/xa-hoi/giao-duc/',
        'https://vov.vn/van-hoa/dien-anh/',
        'https://vov.vn/phap-luat/',
        None,
    ]
    
    main_xpath = '//div[@class="col-main"]'
    articles_xpath = './/div[@class="stories-style-6"]/article'
    thumb_xpath = './figure/a/img/@src'
    url_xpath = './figure/a/@href'
    title_xpath = './div/a/text()'
    sapo_xpath = './p/text()'
    paging_xpath = './div[@class="pagination"]/span/ul'
    nextpage_xpath = './li/a[@class="next"]/@href'

    MAX_PAGE = 1 # 30 per page
    PUBLISHER_ID = 5