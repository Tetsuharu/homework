#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 乾颐堂内部系统由于数字证书有效,所以直接可以得到结果
r = requests.get('https://qytsystem.qytang.com')

print(r.text)

# 下面两句用于禁止告警信息
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 192.168.1.4为路由器自签名证书,所以需要verify=False
r = requests.get('https://192.168.1.4/webui/',
                 verify=False
                 )

print(r.text)


