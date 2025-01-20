import json
from pipes import quote

import scrapy
import execjs


class HeimaoSpider(scrapy.Spider):
    name = "heimao"
    allowed_domains = ["sina.cn"]
    start_urls = ["https://sina.cn"]

    def __init__(self):
        node = execjs.get()

        with open("../decrypt_script/heimao_signature.js", encoding="utf-8") as f:
            js_code = f.read()

        self.ctx = node.compile(js_code)

    def start_requests(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "Host": "tousu.sina.cn"
        }
        kws = ["抖音"]
        page = 1
        for kw in kws:
            ts, rs, signature = self.ctx.call("get_search_url", kw, page).split(";")
            url = f'https://tousu.sina.cn/apps/api/complaint/search_v1?keyword={quote(kw)}&page={page}' \
                  f'&page_size=10&version=2.9.4&ts={ts}&rs={rs}&signature={signature}'
            yield scrapy.Request(url=url, meta={"kw": kw, "page": page}, headers=headers)

    def parse(self, response):
        kw = response.meta["kw"]
        page = response.meta["page"]
        data = json.loads(response.text)
        info_list = data["result"]["data"]["lists"]
        if not info_list:
            info_list = []
        self.logger.info(f"关键词：{kw}，第{page}页，共{len(info_list)}条数据")
        for info in info_list:
            main_info = info.get("main")
            print(main_info.get("title"))


if __name__ == '__main__':
    from scrapy.cmdline import execute

    execute("scrapy crawl heimao".split())
