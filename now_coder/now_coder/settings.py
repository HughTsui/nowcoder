## -*- coding: utf-8 -*-



BOT_NAME = 'now_coder'

SPIDER_MODULES = ['now_coder.spiders']
NEWSPIDER_MODULE = 'now_coder.spiders'

ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {
    'now_coder.pipelines.NowcoderPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
	'now_coder.middlewares.UAMiddleware':543
}

USER_AGENT_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/57.0.2987.98 Chrome/57.0.2987.98 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
                   'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11']

COOKIES_ENABLED = True

SCHEDULER = "scrapy_redis.scheduler.Scheduler"               #Scheduler的替换，这是Scrapy中的调度员,Enables scheduling storing requests queue in redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"   #去重, Ensure all spiders share same duplicates filter through redis.
SCHEDULER_PERSIST = True                                     #不清理Redis队列

SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue' #爬虫调度算法（包括队列，栈，优先级队列），这里采用优先级队列



MONGODB_HOST = '112.74.203.169'#'127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'NowcoderPromblemList'
MONGODB_DOCNAME = 'PList_dis'


REDIS_HOST = '120.25.78.80'#'127.0.0.1'
REDIS_PORT = 6379
