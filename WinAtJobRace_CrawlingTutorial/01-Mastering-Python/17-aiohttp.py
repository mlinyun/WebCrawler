"""协程在爬虫中的应用"""
# 在爬虫中，协程可以帮助我们更高效地发起多个网络请求。以下是
# 一个使用 aiohttp 库的示例，展示如何使用协程来异步地抓取网页
import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    # 假设我们只提取网页标题
    return soup.title.string


async def fetch_and_parse(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        title = await parse(html)
        print(f"URL: {url} - Title: {title}")


async def main(urls):
    await asyncio.gather(*(fetch_and_parse(url) for url in urls))


urls = [
    "https://www.example.com",
    "https://www.example.com",
    "https://www.example.com",
    "https://www.example.com",
    "https://www.example.com",
]

asyncio.run(main(urls))
