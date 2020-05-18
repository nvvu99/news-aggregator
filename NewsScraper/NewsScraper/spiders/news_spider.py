# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .baotintuc import BaoTinTucSpider
from .doanhnghiepvn import DoanhNghiepSpider
from .kienthuc import KienThucSpider
from .laodongthudo import LaoDongThuDoSpider
from .nghenhinvietnam import NgheNhinVietNamSpider
from .nhandan import NhanDanSpider
from .phapluatxahoi import PhapLuatXaHoiSpider
from .plo import PLOSpider
from .tapchimattran import TapChiMatTranSpider
from .thoidai import ThoiDaiSpider
from .tienphong import TienPhongSpider
from .vanhien import VanHienSpider
from .vietnamnet import VietNamNetSpider
from .vietnamplus import VietNamPlusSpider
from .vov import VOVSpider


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