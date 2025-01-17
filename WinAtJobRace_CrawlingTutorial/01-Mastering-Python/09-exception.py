""""上下文管理器的异常处理"""
class Resource:
    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(exc_type)  # 异常类型
        print(exc_value)  # 异常值
        print(exc_tb)  # 异常的错误栈信息
        return True

    def operate(self):
        print(1 / 0)

with Resource() as res:
    res.operate()

# 从输出可以看到异常的详细信息，我们可以在 exit 中对异常进行处理，
# 只要最终的返回结果是 True，那么程序就不会抛出异常，继续向下运行，
# 当主逻辑代码没有报异常时，这三个参数将都为 None
