from nornir import InitNornir
# pip3 install nornir-netmiko
# pip3 install nornir-jinja2
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from open_source_software_1_2_Nornir.vault.python_script.vault_1_init import client


# 加载配置文件config.yaml
nr = InitNornir(
    config_file="config.yaml",
    # dry_run=True
)

# 过滤出路由器
routers = nr.filter(
    type="router",
    # site='beijing'
)

# 过滤出防火墙
asas = nr.filter(
    type="firewall",
    # site='beijing'
)

# 模板目录
templates_path = './templates/'

# 从vault读取信息,并更新nornir inventory
for host in routers.inventory.hosts.keys():
    # 从vault读取用户名和密码
    vault_data = client.secrets.kv.v2.read_secret_version(
                    mount_point='qytang',
                    path=f'{nr.inventory.hosts[host].platform}/cred'
                    )
    cred_data = vault_data['data']['data']
    # 更新nornir inventory对应host的用户名和密码
    nr.inventory.hosts[host].username = cred_data.get('username')
    nr.inventory.hosts[host].password = cred_data.get('password')

for host in asas.inventory.hosts.keys():
    # 从vault读取用户名,密码和secret密码
    vault_data = client.secrets.kv.v2.read_secret_version(
                    mount_point='qytang',
                    path=f'{nr.inventory.hosts[host].platform}/cred'
                    )
    cred_data = vault_data['data']['data']
    # 更新nornir inventory对应host的用户名,密码和secret密码
    nr.inventory.hosts[host].username = cred_data.get('username')
    nr.inventory.hosts[host].password = cred_data.get('password')
    nr.inventory.hosts[host].connection_options['netmiko'].extras['secret'] = cred_data.get('secret')


# 执行show命令
# 路由器show ip inter brief
netmiko_show_result = routers.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="show ip int br")
print_result(netmiko_show_result)


# 打印返回结果
for i in netmiko_show_result:
    print('-'*50 + 'start' + '-'*50)
    print(i)
    print(type(i))
    print('='*50 + i + '='*50)
    print(type(netmiko_show_result[i].result))
    print(netmiko_show_result[i].result)
    print('-' * 50 + 'end' + '-' * 50)


# 配置路由器函数
def config_routers(task):
    # -------------------------------配置接口-------------------------
    # 读取模板,并且通过参数render为具体配置
    ios_interface_template = task.run(
        name='第一步.1:读取IOS接口配置模板',
        task=template_file,
        template='cisco_ios_interface.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第一步.2:配置路由器接口',
             config_commands=ios_interface_template.result.split('\n'),  # 注意此处提取了上次步操作的结果
             cmd_verify=True)

    # -------------------------------配置OSPF-------------------------
    # 读取模板,并且通过参数render为具体配置
    ospf_template = task.run(
        task=template_file,
        name='第二步.1:读取路由器OSPF模板',
        template='cisco_ios_ospf.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第二步.2:配置路由器OSPF',
             config_commands=ospf_template.result.split('\n'),
             cmd_verify=True)


# 执行配置路由器并打印结果
run_result = routers.run(task=config_routers,
                         name='配置路由器',)
print_result(run_result)


# 配置防火墙函数
def config_asas(task):
    # -------------------------------配置接口-------------------------
    asa_interface_template = task.run(
        task=template_file,
        name='第一步.1: 读取ASA接口配置模板',
        template='asa_interface.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第一步.2: 配置ASA接口',
             config_commands=asa_interface_template.result.split('\n'),
             cmd_verify=True)

    # -------------------------------配置路由-------------------------
    asa_route_template = task.run(
        task=template_file,
        name='第二步.1: 读取ASA路由配置模板',
        template='asa_route.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第二步.2: 配置ASA路由',
             config_commands=asa_route_template.result.split('\n'),
             cmd_verify=True)

    # -------------------配置Object, Static PAT and ACL---------------
    asa_object_and_static_pat_and_acl_template = task.run(
        task=template_file,
        name='第三步.1: 读取Object, Static PAT和ACL的配置模板',
        template='asa_object_and_static_pat_and_acl.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第三步.2: 配置ASA Object, Static PAT和ACL',
             config_commands=asa_object_and_static_pat_and_acl_template.result.split('\n'),
             cmd_verify=True)

    # ---------------------------------配置SNMP-----------------------
    asa_snmp_template = task.run(
        task=template_file,
        name='第四步.1: 读取ASA SNMP配置模板',
        template='asa_snmp.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第四步.2: 配置ASA SNMP',
             config_commands=asa_snmp_template.result.split('\n'),
             cmd_verify=True)

    # ---------------------------------配置Logging-----------------------
    asa_logging_template = task.run(
        task=template_file,
        name='第五步.1: 读取ASA Logging配置模板',
        template='asa_logging.template',
        path=templates_path
    )
    # 传入具体配置, 对设备进行配置, 注意需要".split('\n')"把配置转换为列表
    task.run(task=netmiko_send_config,
             name='第五步.2: 配置ASA Logging',
             config_commands=asa_logging_template.result.split('\n'),
             cmd_verify=True)


# 执行配置防火墙并打印结果
run_result = asas.run(task=config_asas,
                      name='配置ASA防火墙',
                      )
print_result(run_result)
