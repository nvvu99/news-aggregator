# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class BaoTinTucSpider(BaseSpider):
    name = 'baotintuc'
    allowed_domains = ['baotintuc.vn']

    start_urls = [
        'https://baotintuc.vn/thoi-su-472ct0.htm',
        'https://baotintuc.vn/the-thao-273ct0.htm',
        'https://baotintuc.vn/the-gioi-130ct0.htm',
        None,
        None,
        'https://baotintuc.vn/du-lich-132ct158.htm',
        'https://baotintuc.vn/viec-lam-498ct129.htm',
        'https://baotintuc.vn/giao-duc-135ct0.htm',
        None,
        'https://baotintuc.vn/phap-luat-475ct0.htm',
        'https://baotintuc.vn/khoa-hoc-cong-nghe-131ct0.htm',
    ]
    
    main_xpath = '//div[@class="listspecial"]'
    articles_xpath = './ul/li'
    thumb_xpath = './a/img/@src'
    url_xpath = './a/@href'
    title_xpath = './h3/a/text()'
    sapo_xpath = './p/text()'
    paging_xpath = './div[@class="paging"]/div[@class="pager"]'
    nextpage_xpath = './a[text()="Tiếp"]/@href'

    MAX_PAGE = 2 # 20 per page
    PUBLISHER_ID = 1