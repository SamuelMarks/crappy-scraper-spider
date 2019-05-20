from __future__ import print_function

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4).pprint

import scrapy
from scrapy_splash import SplashRequest

from bs4 import BeautifulSoup


# sys.stderr = os.devnull

class SlatteryItSpider(scrapy.Spider):
    name = 'slatteryit_spider'
    start_urls = 'http://www.slatteryit.com.au/the-watch-archive/',

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print("response.body.find('campaign'):", response.body.find('campaign'))
        soup = BeautifulSoup(response.body, 'html.parser')
        print(soup.prettify(encoding='utf8'))
        # print(dir(response))
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # ...


if __name__ == '__main__':
    pass
