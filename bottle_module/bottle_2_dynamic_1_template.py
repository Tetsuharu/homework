#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bottle import route, run, TEMPLATE_PATH, jinja2_template

# 定义模板查询路径
TEMPLATE_PATH.append('../templates')


# 静态路由'/template', 限制method仅能使用GET
@route('/template', method=['GET'])
def template():
    # 使用模板'template.html', 并且传递参数, 进行内容替换
    return jinja2_template('template.html', {'template': 'welcome to qytang!'})


# 动态路由/dynamic/<dynamic_name>, 限制method仅能使用GET
@route('/dynamic/<dynamic_name>', method=['GET'])
def dynamic(dynamic_name):
    # 使用模板'template.html', 并且传递动态参数, 进行内容替换
    return jinja2_template('dynamic.html', {'dynamic': dynamic_name})


# 在本地任意地址0.0.0.0的TCP/6868上运行服务, 开启Debug功能
run(host="0.0.0.0", port=6868, debug=True)
