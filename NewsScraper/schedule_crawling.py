from scrapyd_api import ScrapydAPI
from scrapy.utils.project import get_project_settings
import schedule
import time


target = 'http://localhost:6800'
scrapyd = ScrapydAPI(target)
project = 'NewsScraper'
spiders = scrapyd.list_spiders(project)
settings = get_project_settings()

while True:
    for spider in spiders:
        scrapyd.schedule(project, spider, settings=settings)
    time.sleep(60 * 10) # 10 minutes
