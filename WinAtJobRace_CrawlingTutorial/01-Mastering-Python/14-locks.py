"""在多线程中使用锁"""

"""
在 Python 中，多线程编程时经常需要考虑到线程安全性的问题，特别
是多个线程可能同时访问和修改共享的资源。为了避免数据竞争和确保
数据的一致性，Python 提供了多种同步原语，其中最常用的是锁。

锁是一种同步原语，用于在多线程中控制对共享资源的访问。它可以
确保在任意时刻只有一个线程可以持有锁，从而避免多个线程同时修改
共享数据导致的问题。

在 Python 中，最常用的锁是 threading 模块中提供的 Lock 对象。
它的基本用法如下：
    - 创建锁对象：使用 threading.Lock() 创建一个锁对象。
    - 获取锁：使用 acquire() 方法获取锁。如果锁已经被其他线程持有，
      则 acquire() 方法会阻塞当前线程，直到锁被释放。
    - 释放锁：使用 release() 方法释放锁，让其他线程可以获取到锁并执行。
"""

# 共享变量，所有线程都将访问和修改它
import threading

shared_value = 0


# 不使用锁的加法操作函数
def add_without_lock():
    global shared_value
    for _ in range(100000):
        shared_value += 1  # 递增共享变量


# 不适用锁的减法操作函数
def subtract_without_lock():
    global shared_value
    for _ in range(100000):
        shared_value -= 1  # 递减共享变量


# 创建一个锁对象，用于同步线程对共享资源的访问
lock = threading.Lock()


# 使用锁的加法操作函数
def add_with_lock():
    global shared_value
    for _ in range(100000):
        with lock:  # 使用锁来保护对共享变量的访问
            shared_value += 1


# 使用锁的减法操作函数
def subtract_with_lock():
    global shared_value
    for _ in range(100000):
        with lock:
            shared_value -= 1


# 不使用锁的测试
shared_value = 0  # 重新初始化共享变量
threads = []  # 线程列表

# 启动两个线程，分别执行加法和减法操作
for _ in range(2):
    # 创建执行加法操作的线程
    t1 = threading.Thread(target=add_without_lock)
    # 创建执行减法操作的线程
    t2 = threading.Thread(target=subtract_without_lock)
    t1.start()  # 启动加法线程
    t2.start()  # 启动减法线程
    threads.append(t1)  # 保存线程对象
    threads.append(t2)  # 保存线程对象

# 等待所有线程完成
for t in threads:
    t.join()

# 打印不使用锁的情况下的结果
print(f"Without lock: final value is {shared_value}")

# 使用锁的测试
shared_value = 0  # 重新初始化共享变量
threads = []

# 启动两个线程，分别执行加法和减法操作
for _ in range(2):
    t1 = threading.Thread(target=add_with_lock)  # 创建执行加法操作的线程
    t2 = threading.Thread(target=subtract_with_lock)  # 创建执行减法操作的线程
    t1.start()  # 启动加法线程
    t2.start()  # 启动减法线程
    threads.append(t1)  # 保存线程对象
    threads.append(t2)  # 保存线程对象

# 等待所有线程完成
for t in threads:
    t.join()

# 打印使用锁的情况下的结果
print(f"With lock: final value is {shared_value}")
