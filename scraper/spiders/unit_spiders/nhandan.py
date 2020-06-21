# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class NhanDanSpider(BaseSpider):
    name = 'nhandan'
    start_urls = [
        None,
        'https://nhandan.com.vn/thegioi',
        'https://nhandan.com.vn/thethao',
        'https://nhandan.com.vn/vanhoa',
        None,
        'https://nhandan.com.vn/du-lich',
        None,
        'https://nhandan.com.vn/giaoduc',
        None,
        'https://nhandan.com.vn/phapluat',
        'https://nhandan.com.vn/khoahoc-congnghe',
    ]
    main_xpath = '//div[@class="container plr-0 content-container"]/div[@class="row pt-20"]/div[2]/div[1]'
    articles_xpath = './div[@class="hotnew-container lop3"]/div'
    thumb_xpath = './div/a/img/@src'
    url_xpath = './div/a/@href'
    title_xpath = './h5/a/text()'
    sapo_xpath = './div/p/text()'
    paging_xpath = './div[@class="col-md-12"][1]//ul'
    nextpage_xpath = './li[last()]/a/@href'
    
    MAX_PAGE = 3 # 10 per page
    PUBLISHER_ID = 8