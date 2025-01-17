from gevent import monkey  # 导入gevent库中的monkey模块
import gevent, time, requests  # 导入gevent、time和requests模块

monkey.patch_all(ssl=False)  # 打补丁以实现协程支持，禁用SSL补丁

start_time = time.time()  # 记录开始时间
url_list = ['https://www.zyte.com/blog'] * 1000  # 创建一个包含1000个相同URL的列表


def crawler(url):  # 定义爬虫函数
    response = requests.get(url)  # 发送GET请求
    print(len(response.content))  # 打印响应内容的长度


tasks_list = []  # 初始化任务列表
for url in url_list:  # 遍历URL列表
    task = gevent.spawn(crawler, url)  # 为每个URL创建一个协程任务
    tasks_list.append(task)  # 将任务添加到任务列表
gevent.joinall(tasks_list)  # 等待所有协程任务完成
print(f'耗时 {time.time() - start_time} 秒')  # 打印总耗时
