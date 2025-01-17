"""多进程"""
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
from multiprocessing import Process
import random
import time

# 在许多计算密集型应用程序中，如何高效地利用系统资源以加速任务处理是一个关键问题。
# Python 提供了多进程编程的能力，为开发者提供了一种强大的工具来充分利用多核处理器，
# 实现真正的并行计算。通过将任务分配到多个进程中，你可以显著提高程序的性能和响应能力，
# 尤其是在处理大量数据或执行复杂计算时。

# 多进程编程涉及创建多个进程来并行执行任务，每个进程都有自己的内存空间和资源。
# 这种方式与多线程不同，因为它绕过了 Python 的全局解释器锁（GIL），使得 CPU
# 密集型任务能够真正并行运行。虽然多进程编程可以增加系统的资源开销，但它在计算
# 密集型场景中的优势是显而易见的。


"""multiprocessing 模块"""
# Python 中的多线程无法利用多核优势，如果想要充分地使用多核 CPU 的资源，
# 在 Python 中大部分情况需要使用多进程。Python 提供了 multiprocessing。
# 创建进程使用的是 Process 方法，定义如下：
# Process([group [, target [, name [, args [, kwargs]]]]])
# group 参数未使用，值始终为 None
# target 表示调用对象，即子进程要执行的任务
# args 表示调用对象的位置参数元组，args=(1,2,"anne",)，注意必须加逗号
# kwargs 表示调用对象的字典，kwargs={"name":"anne","age":18}
# name 为子进程的名称

# 创建进程有两种方法，第一种是直接调用：
def run(name):
    print("%s runing" % name)
    time.sleep(3)
    print("%s running end" % name)

if __name__ == "__main__":
    p1 = Process(target=run, args=("anne",))
    p2 = Process(target=run, args=("alice",))
    p1.start()
    p2.start()
    print("主线程")


# 第二种是继承并重写：
class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s runing" % self.name)
        time.sleep(random.randrange(1, 5))
        print("%s runing end" % self.name)

if __name__ == "__main__":
    p1 = Run("anne")
    p2 = Run("alex")
    p1.start()  # start 会自动调用 run
    p2.start()
    print("主线程")

"""使用进程池采集数据"""
# 进程池是 Python 中用来管理并行进程的工具，它能够简化并行任务的管理和分发。
# 进程池提供了一种方式来动态地管理进程的数量，从而更高效地利用系统资源，
# 特别是在需要执行大量计算密集型或者 I/O 密集型任务时非常有用。

# 下面示例我们用到了 multiprocessing.Pool 模块，通过代码来讲解下用法：
# 使用 Pool 类来创建进程池。可以指定要创建的进程数量（即池中的工作进程数），例如：
# with Pool(processes=4) as pool:
#     # 执行任务使用 pool.map 或者 pool.apply_async
#     # map 方法：适合并行处理多个任务，并等待所有任务完成后返回结果。
#     # 其中，func 是要并行执行的函数，iterable 是一个可迭代对象，例如一个列表，包含了需要处理的任务参数。
#     results = pool.map(func, iterable)
#     # apply_async 方法：用于异步提交单个任务，并返回一个 AsyncResult 对象，可以用来获取任务的结果或者等待任务完成。
#     # func 是要执行的函数，args 是传递给函数的参数元组。
#     result = pool.apply_async(func, args=(arg1, arg2))  # 这将阻塞当前进程，直到任务完成并返回结果。
#     # 如果使用 apply_async 提交任务，可以通过 get() 方法获取任务的返回值：
#     result = result.get()

# 下面来看如果用进程池来写一段爬虫
# 爬取的 URL 列表
urls = [
    "http://example.com/page1",
    "http://example.com/page2",
    "http://example.com/page3",
    # 添加更多的 URL
]


def scrape(url):
    try:
        # 发起请求
        response = requests.get(url)
        # 检查响应状态
        if response.status_code == 200:
            # 解析 HTML
            soup = BeautifulSoup(response.content, "html.parser")
            # 这里可以根据需要进行具体的数据提取操作
            # 这里只是简单地打印页面标题
            print(f"Title of {url}: {soup.title.text.strip()}")
        else:
            print(
                f"Failed to scrape {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while scraping {url}: {str(e)}")


if __name__ == "__main__":
    # 创建进程池，同时处理多个 URL
    with Pool(processes=4) as pool:
        pool.map(scrape, urls)
