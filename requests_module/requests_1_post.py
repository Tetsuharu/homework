#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

# 响应为文本
request_result = requests.post('http://192.168.1.100:8080/form', data={'name': 'collinsctk', 'age': 40})

print(request_result.text)

# 响应为JSON
request_result = requests.post('http://192.168.1.100:8080/rpc_function', json={'function': 'datetime'})

print(request_result.json())

request_result = requests.post('http://192.168.1.100:8080/rpc_function', json={'function': 'date'})

print(request_result.json())

request_result = requests.post('http://192.168.1.100:8080/rpc_function', json={'function': 'other'})

print(request_result.json())

request_result = requests.post('http://192.168.1.100:8080/rpc_function', json={'other': 'other'})

print(request_result.json())

request_result = requests.post('http://192.168.1.100:8080/rpc_function')

print(request_result.json())
