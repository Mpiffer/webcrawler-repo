```python
import scrapy
from scrapy.crawler import CrawlerProcess
from reddit_scraper import RedditSpider

class Main:
    def __init__(self):
        self.process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

    def run_spiders(self):
        self.process.crawl(RedditSpider)
        self.process.start()

if __name__ == "__main__":
    main = Main()
    main.run_spiders()
```