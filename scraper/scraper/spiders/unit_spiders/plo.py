# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class PLOSpider(BaseSpider):
    name = 'plo'
    allowed_domains = ['plo.vn']

    start_urls = [
        'https://plo.vn/thoi-su/',
        'https://plo.vn/the-thao/',
        'https://plo.vn/quoc-te/',
        None,
        None,
        'https://plo.vn/kinh-te/du-lich/',
        None,
        'https://plo.vn/xa-hoi/giao-duc/',
        None,
        'https://plo.vn/phap-luat/',
        None,
    ]
    
    main_xpath = '//div[@class="cate-listing"]'
    articles_xpath = './div[@class="story clearfix"]'
    thumb_xpath = './p[@class="thumb"]/a/img/@src'
    url_xpath = './p[@class="thumb"]/a/@href'
    title_xpath = './p[@class="title"]/a/text()'
    sapo_xpath = './p[@class="summary"]/text()'
    paging_xpath = './div[@class="pagination"]/span/ul'
    nextpage_xpath = './li[last()]/a/@href'

    MAX_PAGE = 1 # 25 per page
    PUBLISHER_ID = 15