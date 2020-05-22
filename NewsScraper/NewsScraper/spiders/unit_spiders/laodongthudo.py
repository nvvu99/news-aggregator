# -*- coding: utf-8 -*-
from .base_spider import BaseSpider


class LaoDongThuDoSpider(BaseSpider):
    name = 'laodongthudo'
    allowed_domains = ['laodongthudo.vn']
    start_urls = [
        None,
        None,
        'http://laodongthudo.vn/quoc-te',
        None,
        'http://laodongthudo.vn/van-hoa/am-nhac',
        None,
        'http://laodongthudo.vn/lao-dong/viec-lam',
        'http://laodongthudo.vn/giao-duc',
        'http://laodongthudo.vn/van-hoa/dien-anh',
        'http://laodongthudo.vn/phap-luat',
        None,
    ]
    
    main_xpath = '//div[@class="col_category clearfix"]'
    articles_xpath = './div[@class="list_news clearfix"]'
    thumb_xpath = './div[@class="list_news_img clearfix"]/a/img/@src'
    url_xpath = './div[@class="list_news_img clearfix"]/a/@href'
    title_xpath = './div[@class="list_news_title clearfix"]/h2/a/text()'
    sapo_xpath = './div[@class="list_news_title clearfix"]/p/text()'
    paging_xpath = './div[@class="__MB_ARTICLE_PAGING paging"]'
    nextpage_xpath = './a[last()]/@href'

    MAX_PAGE = 2 # 16 per page
    PUBLISHER_ID = 10