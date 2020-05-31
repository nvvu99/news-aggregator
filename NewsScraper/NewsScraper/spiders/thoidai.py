# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class ThoiDaiSpider(BaseSpider):
    name = 'thoidai'
    allowed_domains = ['thoidai.com.vn']

    start_urls = [
        None,
        None,
        None,
        None,
        None,
        'https://thoidai.com.vn/van-hoa-du-lich/diem-den',
        None,
        None,
        None,
        None,
        'https://thoidai.com.vn/kinh-te/cong-nghe',
    ]
    
    main_xpath = '//div[@class="_MB_CATEGORY_LIST lt"]'
    articles_xpath = './/div[@class="bx-article"]'
    thumb_xpath = './a/img/@src'
    url_xpath = './a/@href'
    title_xpath = './h3/a/text()'
    sapo_xpath = './div[@class="bx-description"]/text()'
    paging_xpath = './div[@class="__MB_ARTICLE_PAGING fw lt clearfix"]'
    nextpage_xpath = './a[contains(text(), "Sau")]/@href'
    
    MAX_PAGE = 2 # 15 per page
    PUBLISHER_ID = 2