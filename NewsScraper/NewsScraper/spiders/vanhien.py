# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class VanHienSpider(BaseSpider):
    name = 'vanhien'
    allowed_domains = ['vanhien.vn']
    start_urls = [
        None,
        None,
        None,
        'http://vanhien.vn/news/Nghe-thuat',
        None,
        'http://vanhien.vn/news/du-lich',
        None,
        'http://vanhien.vn/news/giao-duc',
        None,
        None,
        None,
    ]
    main_xpath = '//div[@class="mid"]/div[@class="wrapper"]/div[@class="main pl-10 pr-10"]/div[@class="row"]/div[@class="col-10 mr-20 pt-10"]/div[@class="row" and not(@style)]'
    articles_xpath = './div[@class="list-view"]/div'
    thumb_xpath = './div[@class="col-3 mr-20"]/a/img/@lazy-src'
    url_xpath = './div[@class="col-3 mr-20"]/a/@href'
    title_xpath = './div[@class="col-7"]/h3/a/text()'
    sapo_xpath = './div[@class="col-7"]/p/text()'
    paging_xpath = './div[has-class("pagination")]/ul'
    nextpage_xpath = './li[@class="next"]/a/@href'
    
    MAX_PAGE = 2 # 15 per page
    PUBLISHER_ID = 7