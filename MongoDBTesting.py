import pymongo


myclient = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
mydb = myclient["admin"]       #admin是数据库名称
mydb.authenticate('myUserAdmin','abc123')


tdb = myclient.admin
post = tdb.test         #test是集合，也就是表

print("执行插入操作ing")
post.insert({'name':"李白", "age":"30", "skill":"Python"})
print("插入操作完成")

print("执行查询操作ing")
result = post.find_one({'name': '李白'})
print(result)