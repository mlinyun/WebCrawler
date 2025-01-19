import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
browser = webdriver.Chrome(service=service)
actionChains = ActionChains(browser)  # 实例化 ActionChains 对象

# 全屏
browser.maximize_window()
time.sleep(2)
# 使用 get 方法打开一个页面
browser.get("https://www.baidu.com/")
time.sleep(2)

# 找到更多按钮
more_button = browser.find_element(By.XPATH, "//*[@id='s-top-left']/div/a")
# print(more_button.text)

# 鼠标悬停
actionChains.move_to_element(more_button).perform()
time.sleep(2)

# 找到百度 Ai 搜索按钮
ai_button = browser.find_element(By.XPATH, "//*[@id='s_new_search_guide']/div/a")
# print(ai_button.text)
# 鼠标拖拽
actionChains.drag_and_drop(ai_button, more_button).perform()
# 释放鼠标
actionChains.release().perform()
time.sleep(2)

# 找到百度搜索框
baidu_input = browser.find_element(By.XPATH, "//*[@id='kw']")
# 鼠标右键点击
actionChains.context_click(baidu_input).perform()
time.sleep(2)
# 鼠标双击
actionChains.double_click(baidu_input).perform()
time.sleep(2)

# 关闭浏览器
browser.quit()
