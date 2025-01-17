"""魔法函数"""


# 在 Python 编程中，魔法函数（也称为特殊方法或双下划线方法）
class Student:
    def __init__(self, name):
        self.name = name


# 像上述代码中__init__这样子双下划线__开头和结尾的函数，就叫魔法函数
# 这种函数在特定的情况下会被 Python 解释器自动调用，用于实现类的特定行为

# Python 还提供了很多魔法函数，下边我们来看几个


# __str__ 函数用于 str() 函数和 print() 函数调用
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass({self.value})"


obj = MyClass(10)
print(obj)  # 输出：MyClass(10)
print(str(obj))  # 输出：MyClass(10)


# __getitem__ 函数是用于实现索引访问列表、字典、元组等
# 当对一个对象使用索引操作时，Python 会自动调用该对象的
# __getitem__ 方法来获取对应索引位置的值
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]


my_list = MyList([1, 2, 3, 4, 5])
print(my_list[0])  # 输出：1
print(my_list[2])  # 输出：3


# __add__ 函数用于定义对象的加法行为。当对两个对象执行加法操作时
# Python 会自动调用这两个对象的 __add__ 方法，并返回其结果
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


point1 = Point(11)
point2 = Point(22)
result = point1 + point2
print(result)  # 输出：33


# __enter__ 和 __exit__ 是用于实现上下文管理器
# 当对象被使用在 with 语句块中时，Python 会自动
# 调用 __enter__ 方法获取上下文管理器，并在退出
# with 语句块时调用 __exit__ 方法
class MyResource:
    def __enter__(self):
        print("Entering the context")
        # 这里可以进行一些资源的初始化操作
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # 这里可以进行一些资源的清理操作


with MyResource() as resource:
    print("Inside the context")

# 在这个示例中，当 MyResource 对象被使用在 with 语句块中时，
# Python 会先调用其 __enter__ 方法进入上下文，然后执行 with
# 语句块内部的代码，最后调用 __exit__ 方法退出上下文。
# 在 __exit__ 方法中，exc_type、exc_value 和 traceback 参数
# 分别表示异常的类型、值和追溯信息。我们可以根据需要在 __exit__
# 方法中处理异常或执行清理操作

"""
通过以上几个示例，魔法函数的作用，可以总结为以下三类：

    - 自定义对象行为：通过实现特定的魔法函数，可以自定义对象
      在不同情况下的行为，例如对象的初始化、字符串表示、比较等
    - 运算符重载：通过实现魔法函数，可以重载对象的运算符，使得
      对象支持与内置类型相同的操作，例如加法、减法等
    - 上下文管理：魔法函数还可以用于实现上下文管理器，通过__enter__
      和__exit__方法，在with语句中管理资源的获取和释放
"""
