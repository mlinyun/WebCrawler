"""抽象基类"""

"""
抽象基类（Abstract Base Classes，简称 ABC）是面向对象设计中的一个重要概念。
它们提供了一种机制，用于定义接口或规范，强制派生类实现特定的方法和属性，
从而确保类的结构和行为符合预期。通过使用抽象基类，开发者可以在设计阶段
明确类的接口，从而提高代码的可维护性和可扩展性

并且抽象基类能为复杂系统的设计提供了更高的灵活性和更强的控制力。
抽象基类允许你定义通用接口，帮助你在编写代码时避免重复和错误。
它们使得不同类之间的协作变得更加一致，因为每个实现类都必须遵循抽象基类定义的接口。
这种设计不仅提升了代码的清晰度，还减少了耦合，使得系统能够更加模块化和可扩展。

此外，抽象基类为实现多态性和接口规范提供了有力支持，使得不同的类可以以统一的方式进行操作。
这种一致性对于大型项目和团队开发尤为重要，因为它能够确保各个模块之间的交互符合预期，
减少潜在的集成问题。
"""

# 定义接口
# 目标：假设我们正在开发一个图形类库，其中有各种不同类型的图形对象，
# 如圆形、矩形和三角形。每种图形都应该能够计算其面积和周长
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 使用示例
circle = Circle(5)
print("Circle area:", circle.area())  # 输出：Circle area: 78.53981633974483
# 输出：Circle perimeter: 31.41592653589793
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())  # 输出：Rectangle area: 24
# 输出：Rectangle perimeter: 20
print("Rectangle perimeter:", rectangle.perimeter())


# 强制实现
# 目标：假设我们正在开发一个插件系统，每个插件都必须提供一个特定的接口，
# 例如 run() 方法，用于执行插件的主要功能。我们可以使用抽象基类来确保
# 每个插件都实现了所需的方法
class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass


class EmailPlugin(Plugin):
    def run(self):
        print("Sending email...")


class SMSPlugin(Plugin):
    def run(self):
        print("Sending SMS...")


# 使用示例
email_plugin = EmailPlugin()
email_plugin.run()  # 输出：Sending email...

sms_plugin = SMSPlugin()
sms_plugin.run()  # 输出：Sending SMS...

for cl in [EmailPlugin, SMSPlugin]:
    plugin = cl()
    plugin.run()


# 代码组织
# 目标：假设我们正在开发一个框架，其中有各种不同类型的存储引擎，
# 如 MySQL、SQLite 和 MongoDB。每个存储引擎都应该能够执行
# 基本的数据库操作，如连接、查询和关闭。我们可以使用抽象基类
# 来组织这些不同类型的存储引擎
class DatabaseEngine(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQLEngine(DatabaseEngine):
    def connect(self):
        print("Connecting to MySQL database...")

    def query(self, sql):
        print("Executing MySQL query:", sql)

    def close(self):
        print("Closing MySQL connection...")


class SQLiteEngine(DatabaseEngine):
    def connect(self):
        print("Connecting to SQLite database...")

    def query(self, sql):
        print("Executing SQLite query:", sql)

    def close(self):
        print("Closing SQLite connection...")


# 使用示例
mysql_engine = MySQLEngine()
mysql_engine.connect()
mysql_engine.query("SELECT * FROM users")
mysql_engine.close()

sqlite_engine = SQLiteEngine()
sqlite_engine.connect()
sqlite_engine.query("SELECT * FROM users")
sqlite_engine.close()
