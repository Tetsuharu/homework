#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from flask import Flask, render_template
import os
# 默认目录为当前目录的templates
template_dir = os.path.abspath('../templates')
# 修改目录
node = Flask(__name__, template_folder=template_dir)
# 打开Debug
node.debug = True


# 静态路由,最简单页面
# 访问路径'/html', 限制method仅能使用GET
@node.route('/html', methods=['GET'])
def html():
    # 模板文件为index.html
    return render_template('index.html')  # 模板文件在templates目录


if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
