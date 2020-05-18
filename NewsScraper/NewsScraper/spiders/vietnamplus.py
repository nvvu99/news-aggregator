# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class VietNamPlusSpider(BaseSpider):
    name = 'vietnamplus'
    allowed_domains = ['vietnamplus.vn']

    start_urls = [
        None,
        None,
        None,
        None,
        'https://www.vietnamplus.vn/vanhoa/amnhac.vnp',
        None,
        None,
        None,
        'https://www.vietnamplus.vn/vanhoa/dienanh.vnp',
        None,
        None,
    ]
    
    main_xpath = '//section[@class="zone--timeline"]'
    articles_xpath = './div/article[@class="story"]'
    thumb_xpath = './a[@class="story__thumb"]/img/@src'
    url_xpath = './a[@class="story__thumb"]/@href'
    title_xpath = './h2/a/text()'
    sapo_xpath = './div[@class="summary"]/text()'
    paging_xpath = './nav/span/ul'
    nextpage_xpath = './li[@class="active"]/following-sibling::li[1]/a/@href'

    MAX_PAGE = 2 # 14 per page
    PUBLISHER_ID = 14