#!/usr/bin/env python

from pymongo import Connection
import time
import datetime

connection = Connection('115.220.10.112', 27017)
db = connection['hawaii']

#时间记录器
def func_time(func):

    def _wrapper(*args,**kwargs):

        start = time.time()
        func(*args,**kwargs)
        print func.name,'run:',time.time()-start
    return _wrapper

@func_time
def insert(num):

    posts = db.userinfo

    for x in range(num):

        post = {"_id" : str(x),
                "author": str(x)+"Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}

        posts.insert(post)


if name == "main":

    #设定循环500万次
    num = 5000000
    insert(num)