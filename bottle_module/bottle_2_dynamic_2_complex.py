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


# 静态路由'/complex', 限制method仅能使用GET
@route('/complex', method=['GET'])
def complex_data():
    # 处理复杂数据
    # 字典:complex_dict
    # 列表:complex_list
    return jinja2_template('complex.html',  {'complex_dict': {'dict_key':  'dict_value'},
                                             'complex_list': ['list1', 'list2']})


# 在本地任意地址0.0.0.0的TCP/6868上运行服务, 开启Debug功能
run(host="0.0.0.0", port=6868, debug=True)

