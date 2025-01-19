from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
# 启动参数对象
options = webdriver.ChromeOptions()
# 设置浏览器启动最大化
options.add_argument("--start-maximized")
# 禁用浏览器正在被自动化程序控制的提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 创建浏览器对象
browser = webdriver.Chrome(service=service, options=options)

try:
    # 使用 get 打开登录页面
    browser.get(
        "http://127.0.0.1:5500/WinAtJobRace_CrawlingTutorial/03-Automation-Framework/login/login.html"
    )  # 替换为你的 HTML 文件地址
    time.sleep(2)  # 根据实际情况调整等待时间

    # 输入用户名和密码
    browser.find_element(By.ID, "username").send_keys("username")  # 替换为你的用户名
    browser.find_element(By.ID, "password").send_keys("password")  # 替换为你的密码

    # 模拟滑块操作
    slider = browser.find_element(By.ID, "slider")
    thumb = browser.find_element(By.ID, "thumb")
    action = ActionChains(browser)

    # 执行滑块拖动操作
    action.click_and_hold(thumb).move_by_offset(260, 0).release().perform()

    # 提交表单
    browser.find_element(By.XPATH, "//button[text()='Login']").click()

    # 等待页面跳转
    time.sleep(2)  # 根据实际情况调整等待时间

    # 确保跳转后的页面已经加载完成
    table = browser.find_element(By.XPATH, "//table")

    # 提取表格数据
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        print(data)
        time.sleep(1)

    browser.quit()
except Exception as e:
    print(f"出错：{e}")
    browser.quit()
finally:
    browser.quit()
