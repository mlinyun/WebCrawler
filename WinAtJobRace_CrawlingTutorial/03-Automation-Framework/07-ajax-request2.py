import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""拦截 ajax 请求"""


def parse_log(browser):
    """
    解析日志
    :param browser: 浏览器对象
    :return: 返回解析后的日志
    """
    response_list = []
    perf_list = browser.get_log("performance")
    # print(perf_list)
    for row_log in perf_list:
        log_json = json.loads(row_log["message"])
        message_log = log_json["message"]
        request_id = message_log["params"].get("requestId")
        request_url = message_log["params"].get("response", {}).get("url")
        if not request_id or not request_url:
            continue
        if "spa6.scrape.center/api/movie/" in request_url:
            content = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
            response_list.append({"url": request_url, "content": content.get("body")})
    return response_list


# 配置 Chrome 驱动器路径
service = Service(executable_path="./driver/chromedriver.exe")
# 配置浏览器启动参数
chrome_options = webdriver.ChromeOptions()
# 设置浏览器启动最大化
chrome_options.add_argument("--start-maximized")
# 禁用浏览器正在被自动化程序控制的提示
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 让 selenium 能记录日志
chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL", "performance": "ALL"})

# 实例化一个浏览器对象
browser = webdriver.Chrome(service=service, options=chrome_options)
# 打开页面
browser.get("https://spa6.scrape.center/")
time.sleep(2)
# 解析日志
res = parse_log(browser)

# 关闭页面
browser.close()
# 关闭浏览器
browser.quit()

# 解析电影数据
movie_content_json = json.loads(res[0]["content"])
movie_results = movie_content_json.get("results")
print(f"{'Name':<10} {'Alias':<25} {'Score':<8} {'Regions'}")
print("=" * 65)
for movie in movie_results:
    # print(movie)
    name = movie.get("name")
    alias = movie.get("alias")
    score = movie.get("score")
    regions = ", ".join(movie.get("regions"))
    print(f"{name:<10} {alias:<25} {score:<8} {regions}")
