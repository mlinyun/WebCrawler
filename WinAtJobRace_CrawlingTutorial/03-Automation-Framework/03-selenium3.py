import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
# 实例化一个启动参数对象
chrome_options = webdriver.ChromeOptions()
# # 设置浏览器不提供可视化页面
# # chrome_options.add_argument("--headless")
# # 设置编码格式
# chrome_options.add_argument("lang=zh_CN.UTF-8")
# # 禁止策略化
# chrome_options.add_argument("--disable-infobars")
# # 解决 DevToolsActivePort 文件不存在的报错
# chrome_options.add_argument("--no-sandbox")
# # 指定浏览器分辨率
# chrome_options.add_argument("window-size=1920x1080")
# # 谷歌文档提到需要加上这个属性来规避 bug
# chrome_options.add_argument("--disable-gpu")
# # 隐身模式（无痕模式）
# chrome_options.add_argument("--incognito")
# # 禁用 JavaScript
# chrome_options.add_argument("--disable-javascript")
# # 最大化运行（全屏窗口），不设置，取元素的时候可能会报错
# chrome_options.add_argument("--start-maximized")
# # 禁用浏览器正在被自动化程序控制的提示
# # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # 隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument("--hide-scrollbars")
# # 不加载图片, 提升速度
# # prefs = {"profile.managed_default_content_settings.images": 2}
# # chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--blink-settings=imagesEnabled=false")
# # 设置 UA 请求头
# chrome_options.add_argument(
#     "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
# )
# 实例化一个浏览器对象
browser = webdriver.Chrome(service=service, options=chrome_options)
# 打开百度页面
browser.get("https://www.baidu.com/")
time.sleep(2)
# 关闭浏览器
browser.quit()
