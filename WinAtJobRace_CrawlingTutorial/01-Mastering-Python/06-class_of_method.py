"""类中的方法"""

# Python 中，类的方法可以分为三种主要类型：实例方法、静态方法和类方法


"""实例方法"""
# 实例方法是定义在类中的普通方法，它们可以访问实例的属性和方法。
# 实例方法的第一个参数通常是 self（是约定俗成的写法，并不是特定的名字），
# 用于引用当前实例对象。通过 self，实例方法可以操作和修改实例的状态。
# 实例方法可以直接调用类的其他方法和属性

# 应用场景：实例方法通常用于在类内部操作实例的状态和行为，
# 例如修改实例的属性值、执行与实例相关的计算或操作等
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print(f"当前日期为 {self.year}-{self.month}-{self.day}")

    # 静态方法
    # @staticmethod
    # def parse_str(time_str):
    #     year, month, day = time_str.split("-")
    #     return Date(year, month, day)

    @classmethod
    def parse_str(cls, time_str):
        year, month, day = time_str.split("-")
        return cls(year=year, month=month, day=day)
    # 代码中用 cls 代替了硬编码，这样子我们就不必因为类名字转变而修改静态方法了


now_date = Date(2025, 1, 17)
now_date.display()

# 这个案例是比较简单的，实例画的时候需要传入三个 int 类型参数，
# 年月日，那么我们如果传入别的格式，比如2025-1-17，该怎么做呢？
# 可以像下边这样处理下：
time_str = "2025-1-17"
year, month, day = time_str.split("-")
now_date = Date(year, month, day)
now_date.display()
# 我们使用 split 进行字符串处理成我们想要的，在传入到类中，
# 但是如果多处调用，每个地方都这么写，不仅繁琐还容易出错，
# 怎么去优化一下呢？


"""静态方法"""
# 静态方法是定义在类中的普通函数，与实例无关。它们通常用于执行与类相关的操作，
# 但不需要访问实例的属性或方法。我们可以通过 @staticmethod 装饰器来将一个方法声明为静态方法

# 应用场景：静态方法通常用于实现与类相关的功能，但不需要访问实例的状态。
# 例如，可以在静态方法中实现通用的辅助函数，或者在类中封装一些独立于实例的逻辑

# 通过静态方法的定义，我们可以将处理字符串的操作，在方法中进行
# 在上面的 Date 类中添加 parse_str() 静态方法，然后我们再实例化一个 Date
time_str = "2025-01-17"
now_date = Date.parse_str(time_str)
now_date.display()
# 上边的代码，就通过静态方法，支持了对新格式字符串的处理，对于上边的例子，
# 还可以用静态方法做好多事，比如可以判断参数是否合法，正确的时间才进行实例化等
# 但是这个代码还有瑕疵，如果我们想修改类名字，由于静态方法中是把静态方法写死了，
# 那么类名字改变，静态方法的代码也要变，有些繁琐了，有什么办法能避免这个问题呢？
# 那么就要引入类方法了


"""类方法"""
# 类方法是定义在类中的方法，与实例无关，但与类相关。类方法的第一个参数通常被命名
# 为 cls（和 self 一样，也是约定俗成的写法），表示对当前类的引用。我们可以通过
# 这个参数访问类的属性和其他类方法。我们可以通过 @classmethod 装饰器来将一个方法声明为类方法。

# 应用场景：类方法通常用于实现与整个类相关的功能，例如对类级别的属性进行操作、
# 创建工厂方法以便创建特定类型的实例等
# 在上面的 Date 类中添加 parse_str() 类方法，然后我们再实例化一个 Date
time_str = "2025-01-17"
now_date = Date.parse_str(time_str)
now_date.display()
