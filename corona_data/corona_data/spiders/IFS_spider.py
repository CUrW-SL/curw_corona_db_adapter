import scrapy
from datetime import datetime, timedelta


class IFSSpider(scrapy.Spider):
    name = "ifs"

    def start_requests(self):
        urls = [
            'https://docs.google.com/spreadsheets/d/1zIgPU0ZlYkiKaavYAUcHKgEP95jdaMaf9ljJgRqtog4/htmlview#'
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        page = (datetime.now()).strftime("%Y-%m-%d_%H-%M-%S")
        filename = 'ifs-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)