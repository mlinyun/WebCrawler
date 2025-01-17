"""Python中的生成器函数"""
from bs4 import BeautifulSoup
import requests


# 生成器函数是一种用于创建迭代器的特殊函数，它们能够逐步生成
# 序列中的元素而不是一次性加载所有数据。这种按需生成的特性
# 使得生成器函数特别适合处理大规模数据或需要节省内存的情况。
# 利用生成器，我们可以在内存有限的环境下高效地处理大量数据流，
# 并且避免了传统方法中的性能瓶颈

# 生成器函数是一种特殊的函数，可以使用 yield 语句生成值。
# 它们与普通函数不同，普通函数使用 return 返回一个值并且
# 调用栈被销毁，而生成器函数可以在生成值后保持状态，并且
# 能够在下次调用时从上次离开的地方继续执行。这种特性使得
# 生成器函数非常适合处理大数据集或需要逐步处理的任务，比如
# 爬虫中的数据提取和处理。以下代码比较了 return 和 yield 的区别：
def fun1():
    return 1

def fun2():
    yield 2

f1 = fun1()
f2 = fun2()
print(f1)
print(f2)
print(next(f2))
# 可以看出 yield 并没有输出 2，而是返回的是生成器类型，
# 需要使用 next 才能进行调用

# 生成器对象，并不会即时返回，这种特性有个经典的应用，
# 那就是斐波那契数列，可以用的时候在进行计算，能节省内存空间
# 例如下述代码， 要计算斐波那契数列的第一万项，使用生成器函数，就可以循环计算
def fibonacci_generator():
    a, b = 0, 1
    count = 0
    while True:
        yield a
        a, b = b, a + b
        count += 1

# 创建生成器对象
fib_gen = fibonacci_generator()

# 找到斐波那契数列的第一万项
for i in range(10000):
    fibonacci_number = next(fib_gen)

# 输出第一万项
print(f"The 10000th Fibonacci number is: {fibonacci_number}")


# 在爬虫领域，如果我们要处理很多新闻，也可以使用 yield 进行分批处理，代码如下：
def fetch_news_titles(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # 假设每个新闻标题在 <h2> 标签内
        for headline in soup.find_all("h2"):
            yield headline.text.strip()

# 使用生成器函数逐个处理新闻标题
urls = ["http://example.com/news/page1", "http://example.com/news/page2"]
titles_generator = fetch_news_titles(urls)

for title in titles_generator:
    print(title)
