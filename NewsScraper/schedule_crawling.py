import subprocess
import time


while True:
    subprocess.call(['scrapy', 'crawl'])
    time.sleep(60 * 10) # 10 minutes
