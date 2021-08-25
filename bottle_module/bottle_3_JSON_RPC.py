#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bottle import run, post, get, request, response
from datetime import datetime, date


# GET使用动态路由实现RPC
@get('/rpc/<rfc_func>')
def rpc(rfc_func):
    # 可选: 设置响应(response)内容类型(content_type)为'application/json'
    response.content_type = 'application/json'
    # 如果动态传入的参数为'datetime'
    if rfc_func == 'datetime':
        # 返回时间datetime(JSON需要格式化)
        return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    # 如果动态传入的参数为'date'
    elif rfc_func == 'date':
        # 返回日期date(JSON需要格式化)
        return {'datetime': date.today().strftime('%Y-%m-%d')}
    # 如果参数其他参数, 就报错('error'), 'function not find!'
    else:
        return {'error': 'function not find!'}


# POST实现JSON RPC
@post('/rpc_function')
def rpc_function():
    # 可选: 设置响应(response)内容类型(content_type)为'application/json'
    response.content_type = 'application/json'
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    # 如果存在JSON数据
    if client_post_data:
        # 提取键'function'
        client_function = client_post_data.get('function')
        # 如果键'function'的值为datetime, 就返回时间datetime(JSON需要格式化)
        if client_function == 'datetime':
            return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        # 如果键'function'的值为date, 就返回日期date(JSON需要格式化)
        elif client_function == 'date':
            return {'datetime': date.today().strftime('%Y-%m-%d')}
        # 如果没有键'function', 就报错('error'), 'function not found!'
        else:
            return {'error': 'function not found!'}
    # 如果没有JSON数据, 就报错('error'), 'no json data'
    else:
        return {'error': 'no json data'}


# 在本地任意地址0.0.0.0的TCP/6868上运行服务, 开启Debug功能
run(host="0.0.0.0", port=6868, debug=True)
