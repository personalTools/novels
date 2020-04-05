# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.co']
    start_urls = ['https://www.81zw.co/book_3465/2979604.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            'title':title,
            'content':content
        }

        next_url = response.xpath('//div[@class="papgbutton"]/a[3]/@href').extract_first()
        # base_url = '{}'.format(next_url)
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
