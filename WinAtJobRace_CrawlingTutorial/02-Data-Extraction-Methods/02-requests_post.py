"""HTTP/HTTPS POST 请求"""
import requests

url = "https://reqres.in/api/users"

data = {
    "name": "John Doe",
    "job": "Software Developer"
}

response = requests.post(url=url, json=data)
print("状态码：", response.status_code)
print("响应头：", response.headers)
print("响应正文：", response.json())

"""
post 函数有两个参数，分别是 json 和 data，这俩参数有以下注意事项：
    - 不管 json 是 str 还是 dict，如果不指定 headers 中的 content-type，
      默认为 application/json
    - json 为 dict 时，如果不指定 content-type，默认为 application/json
    - json 为 str 时，如果不指定 content-type，默认为 application/json

    - data 为 dict 时，如果不指定 content-type，
      默认为 application/x-www-form-urlencoded，相当于普通 form 表单提交的形式
    - data 为 str 时，如果不指定 content-type，默认为 text/plain

    - 用 data 参数提交数据时，request.body 的内容则为 a=1&b=2 的这种形式，
      用 json 参数提交数据时，request.body 的内容则为"{“a”: 1, “b”: 2}’的这种形式

还有一些其他请求，用的比较少，就不展开演示了：
"""
r_put = requests.put("https://jsonplaceholder.typicode.com/posts", data={"key": "value"})
r_delete = requests.delete("https://jsonplaceholder.typicode.com/posts")
r_head = requests.head("https://jsonplaceholder.typicode.com/posts")
r_options = requests.options("https://jsonplaceholder.typicode.com/posts")
