## -*- coding: utf-8 -*-



BOT_NAME = 'now_coder'

SPIDER_MODULES = ['now_coder.spiders']
NEWSPIDER_MODULE = 'now_coder.spiders'

ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {
    'now_coder.pipelines.NowcoderPipeline': 300,
}



USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/57.0.2987.98 Chrome/57.0.2987.98 Safari/537.36'
COOKIES_ENABLED = True

SCHEDULER = "scrapy_redis.scheduler.Scheduler"               #Scheduler的替换，这是Scrapy中的调度员,Enables scheduling storing requests queue in redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"   #去重, Ensure all spiders share same duplicates filter through redis.
SCHEDULER_PERSIST = True                                     #不清理Redis队列

SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue' #爬虫调度算法（包括队列，栈，优先级队列），这里采用优先级队列



MONGODB_HOST = '120.25.78.80'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'NowcoderPromblemList'
MONGODB_DOCNAME = 'PList_dis'


REDIS_HOST = '120.25.78.80'
REDIS_PORT = 6379
