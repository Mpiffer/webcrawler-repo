```python
import scrapy
import json

class RedditScraper(scrapy.Spider):
    name = "reddit_scraper"
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        for post in response.css('div.thing'):
            yield {
                'title': post.css('p.title a::text').get(),
                'url': post.css('p.title a::attr(href)').get(),
                'upvotes': post.css('div.score.unvoted::attr(title)').get(),
            }

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def close(self, reason):
        with open('data.json', 'w') as f:
            json.dump(self.crawled_data, f)

    def __init__(self):
        self.crawled_data = []
```
