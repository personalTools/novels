# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TestonePipeline(object):

    def open_spider(self,spider):
        # self.filename = open('movie.txt','w',encoding='utf-8')
        self.filename = open('wddfss1.txt', 'w', encoding='utf-8')



    def process_item(self, item, spider):
        # movie
        # self.filename.write(item['name'] + ": " + item['address'] + '\n')
        # self.filename.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        # with open('movie.txt','a',encoding='utf-8') as f:
            # f.write(json.dumps(item, ensure_ascii=False) + '\n')
            # f.write(item['name'] + ":" + item['address'] + '\n')

        # xiaoshuo
        title = item['title']
        content = item['content']
        info = title + '\n' + content + '\n'
        self.filename.write(info)
        self.filename.flush() #手动刷新文件流，避免文件流过小而没有写进来。一百一写，才五十。
        return item

    def close_spider(self,spider):
        self.filename.close()
