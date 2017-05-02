# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from now_coder.items import NowcoderItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class NowcoderspiderSpider(RedisSpider):
    name = "nowcoderspider"
    redis_key = 'nowcoderspider'   #redis_key实际上就是一个变量名，之后爬虫爬到的所有URL都会保存到Redis中这个名为“spider:start_urls”的列表下面，爬虫同时也会从这个列表中读取后续页面的URL
    #start_urls = ['https://www.nowcoder.com/activity/oj/']
    url = 'http://www.nowcoder.com'    #self.url

    def parse(self, response):

        problemlistgroup = response.xpath('//table/tbody')#.extract()

        for problemlist in problemlistgroup:
            problems_urls = problemlist.xpath('tr/td[@class="offer-pot txt-left"]/a/@href').extract()
            for each in problems_urls:
                yield Request(self.url + each, callback = self.parse_content)

            next_page = response.xpath('//li[@class="txt-pager js-next-pager"]/a/@href').extract()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page[0]), callback=self.parse)

    def parse_content(self, response):
        item = NowcoderItem()
        sub = response.xpath('//div[@class="subject-describe"]')
        sub_1 = sub.xpath('string(.)').extract()
        item['SubDescribe'] = sub_1
        yield item  #将item交给pipelines处理


