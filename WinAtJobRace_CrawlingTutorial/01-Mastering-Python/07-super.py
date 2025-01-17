"""super 和继承关系"""


# 在 python 中，super() 函数是用于调用父类的一个方法
class A:
    def __init__(self):
        print("AAA")

class B(A):
    def __init__(self):
        print("BBB")
        super().__init__()

b = B()
# 上述先输出了 BBB 然后是 AAA，就是先调用了 B 的 init 然后是 A 的 init


# 初始化父类属性
class Parent:
    def __init__(self, name):
        self.name = "My name is " + name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child = Child("Tom", 18)
print(child.name)
print(child.age)
# 上述代码中，父类中实现了对 name 参数的处理，子类直接调用，
# 就能使用父类的逻辑，减少了代码量，也能让代码看起来更整洁


# 确保正确的多重继承行为
class A:
    def __init__(self):
        print("A's __init__")

class B(A):
    def __init__(self):
        print("B's __init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C's __init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D's __init__")
        super().__init__()

d = D()
# 相信大家可能会有疑惑，为什么不是 DBAC 呢，这是因为在 python 的继承关系中，
# 并不是简单的深度优先，而是一种叫 C3 线性化的算法来计算属性查找顺序


# MRO
# MRO 是 Method Resolution Order（方法解析顺序）的缩写，
# 它定义了在多重继承情况下，Python 应该按照什么顺序来查找方法和属性
# 如果想直观的查看 mro，可以使用 mro 魔法函数来查看
print(D.__mro__)
# mro 输出的，就是实际的查找顺序了，通过排查这个可以来避免一些难以排查的错误
