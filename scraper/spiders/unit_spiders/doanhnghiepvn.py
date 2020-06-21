# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class DoanhNghiepSpider(BaseSpider):
    name = 'doanhnghiepvn'
    allowed_domains = ['doanhnghiepvn.vn']
    start_urls = [
        None,
        'https://doanhnghiepvn.vn/966/the-thao',
        'https://doanhnghiepvn.vn/967/quoc-te',
        'https://doanhnghiepvn.vn/1019/nghe-thuat',
        None,
        'https://doanhnghiepvn.vn/997/du-lich',
        None,
        'https://doanhnghiepvn.vn/1028/giao-duc',
        None,
        None,
        'https://doanhnghiepvn.vn/987/cong-nghe',
    ]
    main_xpath = '//div[@class="main-content-inner clearfix"]'
    articles_xpath = './div[@class="main-content-inner row"]/article'
    thumb_xpath = './/div[@class="featured-image"]/a/img/@lazy-src'
    url_xpath = './/div[@class="featured-image"]/a/@href'
    title_xpath = './/h4[@class="entry-post-title"]/a/text()'
    sapo_xpath = './/div[@class="entry-content blog-entry-summary"]/text()'
    paging_xpath = './div[@class="post-pagination"]/ul'
    nextpage_xpath = './li[last()]/a/@href'
    
    MAX_PAGE = 2 # 15 per page
    PUBLISHER_ID = 12