#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 综合方案,解决400/500 和网络问题的所有except
try:
    r = requests.get('http://192.168.1.100:8080')
    # r = requests.get('http://192.168.1.100:8080/%qytang')
    # r = requests.get('https://qytsystem.qytang.com', timeout=0.001)
    r.raise_for_status()
    print(r.text)
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ReadTimeout:
    print('读取超时')
except requests.exceptions.ConnectTimeout:
    print('连接超时')


