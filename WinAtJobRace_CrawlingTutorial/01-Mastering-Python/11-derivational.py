"""Python中的推导式"""
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

# 推导式是一种优雅的语法结构，可以让我们用简洁的方式生成新的列表、
# 集合或字典。它们通过将循环和条件语句结合在一起，使得代码更加直观
# 且易于理解。例如，通过列表推导式，我们可以在一行代码中完成复杂的
# 数据处理任务，这不仅减少了代码量，也提高了可读性

"""列表推导式"""
# 列表推导式顾名思义，就是通过一个式子来生成列表，比如有以下需求，
# 一个新闻类 URL 的路径是自然数，我们要生成前 100 页放到一个列表里
# 一般代码：
url_list = []
for page in range(1, 101):
    url = f"https://example.com/{page}"
    url_list.append(url)
# print(url_list)
# print()
# 看起来比较繁琐，如果用列表推导式来写，那只需要一行代码
url_list2 = [f"https://example.com/{page}" for page in range(1, 101)]
# print(url_list2)
# print()
# 是不是很简单明了，再加点难度，如果只想要页数是 3 的倍数的 URL 呢，那么可以这么写：
url_list3 = [
    f"https://example.com/{page}" for page in range(1, 101) if page % 3 == 0]
# print(url_list3)

# 由上述可以看出，列表推导式的格式是这样的
# [expression for item in iterable if condition]
# expression：对序列中每个元素进行操作或计算的表达式
# item：可迭代对象中的元素
# iterable：可迭代对象，如列表、元组、字符串等
# condition（可选）：筛选条件，只有满足条件的元素才会包含在结果列表中


"""字典推导式"""
# 字典推导式允许你轻松地从一个可迭代对象中创建字典。语法形式为：
# new_dict = {key_expression: value_expression for item in iterable if condition}
# key_expression：字典键的计算方式
# value_expression：字典值的计算方式
# item：可迭代对象中的每个元素
# iterable：可迭代对象
# condition（可选）：过滤条件

# 比如在爬虫中，我们想把新闻的标题和链接存到一个字典里，那么就可以使用字典生成式

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# 获取页面中所有的标题和链接，get("href")是获取标签中的 href 属性，一般指向的页面的 URL，a 标签是超链接
title_link_dict = {title.text: title.get(
    "href") for title in soup.find_all("a")}
print(title_link_dict)

"""集合推导式"""
# 集合推导式与列表推导式类似，只有最外层符号的不同，但是生成的是集合而不是列表。语法形式为：
# new_set = {expression for item in iterable if condition}
# expression：集合中每个元素的计算方式
# item：可迭代对象中的每个元素
# iterable：可迭代对象
# condition（可选）：过滤条件

# 在爬虫中，比如我们想生成一个 URL 列表，但是还不想让 URL 有重复的，就可以使用集合推导式：

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# 获取页面中所有的链接
links = [link.get("href") for link in soup.find_all("a")]

# 提取链接的域名并生成集合
domains = {urlparse(link).netloc for link in links}
print(domains)
