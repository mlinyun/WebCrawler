import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
browser = webdriver.Chrome(service=service)

# 使用 get 方法打开一个页面
browser.get("https://spa6.scrape.center/")
# 等待页面加载完毕
# time.sleep(4) # 使用 time.sleep() 函数很不优雅，这里我们使用隐式等待或显式等待来优化
# 显示等待
video_card = (WebDriverWait(browser, 10, 0.5)
              .until(EC.presence_of_element_located((By.CLASS_NAME, "el-card__body"))))
# 在 WebDriverWait 这一行就是显式等待，其中 10 是最长等待时间，0.5 是每 0.5 秒去查询对应的元素
# until 后面跟的等待具体条件，EC 是判断条件，检查`el-card__body`元素是否存在于页面的 DOM 上
# 隐式等待
# browser.implicitly_wait(10)  # 隐式等待，最长等 10 秒
video_title = browser.find_elements(By.CLASS_NAME, 'm-b-sm')[0].text
print(video_title)
# 调用 page_source 属性获取页面源码
html = browser.page_source
print(html)

# 关闭页面
browser.close()
# 关闭浏览器
browser.quit()
