from __future__ import unicode_literals

import pymongo
import redis
import json

# Redis 连接
# HOST = "redis-18235.c228.us-central1-1.gce.cloud.redislabs.com"
# PWD = "w2vwWBPYLIgggR0kiQzkMX7CXN4L1KjC"
# PORT = "18235"
#
# redis1 = redis.Redis(host = HOST, password = PWD, port = PORT, decode_responses = True)


# mogodb 连接
myclient = pymongo.MongoClient("mongodb://115.220.10.112:27017/")
mydb = myclient["admin"]       #admin 是数据库名称
mydb.authenticate('myUserAdmin','abc123')

value1 = {"restaurant":"泰式海南鸡","style":"thai","tel":"+852-24758813","address":"元朗西菁街9號富盛商場地下62號舖","popular_menu":[{"dish":"招牌泰式去骨海南鸡","price":208,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/qghnj.jpg"},{"dish":"酸辣去骨凤爪","price":62,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/fz.jpg"},{"dish":"泰式炒通菜","price":52,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tsctc.jpg"},{"dish":"明炉鱿鱼","price":135,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/mlyy.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tshnj_environment.jpg"}

value2 = {"restaurant":"Add Some Thai","style":"thai","tel":"+852 - 53741988","address":"观塘开源道62号骆驼漆大厦一期9楼D室","popular_menu":[{"dish":"AST小食拼盘","price":90,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/xspp.jpg"},{"dish":"泰式无骨海南鸡半只","price":180,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hnj.jpg"},{"dish":"椰汁芒果糯米饭","price":50,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nmf.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/Add%20Some%20Thai.jpg"}

value3 = {"restaurant":"金泰子泰国餐厅","style":"thai","tel":"+852-21726106","address":"太子柏树街17A号地铺","popular_menu":[{"dish":"海虾刺身","price":88,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hxcs.jpg"},{"dish":"泰式冬阴功","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tsdyg.jpg"},{"dish":"泰式柠檬鲈鱼","price":50,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nmly.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/jtz_environment.jpg"}

value4 = {"restaurant":"Wildfire Pizzabar","style":"western","tel":"+852 - 28495123","address":"山顶山顶道128号凌霄阁1楼2号铺","popular_menu":[{"dish":"波士顿龙虾尾焰角博饼","price":200,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/lx.jpg"},{"dish":"煨牛肉阔面","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/wnkm.jpg"},{"dish":"t骨牛排","price":90,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tgnp.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/Wildfire%20Pizzabar.jpg"}

value5 = {"restaurant":"大满喜日本料理","style":"japan","tel":"+852-36222162","address":"旺角弥敦道601号创兴广场8楼","popular_menu":[{"dish":"烤鳗鱼","price":43,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/kmy.jpg"},{"dish":"三文鱼","price":66,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/swy.jpg"},{"dish":"海胆卷","price":33,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hdj.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/dmx_environment.jpg"}

value6 = {"restaurant":"北京老家","style":"china","tel":"+852-34622518","address":"尖沙咀加拿分道25-31號國際商業信貸銀行大廈8樓","popular_menu":[{"dish":"北京烤鸭","price":108,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/bjky.jpg"},{"dish":"小笼包","price":55,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/xlb.jpg"},{"dish":"水煮鱼片","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/syp.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/beijing_environment.jpg"}

value7 = {"restaurant":"南瀛水产","style":"japan","tel":"+852-23688028","address":"香港尖沙咀金马伦道5号太兴广场5楼","popular_menu":[{"dish":"刺身","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/cs.jpg"},{"dish":"甜虾海胆三文鱼寿司卷","price":68,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hd.jpg"},{"dish":"杂锦天妇罗","price":62,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/thl.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nanyin_environment.jpg"}

# 餐厅数据json格式
# {
#     "restaurant": "泰式海南雞",
#     "tel": "+852-24758813",
#     "address": "元朗西菁街9號富盛商場地下62號舖",
#     "popular_menu": [
#         {
#             "dish": "招牌泰式去骨海南鸡",
#             "price": 208,
#             "img_url": "https://qcloud.dpfile.com/pc/2mRgRTrBFr8PGNxDK-4RaCbxYuxm9j_ftTqzd0_N2v5yQtPkWzOF1DSEEqmqNrtl0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"
#         },
#         {
#             "dish": "酸辣去骨凤爪",
#             "price": 62,
#             "img_url": "https://qcloud.dpfile.com/pc/-DYof9DNPHJELwRaS5ozlu43ziRsWmDWHkW1ZBrHlsmhwknyKhPrQprPwrvPpf_NuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"
#         },
#         {
#             "dish": "泰式炒通菜",
#             "price": 52,
#             "img_url": "https://qcloud.dpfile.com/pc/mRsaf24UzyMGmrzV9r4820C3JSTfhBm61mjqmoSgqKyFff-3Vpg1uQyjg14tVv6euzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"
#         },
#         {
#             "dish": "明炉鱿鱼",
#             "price": 135,
#             "img_url": "https://qcloud.dpfile.com/pc/iXeOlNR0vo7pE0s9Uvdzw8xhmpxfSgZR5-ee0rg14jOyKMVJSEw_x5CADA8FrX9OuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"
#         }
#     ],
#     "environment": "https://qcloud.dpfile.com/pc/UkYuu4jsOZA_RvueVpaT4tIZepNkrUOUhuFxQwfMxrW5YRpPQFkAuvjoyCCuvD3e0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"
# }


# key_style_list = 'style_restaurant_list'
# value_style_list = {"thai":[{"restaurant":"泰式海南雞","tel":"+852-24758813","address":"元朗西菁街9號富盛商場地下62號舖"},{"restaurant":"Add Some Thai","tel":"+852-53741988","address":"观塘开源道62号骆驼漆大厦一期9楼D室"},{"restaurant":"金泰子泰国餐厅","tel":"+852-21726106","address":"太子柏树街17A号地铺"}],"western":[{"restaurant":"Wildfire Pizzabar","tel":"+852-28495123","address":"山顶山顶道128号凌霄阁1楼2号铺"},{"restaurant":"登堂","tel":"+852-21104103","address":"观塘兴业街4号The Wave2楼"},{"restaurant":"BRICK LANE Deli (新城市广场店)","tel":"+852-21110480","address":"沙田正街18号新城市广场一期1楼126号铺"}],"japan":[{"restaurant":"南瀛水产","tel":"+852-23688028","address":"香港尖沙咀金马伦道5号太兴广场5楼"},{"restaurant":"大满喜日本料理","tel":"+852-36222162","address":"旺角弥敦道601号创兴广场8楼"},{"restaurant":"爆丼屋","tel":"+852-23322918","address":"旺角豉油街50号"}],"china":[{"restaurant":"北京老家","tel":"+852-34622518","address":"尖沙咀加拿分道25-31號國際商業信貸銀行大廈8樓"}]}



tdb = myclient.admin

post = tdb.restaurant_list

post.insert_one(value1)
post.insert_one(value2)
post.insert_one(value3)
post.insert_one(value4)
post.insert_one(value5)
post.insert_one(value6)
post.insert_one(value7)
am = post.find({"style":"thai"})
for a in am:
    print(a)






