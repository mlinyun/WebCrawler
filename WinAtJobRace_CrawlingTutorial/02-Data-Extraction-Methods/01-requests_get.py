"""HTTP/HTTPS GET 请求"""
import requests

# GET 请求
url = "https://reqres.in/api/users"
response = requests.get(url=url)

print("状态码：", response.status_code)
print("响应头：", response.headers)
print("响应正文：", response.json())

# GET 请求是数量最多的请求了，在实际的爬虫中，上述代码大概率
# 会被封，所以我们要抓包，然后修改相应的 headers 等参数，并且
# 如果高频请求一个网站，还要添加代理防止被禁止 ip，还有一个
# 比较常用的参数就是 verify 了，这个参数可以控制是否检验网站
# 的证书，如果遇到 SSLError，就可以将此参数设置为 False，
# 修改后示例如下：

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://jsonplaceholder.typicode.com/posts/1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

# 可选
# proxies = {
#     # 具体信息需要代理供应商提供
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/",
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/"
# }

url = "https://reqres.in/api/users"
# response = requests.get(url=url, headers=headers, proxies=proxies, verify=False)
response = requests.get(url=url, headers=headers, verify=False)
print("状态码：", response.status_code)
print("响应头：", response.headers)
print("响应正文：", response.json())
