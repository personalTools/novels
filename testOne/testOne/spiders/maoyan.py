# -*- coding: utf-8 -*-
import scrapy
from testOne.items import MoveItem



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/cinemas?offset=0']

    def parse(self, response):
        names = response.xpath('//div[@class="cinema-info"]/a/text()').extract()
        addresses = response.xpath('//div[@class="cinema-info"]/p/text()').extract()

        item = MoveItem()
        for name,address in zip(names,addresses):
            item['name'] = name
            item['address'] = address
            yield item

        # for name,address in zip(names,addresses):
            # print(name,":",address)
            # yield {"name":name,"address":address}
