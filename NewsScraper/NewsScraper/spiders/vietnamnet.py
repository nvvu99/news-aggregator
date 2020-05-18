# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class VietNamNetSpider(BaseSpider):
    name = 'vietnamnet'
    allowed_domains = ['vietnamnet.vn']
    start_urls = [
        'https://vietnamnet.vn/vn/thoi-su/',
        'https://vietnamnet.vn/vn/the-thao/',
        'https://vietnamnet.vn/vn/the-gioi/',
        'https://vietnamnet.vn/vn/giai-tri/di-san-my-thuat-san-khau/',
        'https://vietnamnet.vn/vn/giai-tri/nhac/',
        'https://vietnamnet.vn/vn/doi-song/du-lich/',
        None,
        'https://vietnamnet.vn/vn/giao-duc/',
        'https://vietnamnet.vn/vn/giai-tri/phim/',
        'https://vietnamnet.vn/vn/phap-luat/',
        'https://vietnamnet.vn/vn/cong-nghe/',
    ]
    main_xpath = '//div[has-class("list-content")]'
    articles_xpath = './div[@class="clearfix item"]'
    thumb_xpath = './a/img/@lazy-src'
    url_xpath = './a/@href'
    title_xpath = './div/h3/a/text()'
    sapo_xpath = './div/div[@class="lead"]/text()'
    paging_xpath = '/html/head'
    nextpage_xpath = './link[@rel="next"]/@href'
    
    MAX_PAGE = 2 # 15 per page
    PUBLISHER_ID = 11