from pymongo import MongoClient
import json
from bson import json_util


# 建立和数据库系统的连接,指定host及port参数
client = MongoClient('129.204.178.29', 27017)
# 连接mydb数据库,账号密码认证
db = client.monitor
db.authenticate("monitor", "DReqd0AqLCUTgVzx")
# 连接表
collection = db.myset


# 访问表的一行数据
results=collection.find_one()
print(results)
results['asset_type']='server'
results['sn']=results['InstanceId']
results['os_distribution']='Linux'
results['os_type']='Linux'
results['os_release']=results['OsName']
results['cpu_count']=1
results['cpu_model']='inter'
results['cpu_core_count']=results['CPU']
#固定插槽
results['ram']=[{"slot": "A1","capacity": results['Memory']}]
# results['physical_disk_driver']=[{"model":"FAST","size":results['DataDisks'][0]['DiskSize'],"sn":results['DataDisks'][0]['DiskId']}]
results['physical_disk_driver']=[{"model":"FAST","size":"666","sn":results['DataDisks'][0]['DiskId']}]
results['idcname']=results['Placement']['Zone']
results['ip']=results['PrivateIpAddresses']
print(results['physical_disk_driver'])
print(results['DataDisks'][0]['DiskSize'])
#转换为json格式
print(json_util.dumps(results))
