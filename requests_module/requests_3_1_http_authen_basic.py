#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
from requests.auth import HTTPBasicAuth

# HTTP Basic认证
r = requests.get('http://192.168.1.4/level/15/exec/-/show/ip/interface/brief/CR',
                 auth=HTTPBasicAuth('admin', 'Cisc0123'))

print(r.text)
