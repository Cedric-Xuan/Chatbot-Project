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

key1 = 'restaurant_泰式海南鸡'
value1 = {"restaurant":"泰式海南鸡", "style":"thai","tel":"+852-24758813","address":"元朗西菁街9號富盛商場地下62號舖","popular_menu":[{"dish":"招牌泰式去骨海南鸡","price":208,"img_url":"https://qcloud.dpfile.com/pc/2mRgRTrBFr8PGNxDK-4RaCbxYuxm9j_ftTqzd0_N2v5yQtPkWzOF1DSEEqmqNrtl0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"},{"dish":"酸辣去骨凤爪","price":62,"img_url":"https://qcloud.dpfile.com/pc/-DYof9DNPHJELwRaS5ozlu43ziRsWmDWHkW1ZBrHlsmhwknyKhPrQprPwrvPpf_NuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"泰式炒通菜","price":52,"img_url":"https://qcloud.dpfile.com/pc/mRsaf24UzyMGmrzV9r4820C3JSTfhBm61mjqmoSgqKyFff-3Vpg1uQyjg14tVv6euzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"明炉鱿鱼","price":135,"img_url":"https://qcloud.dpfile.com/pc/iXeOlNR0vo7pE0s9Uvdzw8xhmpxfSgZR5-ee0rg14jOyKMVJSEw_x5CADA8FrX9OuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/UkYuu4jsOZA_RvueVpaT4tIZepNkrUOUhuFxQwfMxrW5YRpPQFkAuvjoyCCuvD3e0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

key2 = 'restaurant_add some thai'
value2 = {"restaurant":"Add Some Thai","style":"thai","tel":"+852 - 53741988","address":"观塘开源道62号骆驼漆大厦一期9楼D室","popular_menu":[{"dish":"AST小食拼盘","price":90,"img_url":"https://qcloud.dpfile.com/pc/uXzy_AobaFmymT3-X0ILKcQP4x7oIy7YBgS5WpfQUIsE6GwR889-eGUMyMSWxJjiuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"泰式无骨海南鸡半只","price":180,"img_url":"https://qcloud.dpfile.com/pc/81BeosrDPwo7AFKX_65UvlMuXMTAzsqE6As95YXhlk25dTMBG8P69i-vzcEzx7dLuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"椰汁芒果糯米饭","price":50,"img_url":"https://qcloud.dpfile.com/pc/RvMmTjQdBC7cy6VfqAtJsWiPKl1VP5M34j1oCnsNhWGozkitQKqHlrJgLKwbanFcuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/v_yu-hgIYiZACNR4rqDbTY_6FPYJvdJkbMeENH1-QYILNlrPeiqN3Fqv7YOpYCxtl0cm-Lf9tDMlLZpO7rb3bg.jpg"}

key3 = 'restaurant_金泰子泰国餐厅'
value3 = {"restaurant":"金泰子泰国餐厅","style":"thai","tel":"+852-21726106","address":"太子柏树街17A号地铺","popular_menu":[{"dish":"海虾刺身","price":88,"img_url":"https://qcloud.dpfile.com/pc/pC84Wt8-q3kU-B9icxALD1fWo1dtjFs1uZFtRtwKtOXi4WXlM2FY1te0-7pE3Wb9uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"泰式冬阴功","price":99,"img_url":"https://qcloud.dpfile.com/pc/ol182S_K0nBd8IEeYfgxmzooPKRHvRE2Lw-SNfy-GXsdvtM1-my-fcr4D_rZXr3huzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"泰式柠檬鲈鱼","price":50,"img_url":"https://qcloud.dpfile.com/pc/skzPU9Jw8Xb-Ptkeg9EatdjYhW9ggnOGkC7S_545tx4JBPuxaw_ytQFAmeRggNhOuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/YPjegFLXNehZDeoMLt2Ac46mqpfHc6iMEcFWkkxqAA02w1aQSuHVml6zJHAes4eqjoJrvItByyS4HHaWdXyO_I7F0UeCRQYMHlogzbt7GHgNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"}

key4 = 'restaurant_wildfire pizzabar'
value4 = {"restaurant":"Wildfire Pizzabar","style":"western","tel":"+852 - 28495123","address":"山顶山顶道128号凌霄阁1楼2号铺","popular_menu":[{"dish":"波士顿龙虾尾焰角博饼","price":200,"img_url":"https://p0.meituan.net/overseas/0e1e5294e93b4cf1ae9d5a0bc3df03ff.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"},{"dish":"煨牛肉阔面","price":99,"img_url":"https://qcloud.dpfile.com/pc/D3Asi_s3l1Tug-L1iQnMDT0eigsZTDiXX56rvvZyY9vAxzdekhTcSA766YY2lur4uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"t骨牛排","price":90,"img_url":"https://qcloud.dpfile.com/pc/veLCCLzDPfZuI6_M_HU2IKkCAilojAER38UB9o-tPs5GsqaxLpSj774Rz44X9YJ10scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}],"environment":"https://p1.meituan.net/overseas/29a8c990f1c42ee9ad36954716d364f7.jpg"}

key5 = 'restaurant_大满喜日本料理'
value5 = {"restaurant":"大满喜日本料理","style":"japan","tel":"+852-36222162","address":"旺角弥敦道601号创兴广场8楼","popular_menu":[{"dish":"烤鳗鱼","price":43,"img_url":"https://qcloud.dpfile.com/pc/u5q57E76qgbZ7azs_UyJLvznDGHZlOqHN6E-8sORsYZKRdhXVHTmUsh3r_s-B_b-uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"三文鱼","price":66,"img_url":"https://qcloud.dpfile.com/pc/4WX_KrA_pivHx-2CbQWzswdF4VUIooOQ2lYtP-I541Q82HXOkm9uYIzYufdUZZDf0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"},{"dish":"海胆卷","price":33,"img_url":"https://qcloud.dpfile.com/pc/eBGZFgi6Rst9ENNH8cOz4MK4pEFdMtianM9TwUJgPPFxfOasxB0tol5BWceNMBJQuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/4vSlED1TpHVvPSLu7afo7znOXraWJc9jGk5LDy3z_BAMPxq7ME1_3c5Ct3iu89Fh0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

key6 = 'restaurant_北京老家'
value6 = {"restaurant":"北京老家","style":"china","tel":"+852-34622518","address":"尖沙咀加拿分道25-31號國際商業信貸銀行大廈8樓","popular_menu":[{"dish":"北京烤鸭","price":108,"img_url":"https://qcloud.dpfile.com/pc/3B20FQHGmaYhn_GCZgUF5qi1S8bGN4eJtU4_K_gIwZQjB9PnpfRGfwdf-EZnI0PtuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"小笼包","price":55,"img_url":"https://qcloud.dpfile.com/pc/3EGT4X68aWSAPxWj12C9kTKjuGtilg2-wqGYQlEwS-Ox-vxa7-jRdMqvX-dxFsWzuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"水煮鱼片","price":99,"img_url":"https://qcloud.dpfile.com/pc/lK6GRJcp-aUwAagzs_3Bvrkg1nb08q7wh93nrGyRfp-ZRJPppoEcDwiwGK5id0MuuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/-JQCou6onctKiVMd1-gogg00AFBfV9yvGx4qMZ6pOogN_PWZwTQ-oij0Ex-X7tJF0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

key7 = 'restaurant_南瀛水产'
value7 = {"restaurant":"南瀛水产","style":"japan","tel":"+852-23688028","address":"香港尖沙咀金马伦道5号太兴广场5楼","popular_menu":[{"dish":"刺身","price":99,"img_url":"https://qcloud.dpfile.com/pc/3EWQrzL_-I8DNJKiiM3yizza_C0RT22j78Onuw-oUx8jB9PnpfRGfwdf-EZnI0PtuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"甜虾海胆三文鱼寿司卷","price":68,"img_url":"https://qcloud.dpfile.com/pc/hu-h7vsiFjT7_Pizob_cWumMZut4StF9ncu8ljtvVxZ5tn8kypBcqNwHnjg96EvTuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"杂锦天妇罗","price":62,"img_url":"https://qcloud.dpfile.com/pc/ma6RtN7F5kTh3OrBCgp3fSClK5H0APxmN7b4G2S2RZIrby3SL8JiuqxTxq0ya0ULuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/3MRBLFzoRPJz8W4VnntUZO-tNBxIOac_SQbu8V2FMO8AiX-0U4l8HVcLNTIkRJTf0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

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






