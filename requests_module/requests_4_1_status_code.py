#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests

r = requests.get('http://192.168.1.100:8080')

print(r.ok)
# 状态码
print(r.status_code)
# 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：
# 由于访问http://192.168.1.100:6666的状态码为200,所以不会产生异常
r.raise_for_status()

r = requests.get('http://192.168.1.100:8080/%qytang')

print(r.ok)
# 状态码
print(r.status_code)
# 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：
# 由于访问http://192.168.1.100:6666/%qytang的状态码为404,所以抛出异常
r.raise_for_status()

