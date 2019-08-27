import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devsys.settings")# project_name 项目名称
django.setup()

from pymongo import MongoClient

from assets.models import Asset

# 建立和数据库系统的连接,指定host及port参数
client = MongoClient('129.204.178.29', 27017)
# 连接mydb数据库,账号密码认证
db = client.monitor
db.authenticate("monitor", "DReqd0AqLCUTgVzx")
# 连接表
collection = db.myset
# results=list(collection.find())
results=list(collection.find().limit(900))
for i in results:
    name1=i['InstanceId']
    print(i)
    #环境名
    if "uat" in name1:
        envir1="uat环境"
    elif "test" in name1:
        envir1="测试环境"
    elif "dev" in "name1":
        envir1="dev环境"
    else:
        envir1="生产环境"
    #print(envir1)
    #操作系统
    ossys1=i['OsName']
    print(ossys1)
    #用户名
    userid1="root"
    #密码
    userpasswd1=""
    #内网IP
    ipin1=i['PrivateIpAddresses'][0]
    print(ipin1)
    #外网IP
    if i['PublicIpAddresses']:
        ipout1=i['PublicIpAddresses']
    else:
        ipout1=""
    print("ipout")
    #CPU信息
    cpu1=i['CPU']
    #内存信息
    mem1=i['Memory']
    #描述信息
    desc1=""
    #系统盘
    sysdisk1=i['SystemDisk']['DiskSize']
    print(sysdisk1)
    #数据盘
    if i['DataDisks']:
        disksize=0
        for p in i['DataDisks']:
            disksize+=p['DiskSize']
        print("总大小为%d"%(disksize))
    datadisk1=disksize
    #带宽
    bandwidth1=i['InternetAccessible']['InternetMaxBandwidthOut']
    print(bandwidth1)
    #secgroup
    if i['SecurityGroupIds']:
        secgroup1=i['SecurityGroupIds'][0]
    print(secgroup1)
    #分组
    if i ['Tags']:
        group1=i['Tags'][0]['Value']
    else:
        group1=""
    print(group1)