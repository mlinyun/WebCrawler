"""BeautifulSoup"""
import requests
from bs4 import BeautifulSoup

# 发送请求
url = "https://quotes.toscrape.com"
try:
    response = requests.get(url=url)
    response.raise_for_status()  # 检查响应状态
except requests.RequestException as e:
    print(f"请求出错：{e}")
    response = None

if response:
    # 获取网页内容
    html = response.text

    # 解析 HTML
    soup = BeautifulSoup(html, "html.parser")

    # 提取数据
    quotes = []

    # 查找所有类名为 quote 的 div
    div_quote = soup.find_all("div", class_="quote")
    for quote in div_quote:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    print(quotes)

"""bs4 的基本语法如下"""
# 查找单个元素
# 查找第一个 <p> 标签
p_tag = soup.find("p")
print(p_tag.text)

# 查找所有匹配的元素：
# 查找所有 <p> 标签
p_tags = soup.find_all("p")
for tag in p_tags:
    print(tag.text)

# 查找具有特定属性的元素：
# 查找具有 class="description" 的 <p> 标签
description_paragraphs = soup.find_all("p", class_="description")
for p in description_paragraphs:
    print(p.text)

# 访问元素属性：
# 查找 <a> 标签并访问其 href 属性
a_tag = soup.find("a")
print(a_tag["href"])

# 访问子元素：
# 查找 <body> 标签中的第一个 <p> 标签
body_tag = soup.find("body")
first_p_in_body = body_tag.find("p")
print(first_p_in_body.text)

# 便利所有子元素：
# 遍历 <body> 中的所有子元素
for element in soup.body.children:
    print(element)
