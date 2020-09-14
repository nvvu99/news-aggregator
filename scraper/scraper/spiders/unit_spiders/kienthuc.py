# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class KienThucSpider(BaseSpider):
    name = 'kienthuc'
    allowed_domains = ['kienthuc.net.vn']

    start_urls = [
        None,
        'https://kienthuc.net.vn/the-thao/',
        'https://kienthuc.net.vn/the-gioi/',
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        'https://kienthuc.net.vn/khoa-hoc-cong-nghe/',
    ]
    
    main_xpath = '//div[@class="sticky-wrap"]/div[@class="container"]'
    articles_xpath = './div[@class="listNsub clearfix"]/section/article'
    thumb_xpath = './p[@class="thumbnail"]/a/img/@src'
    url_xpath = './h2/a/@href'
    title_xpath = './h2/a/text()'
    sapo_xpath = './div/text()'
    paging_xpath = './div[@class="vov-pager"]/ul/span/ul'
    nextpage_xpath = './li[last()]/a/@href'

    MAX_PAGE = 2 # 20 per page
    PUBLISHER_ID = 13