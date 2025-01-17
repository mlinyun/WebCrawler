"""协程"""

# 协程是一种特殊类型的函数，它可以挂起执行并在将来某个时刻恢复。
# 这种特性使得协程非常适合处理需要等待的操作，比如网络请求或磁盘读写。
# 与线程和进程不同，协程不需要频繁切换上下文，因此在处理大量并发任务时，
# 协程通常能够提供更高的效率和更低的资源消耗

# 协程，又称微线程，顾名思义，比线程更加轻量，并且协程是在同一个线程中运行的

import asyncio
import time


# 使用 async 来定义一个异步函数，它返回一个协程对象，而不是直接执行函数内部的代码
async def task1():
    print("任务 1 开始")
    # await 用于暂停异步函数的执行，等待另一个异步任务完成
    await asyncio.sleep(5)
    print("任务 1 完成")


async def task2():
    print("任务 2 开始")
    await asyncio.sleep(4)
    print("任务 2 完成")


async def main():
    # asyncio 是一种工具，用于管理和调度这些协程，提供了事件循环、
    # 任务管理等功能，使得协程能够在异步环境中运行
    # gather 可以调用协程函数
    await asyncio.gather(task1(), task2())


start_time = time.time()
# 运行顶级入口点的异步代码，并处理事件循环的创建、运行和关闭
asyncio.run(main())
end_time = time.time()
total_time = (end_time - start_time)
print(f"total time: {total_time}")
