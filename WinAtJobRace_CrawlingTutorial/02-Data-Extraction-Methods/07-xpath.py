"""Xpath"""
import requests
from lxml import html

# 发送请求
url = "https://quotes.toscrape.com"
try:
    response = requests.get(url=url)
    response.raise_for_status()  # 检查响应状态
except requests.RequestException as e:
    print(f"请求出错：{e}")
    response = None

if response:
    content = response.content
    tree = html.fromstring(content)

    # 使用 xpath 提取
    quotes = tree.xpath("//div[@class='quote']")
    results = []

    for quote in quotes:
        text = quote.xpath(".//span[@class='text']/text()")[0]
        author = quote.xpath(".//small[@class='author']/text()")[0]
        tags = quote.xpath(".//div[@class='tags']/a[@class='tag']/text()")
        results.append({"text": text, "author": author, "tags": tags})

    print(results)
