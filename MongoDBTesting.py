import pymongo


myclient = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
mydb = myclient["admin"]       #test-db是数据库名称
mydb.authenticate('myUserAdmin','abc123')


tdb = myclient.admin
post = tdb.test
print("操作ing")
post.insert({'name':"李白", "age":"30", "skill":"Python"})
print("操作完成")