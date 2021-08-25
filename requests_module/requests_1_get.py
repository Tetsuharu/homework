#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
from PIL import Image  # pip install Pillow
from io import BytesIO

# 响应为文本
request_result = requests.get('http://192.168.1.100:8080')

print(request_result.text)

# 响应为JSON
request_result = requests.get('http://192.168.1.100:8080/rpc/datetime')

print(request_result.json())

request_result = requests.get('http://192.168.1.100:8080/rpc/date')

print(request_result.json())

request_result = requests.get('http://192.168.1.100:8080/rpc/other')

print(request_result.json())

# 下载图片
r = requests.get('https://qytsystem.qytang.com/static/images/logo.jpg')

imgContent = r.content

# 在PyCharm中展示图片
i = Image.open(BytesIO(r.content))
i.show()

# 下载并保存图片
imageFile = open('qyt_logo.jpg', 'wb')
imageFile.write(imgContent)
imageFile.close()
