#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
# 注意使用fiddler会证书报错!
# 注意linux的/etc/hosts文件的映射
r = requests.get('https://qytsystem.qytang.com/accounts/login/')

# 获取头部内容
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers.get('Content-Type'))

# 获取Cookie(Cookie为头部内容)
print(r.cookies.get_dict())
print(r.cookies.keys())
print(r.cookies.get('csrftoken'))
