"""contextlib"""

# 前边的例子中，我们使用魔法函数构建了一个上下文管理器，难免
# 有些繁琐，那么怎么样能用一个函数快速构建一个上下文管理器呢？
# python 的 contextlib 库提供了丰富的上下文管理器相关的工具，
# 例如 @contextlib.contextmanager 装饰器，就能让一个函数变成一个上下文管理器
import sqlite3
from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Entering the context")
    yield ()
    print("Exiting the context")
# 使用 contextmanager 装饰器的时候，主要分为三块，使用 yield 进行分隔，
# yield 前相当于enter，yield 后相当于exit


# 使用生成器函数创建的上下文管理器
with my_context_manager():
    print("Inside the context")
# 由于代码都在一个方法内，所以要用 yield 语句将控制权交给 with 块，
# 在 with 块执行完毕后继续执行 yield 后面的代码，并且 yield 可以被
# 包在 try 里边，进行异常处理，下边是用 contextmanager 实现的
# sqlite3 查询操作，代码如下
@contextmanager
def open_database(db_name):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()

# 使用这个上下文管理器
with open_database('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print(f"SQLite version: {data}")
