#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from bottle import run, request, route, TEMPLATE_PATH, jinja2_template

TEMPLATE_PATH.append('../templates')


# 静态路由'/form', 限制method仅能使用GET或POST
@route('/form', method=['GET', 'POST'])
def form():
    # POST表示客户提交表单
    if request.method == 'POST':
        # 提取客户填写的参数name
        name = request.forms.get('name')
        # 提取客户填写的参数age
        age = request.forms.get('age')
        # 返回页面form_result.html, 里边显示客户填写的name和age信息
        return jinja2_template('form_result.html',  {'name': name, 'age': age})
    # else为GET请求, 给客户返回空表单
    else:
        return jinja2_template('form.html')


# 在本地任意地址0.0.0.0的TCP/6868上运行服务, 开启Debug功能
run(host="0.0.0.0", port=6868, debug=True)
