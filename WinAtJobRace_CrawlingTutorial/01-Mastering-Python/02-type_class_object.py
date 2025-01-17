"""type, class, object 的关系"""

# type() 函数可以查看对象的类型，比如 num = 10086，
# num 的 type 是 int，那么 int 的 type 是啥呢？
num = 10086
print("Type:", type(num))
print(type(int))


# 从输出的结果可以看到 int 的 type 还是 type，那么就可以看出，
# type 类生成了 int 类，然后又被我们实例化使用，那么 type 类
# 的作用就可以理解为用来生成类（class）

# 下面来看一下 class 的继承关系，插一个知识，使用__bases__可以查看一个类的直接父类
class Room:
    pass
class MyRoom(Room):
    pass


print(MyRoom.__base__)
print(Room.__base__)
print(object.__base__)
print(type(object))
print(type.__base__)
# 可以看到 MyRoom 类继承 Room 类，Room 类继承了 object 类
# object 没有继承任何类，因为 object 是所有类的基础类，不管
# 继承关系如何复杂，最后都是继承了 object，object 是最顶级的类了

# 看到这可能会疑惑 type 和 object 的关系，看代码得知 object 的类型是 type
# 也就是 object 类是 type 实例化而来，但是 type 的父类又是 object
# 像是循环依赖一样，其实在 Python 被设计的时候，type 即是类又是对象
# 拥有双重身份，这种设计理解起来可能比较绕，但是为 Python 提供了强大
# 的元编程能力，使得我们可以在运行时动态地创建、修改和操作类和对象，
# 从而实现更加灵活和强大的编程模式
