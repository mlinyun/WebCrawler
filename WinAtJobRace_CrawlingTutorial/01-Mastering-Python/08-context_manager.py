"""上下文管理器"""

# 上下文管理器（Context Manager）是一种用于管理资源的机制，
# 它允许你在代码块前后执行一些特定的操作，例如资源的初始化和
# 清理。上下文管理器通常与 with 语句一起使用，以确保资源得以
# 正确管理，即使在出现异常的情况下也能妥善处理


"""
上下文管理器的原理是依赖两个魔法函数：
    - __enter__(self): 在进入 with 语句块时调用
    - __exit__(self, exc_type, exc_value, traceback): 
      在退出 with 语句块时调用，无论是正常退出还是异常退出
如果一个类实现了这两个方法，那就可以使用 with 语句来进行管理
"""
class Resource:
    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("close resource connection")

    def operate(self):
        print("in operation")

with Resource() as res:
    res.operate()
