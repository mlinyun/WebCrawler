"""鸭子类型"""

"""
这个名字最初是源自美国诗人的一句话：当我看到一只像鸭子一样走路、
像鸭子一样游泳、像鸭子一样嘎嘎叫的鸟时，我就把那只鸟称为鸭子。

在静态语言中，有着严格的类型限制，哪怕两个类有着相同的方法，
相同的功能，也不能说他们是一个类型。

Python 中的鸭子类型是动态类型的一种风格，在这种风格在我们
更关心对象的行为，也就是关心它是否具有执行某个操作所需要的
方法和属性，而不关心对象的类型本身
"""


# 下面是个简单的例子，例如鸭子会跑，小狗也会跑，代码示例如下：
class Duck:
    def run(self):
        print('鸭鸭跑步')

class Dog:
    def run(self):
        print('狗狗跑步')

def go(animal):
    animal.run()

duck = Duck()
dog = Dog()

go(duck)
go(dog)
# 以上代码中，两个对象都可以执行 run 方法，那么就可以认为这俩是同一类型


# 那么我们如何判断一个对象是否能执行一个方法呢，可以用 dir() 来查看
# 对象的方法和属性，也可以用 hasattr() 检查对象是否有某个属性或方法
class Fish:
    def swim(self):
        print('鱼儿游泳')

fish = Fish()
print(dir(duck))  # 输出所有属性
print(hasattr(dog, "run"))  # True
print(hasattr(fish, "run"))  # False


# 在爬虫的开发中，鸭子类型也有很多应用场景，比如我想从不同的数据源去读取数据
# 就可以这么写，不同的类都实现了 fetch 方法，我们就无需进行单独处理了：
class WebPage:
    def fetch(self):
        # 从网页抓取数据
        return "Web page data"

class API:
    def fetch(self):
        # 从 API 获取数据
        return "API data"

class File:
    def fetch(self):
        # 从文件读取数据
        return "File data"

def process_data(source):
    # 不关心 source 的具体类型，只需它实现了 fetch 方法
    data = source.fetch()
    print(f"Processing {data}")

# 使用不同的数据源
webpage = WebPage()
api = API()
file = File()

process_data(webpage)
process_data(api)
process_data(file)
