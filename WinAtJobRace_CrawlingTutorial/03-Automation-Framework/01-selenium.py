import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
browser = webdriver.Chrome(service=service)

# selenium 的基础用法
# 1. 页面相关操作
# 调整窗口大小
# 指定大小
browser.set_window_size(500, 500)
time.sleep(2)
# 全屏
browser.maximize_window()
time.sleep(2)
# 使用 get 方法打开一个页面
browser.get("https://www.baidu.com/")
# 刷新页面
browser.refresh()
# 后退
browser.back()
time.sleep(1)
# 前进
browser.forward()
time.sleep(1)

# 2. 元素操作
# 在 selenium 中，也支持使用 xpath 提取数据
# 找到百度搜索框
baidu_input = browser.find_element(By.XPATH, "//*[@id='kw']")
# 输入框输入内容
baidu_input.send_keys("Python")
time.sleep(1)
# 找到百度搜索按钮
search_button = browser.find_element(By.XPATH, "//*[@id='su']")
# 点击搜索按钮
search_button.click()
time.sleep(4)
# 清除输入框内容
baidu_input.clear()
time.sleep(1)
# 获取搜索按钮左上角的坐标
print(search_button.location)
# 获取搜索按钮左上角的 x 坐标
# print(search_button.location["x"])
print(search_button.location.get("x"))
# 获取搜索按钮左上角的 y 坐标
# print(search_button.location["y"])
print(search_button.location.get("y"))
# 获取搜索按钮的大小
print(search_button.size)
# 获取搜索按钮的宽度
# print(search_button.size["width"])
print(search_button.size.get("width"))
# 获取搜索按钮的高度
# print(search_button.size["height"])
print(search_button.size.get("height"))
# 获取搜索按钮的标签名
print(search_button.tag_name)
# 获取搜索按钮的文本
print(search_button.text)
# 获取搜索按钮的属性
print(search_button.get_attribute("class"))
# 查看搜索按钮是否可见
print(search_button.is_displayed())
# 查看搜索按钮是否启用
print(search_button.is_enabled())
# 查看搜索按钮是否选中
print(search_button.is_selected())

# 关闭浏览器
browser.quit()
