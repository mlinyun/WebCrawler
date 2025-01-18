"""使用 urllib3 发送 GET 请求"""
import urllib3
from bs4 import BeautifulSoup

# 创建一个 HTTP 管道
http = urllib3.PoolManager()

# 发送 GET 请求
url = "https://www.example.com"
# 异常处理
try:
    response = http.request("GET", url)
except urllib3.exceptions.RequestError as e:
    print(f"请求出错：{e}")
    response = None

if response:
    # 获取网页内容
    html = response.data.decode("utf-8")

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, "html.parser")
    print(soup.title.string)  # 打印网页标题
else:
    print("请求失败")
