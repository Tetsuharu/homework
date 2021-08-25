#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bottle import route, run


# 静态路由, 访问路径'/'
@route('/')
def index():
    # 仅仅返回文本
    return "qytang bottle home"


# 在本地任意地址0.0.0.0的TCP/6868上运行服务, 开启Debug功能
run(host="0.0.0.0", port=6868, debug=True)
