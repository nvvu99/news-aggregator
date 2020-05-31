# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .unit_spiders import *


process = CrawlerProcess(get_project_settings())
process.crawl(BaoTinTucSpider)
process.crawl(DoanhNghiepSpider)
process.crawl(KienThucSpider)
process.crawl(LaoDongThuDoSpider)
process.crawl(NgheNhinVietNamSpider)
process.crawl(NhanDanSpider)
process.crawl(PhapLuatXaHoiSpider)
process.crawl(PLOSpider)
process.crawl(TapChiMatTranSpider)
process.crawl(ThoiDaiSpider)
process.crawl(TienPhongSpider)
process.crawl(VanHienSpider)
process.crawl(VietNamNetSpider)
process.crawl(VietNamPlusSpider)
process.crawl(VOVSpider)

process.start()