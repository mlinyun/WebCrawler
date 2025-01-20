from ..items import NewsScraperItem
import scrapy


class NewsSpiderSpider(scrapy.Spider):
    # 爬虫名字，不可以重复
    name = "news_spider"
    # 初始化 URL 列表，如果没有 start_requests 函数会先抓取这个列表的 URL
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        # 选择新闻标题的 XPATH 或 CSS 选择器，extract_first 提取符合条件的第一个元素
        title = response.css("h1").extract_first()
        content = response.css("P").extract_first()
        item = NewsScraperItem(title=title, content=content)
        yield item
