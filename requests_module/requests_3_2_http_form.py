#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

from bs4 import BeautifulSoup

# 打开DevNet Enhanced API的DJG项目, 并运行
# 登录URL
url = 'http://192.168.1.100:8000/accounts/login/'

# 登录用户和密码
username = 'admin'
password = 'Cisc0123'

# 建立并保持会话
client = requests.session()
# 获取登录页面的内容
first_html = client.get(url).content
# 使用bs4分析登录页面的内容
soup = BeautifulSoup(first_html, 'lxml')
# 找到csrf令牌的值
csrftoken = soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
# 构建用户名, 密码和csrf值的POST数据
login_data = {'username': username, 'password': password, "csrfmiddlewaretoken": csrftoken}
# POST提交数据到登录页面
client.post(url, data=login_data)

# 一旦登录成功, 打开ASA自动化页面
r = client.get('http://192.168.1.100:8000/asa_auto')
# 打印ASA自动化页面
print(r.text)
