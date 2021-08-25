#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from flask import Flask, render_template, request
import os
# 默认目录为当前目录的templates
template_dir = os.path.abspath('../templates')
# 修改目录
node = Flask(__name__, template_folder=template_dir)
# 打开Debug
node.debug = True


@node.route('/form', methods=['GET', 'POST'])
def form():
    # POST表示客户提交表单
    if request.method == 'POST':
        # 提取客户填写的参数name
        name = request.form.get('name')
        # 提取客户填写的参数age
        age = request.form.get('age')
        # 返回页面form_result.html, 里边显示客户填写的name和age信息
        return render_template('form_result.html', name=name, age=age)
    # else为GET请求, 给客户返回空表单
    else:
        return render_template('form.html')


if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
