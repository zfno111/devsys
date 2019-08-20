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

# # 查看全部表名称
# db.collection_names()
# print db.collection_names()
#
# # 访问表的数据,过滤查询
# item = collection.find({}, {"name": 1, "age": 21})
# for rows in item:
#     print rows.values()

# 访问表的一行数据
results=collection.find_one()
print(results)
print(type(results))
print(json_util.dumps(results))


