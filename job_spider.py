import scrapy


class JobSpiderSpider(scrapy.Spider):
    name = "job_spider"
    allowed_domains = ["indeed.com"]
    start_urls = ["https://indeed.com"]

    def parse(self, response):
        pass
