# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/1215/']

    rules = (
        # 可以写多个规则
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[10]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths =r'//div[@class="bottem2"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ','\n')

        yield {
            'title':title,
            'content':content
        }


        return item
