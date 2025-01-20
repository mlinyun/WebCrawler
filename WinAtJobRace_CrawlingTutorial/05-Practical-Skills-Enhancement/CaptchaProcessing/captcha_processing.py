from PIL import Image

# 打开图片
image = Image.open("./images/captcha.png")

# 转为灰度图
image = image.convert("L")

# 二值化, 自定义阈值
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, "1")

# image.show()

# 使用 ddddocr 识别验证码
from ddddocr import DdddOcr

orc = DdddOcr()
image2 = open("./images/captcha.png", "rb").read()
result = orc.classification(image2)
print(result)