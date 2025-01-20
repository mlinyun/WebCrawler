if __name__ == "__main__":
    from scrapy.cmdline import execute

    execute("scrapy crawl news_spider -o output.json".split())