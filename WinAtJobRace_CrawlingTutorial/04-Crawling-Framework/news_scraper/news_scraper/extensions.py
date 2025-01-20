from scrapy import signals


class SimpleExtension:
    @classmethod
    def from_crawler(cls, crawler):
        # 连接到 crawler 的信号
        ext = cls()
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_opened(self, spider):
        print(f"Spider {spider.name} opened 开始爬取")

    def spider_closed(self, spider):
        print(f"Spider {spider.name} closed 爬取结束")
