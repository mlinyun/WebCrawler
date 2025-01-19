import time
from DrissionPage import ChromiumPage
from DrissionPage.common import Settings

# 设置语言
Settings.set_language("zh_cn")

# 启动或接管浏览器，并创建标签页对象
tab = ChromiumPage().latest_tab
# 跳转到 gitee 登录页面
tab.get("https://gitee.com/login")

# 定位到账号文本框，获取文本框元素
account_input = tab.ele("#user_login")
# 输入账号
account_input.input("username")
# 定位到密码文本框，获取文本框元素
password_input = tab.ele("#user_password")
# 输入密码
password_input.input("password")
# 定位到登录按钮，获取按钮元素
login_button = tab.ele("@value=登 录")
# 点击登录按钮
login_button.click()

# 关闭标签页
tab.close()
# 关闭浏览器
tab.quit()
# 退出 Chrome Driver
ChromiumPage().quit()

# 其他示例
# div1 = tab.ele("#one")  # 获取 id 为 one 的元素
# p1 = tab.ele("@name=row1")  # 获取 name 属性为 row1 的元素
# div2 = tab.ele("第二个 div")  # 获取包含“第二个 div”文本的元素
# div_list = tab.eles("tag:div")  # 获取所有 div 元素
# div1 = tab.ele("#one")  # 获取到一个元素 div1
# p_list = div1.eles("tag:p")  # 在 div1 内查找所有 p 元素
# div2 = div1.next()  # 获取 div1 后面一个元素
