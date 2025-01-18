import requests
from bs4 import BeautifulSoup

# 发送 GET 请求
url = "https://www.example.com"
# 异常处理
try:
    response = requests.get(url=url)
    response.raise_for_status()  # 检查响应状态
except requests.RequestException as e:
    print(f"请求出错：{e}")
    response = None

if response:
    # 获取网页内容
    html = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, "html.parser")
    print(soup.title.string)  # 打印网页标题
else:
    print("请求失败")
