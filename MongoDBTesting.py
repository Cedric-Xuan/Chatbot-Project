import pymongo


myclient = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
mydb = myclient["admin"]       #admin是数据库名称
mydb.authenticate('myUserAdmin','abc123')


tdb = myclient.admin
post = tdb.test         #test是集合，也就是表

#print("执行插入操作ing")
#post.insert({'name':"李白", "age":"30", "skill":"Python"})
#print("插入操作完成")

print("执行查询操作ing")
#result = post.find_one({'style': 'thai'},{'style': 1,'img_url': 1,'_id': 0})

result1 = post.find_one({'style': 'china'},{'style': 1,'popular_menu': {"$slice":1},'_id': 0})
result2 = post.find_one({'style': 'western'},{'style': 1,'popular_menu.img_url': 1,'_id': 0})
result3 = post.find_one({'style': 'japan'},{'style': 1,'popular_menu.img_url': 1,'_id': 0})



print(post.distinct('style'))

print(result1,"\n",result2,"\n",result3)

# for x in post.find({},{'style': 1,'popular_menu.img_url': 1,'_id': 0}):
#     print(x)

