import hvac

client = hvac.Client(
    url='https://192.168.1.100:8200',
    # token="s.fXX4OZfgckYeAeuHnL3oI89C",  # 使用权限被控制的令牌
    token="s.s5OLZZxTLiEZZzctH4VckVmk",  # 管理员令牌
    verify="/opt/certs/ca.pem"
)

# 是否认证
print(client.is_authenticated())

# 是否解锁
print(client.sys.is_sealed())

