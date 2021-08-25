#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from bottle import route, run, static_file, request, post, get, TEMPLATE_PATH, jinja2_template
from datetime import date, datetime

TEMPLATE_PATH.append('../templates')


@route('/')
def index():
    return "qytang bottle home"


@route('/html')
def html():
    return static_file('index.html', root='../templates')


@route('/template', method=['GET'])
def template():
    return jinja2_template('template.html', {'template': 'welcome to qytang!'})


@route('/dynamic/<dynamic_name>', method=['GET'])
def dynamic(dynamic_name):
    return jinja2_template('dynamic.html', {'dynamic': dynamic_name})


@route('/complex', method=['GET'])
def complex_data():
    return jinja2_template('complex.html',  {'complex_dict': {'dict_key':  'dict_value'},
                                             'complex_list': ['list1', 'list2']})


@route('/form', method=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.forms.get('name')
        age = request.forms.get('age')
        return jinja2_template('form_result.html',  {'name': name, 'age': age})
    else:
        return jinja2_template('form.html')


@get('/rpc/<rfc_func>')
def rpc(rfc_func):
    # response.content_type = 'application/json'
    if rfc_func == 'datetime':
        return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    elif rfc_func == 'date':
        return {'datetime': date.today().strftime('%Y-%m-%d')}
    else:
        return {'error': 'function not find!'}


@post('/rpc_function')
def rpc_function():
    # response.content_type = 'application/json'
    client_post_data = request.json
    if client_post_data:
        client_function = client_post_data.get('function')
        if client_function == 'datetime':
            return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        elif client_function == 'date':
            return {'datetime': date.today().strftime('%Y-%m-%d')}
        else:
            return {'error': 'function not found!'}
    else:
        return {'error': 'no json data'}


run(host="0.0.0.0", port=6868, debug=True)
