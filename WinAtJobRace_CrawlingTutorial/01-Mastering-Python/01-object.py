""""Python 一切皆对象"""
# 在 Python 中，对象有三个特征：
# - 身份（Identity）：每个对象都有一个唯一的身份标识，可以
#   通过 内置函数 id() 来获取这个身份值是对象在内存中的地址
# - 类型（Type）：对象的类型决定了对象可以做哪些操作以及支持
#   哪些方法。可以使用 type() 函数来获取对象的类型
# - 值（Value）：对象的值是存储在对象中的数据

# 在 Python 中，int 是一个整数对象，他就有这三个特征
num = 10086
print("Identity:", id(num))  # 输出对象的身份
print("Type:", type(num))  # 输出对象的类型
print("Value:", num)  # 输出对象的值


# 在 Python 中，基本数据类型（如整数、浮点数、布尔值、字符串）、
# 数据结构（如列表、元组、字典、集合），都是对象
# 除了上述类型，Python 中的类和函数也是对象，这意味着类和函数
# 也可以进行对象个各种操作，比如赋值、传递给函数、
# 作为函数的返回值，可以添加到集合等：
# 赋值
def hi():
    print("Hello, def")
my_func = hi
my_func()


class MyClass:
    def __init__(self):
        print("Hello, class")
obj = MyClass
obj()


# 传递给函数
def apply_function(func, value):
    return func(value)
# len 是 Python 自带的计算对象长度的函数
result = apply_function(len, "hello")
print(result)


# 作为返回值
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

# 在函数内部返回另一个函数
double = create_multiplier(2)
print(double(5))
