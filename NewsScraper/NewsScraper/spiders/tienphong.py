# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class TienPhongSpider(BaseSpider):
    name = 'tienphong'
    allowed_domains = ['tienphong.vn']

    start_urls = [
        None,
        'https://www.tienphong.vn/the-thao/',
        'https://www.tienphong.vn/the-gioi/',
        None,
        None,
        None,
        None,
        'https://www.tienphong.vn/giao-duc/',
        None,
        'https://www.tienphong.vn/phap-luat/',
        'https://www.tienphong.vn/cong-nghe/',
    ]
    
    main_xpath = '//div[@class="region cate-list-news"]'
    articles_xpath = './div[@class="collection other-news"]/article'
    thumb_xpath = './a/figure/img/@src'
    url_xpath = './a/@href'
    title_xpath = './a/h2/text()'
    sapo_xpath = './a/p/text()'
    paging_xpath = './nav[@class="pagination-wrap"]/div/span/ul'
    nextpage_xpath = './li/a[@id="ctl00_mainContent_ContentList1_pager_nextControl"]/@href'
    
    MAX_PAGE = 1 # 30 per page
    PUBLISHER_ID = 6