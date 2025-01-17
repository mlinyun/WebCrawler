"""多线程"""
import time
import threading
import requests
from concurrent.futures import ThreadPoolExecutor

# 多线程技术是一种极其重要的概念，它允许程序在同一时间执行多个任务，
# 从而提升了应用程序的效率和响应速度
# 多线程类似于同时执行多个不同程序（也称为轻量级的执行单元），
# 每个线程独立运行，但共享相同的进程资源。这使得程序能够更
# 高效地利用多核处理器和执行并发任务
# 在 Python 中，有两种主要的方式来创建和管理线程：使用 threading 模块
# 或使用 concurrent.futures 模块中的 ThreadPoolExecutor

"""threading"""


# threading 模块提供了一个高级的线程接口，允许我们直接操作线程
# 下面是一个简单的示例，展示了如何使用 threading 模块创建和启动线程

# 定义一个函数用于爬取网页


def crawl_website(url):
    print(f"Crawling {url}")
    time.sleep(2)  # 模拟爬取过程，这里用 sleep 代替
    print(f"Finished crawling {url}")


# 创建线程
thread1 = threading.Thread(target=crawl_website, args=("http://example.com/page1",))
thread2 = threading.Thread(target=crawl_website, args=("http://example.com/page2",))

# 启动线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("All threads finished")

"""concurrent.futures.ThreadPoolExecutor"""


# 另一种常用的方法是使用 ThreadPoolExecutor，它提供了更高级的接口来管理线程池，可以更方便地提交和管理多个线程任务。
# 下面是一个使用 ThreadPoolExecutor 的示例：

# 爬取网页的函数

def crawl_website(url):
    print(f"Crawling {url}")
    response = requests.get(url)
    print(f"Finished crawling {url}, status code: {response.status_code}")


# 创建 ThreadPoolExecutor 对象
with ThreadPoolExecutor(max_workers=2) as executor:
    # 提交任务到线程池
    future1 = executor.submit(crawl_website, "http://example.com/page1")
    future2 = executor.submit(crawl_website, "http://example.com/page2")

    # 获取结果（可选）
    # result1 = future1.result()
    # result2 = future2.result()

# 不需要调用 shutdown()，使用 with 语句会自动管理线程池的关闭
print("All tasks are completed")
