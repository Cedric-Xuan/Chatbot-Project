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

value1 = {"restaurant":"泰式海南鸡","style":"thai","tel":"+852-24758813","address":"元朗西菁街9號富盛商場地下62號舖","latitude":"22.3311313000","longitude":"114.1599565300","popular_menu":[{"dish":"招牌泰式去骨海南鸡","price":208,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/qghnj.jpg"},{"dish":"酸辣去骨凤爪","price":62,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/fz.jpg"},{"dish":"泰式炒通菜","price":52,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tsctc.jpg"},{"dish":"明炉鱿鱼","price":135,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/mlyy.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tshnj_environment.jpg","video_img":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hnj_video_img.jpg","video":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hnj_video.mp4"}

value2 = {"restaurant":"Add Some Thai","style":"thai","tel":"+852 - 53741988","address":"观塘开源道62号骆驼漆大厦一期9楼D室","latitude":"22.3104054300","longitude":"114.2251102000","popular_menu":[{"dish":"AST小食拼盘","price":90,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/xspp.jpg"},{"dish":"泰式无骨海南鸡半只","price":180,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hnj.jpg"},{"dish":"椰汁芒果糯米饭","price":50,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nmf.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/Add%20Some%20Thai.jpg"}

value3 = {"restaurant":"金泰子泰国餐厅","style":"thai","tel":"+852-21726106","address":"太子柏树街17A号地铺","latitude":"22.2800580100","longitude":"114.1798754200","popular_menu":[{"dish":"海虾刺身","price":88,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hxcs.jpg"},{"dish":"泰式冬阴功","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tsdyg.jpg"},{"dish":"泰式柠檬鲈鱼","price":50,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nmly.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/jtz_environment.jpg"}

value4 = {"restaurant":"Wildfire Pizzabar","style":"western","tel":"+852 - 28495123","address":"山顶山顶道128号凌霄阁1楼2号铺","latitude":"22.3011600100","longitude":"114.1733996100","popular_menu":[{"dish":"波士顿龙虾尾焰角博饼","price":200,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/lx.jpg"},{"dish":"煨牛肉阔面","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/wnkm.jpg"},{"dish":"t骨牛排","price":90,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/tgnp.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/Wildfire%20Pizzabar.jpg"}

value5 = {"restaurant":"大满喜日本料理","style":"japan","tel":"+852-36222162","address":"旺角弥敦道601号创兴广场8楼","latitude":"22.3162084400","longitude":"114.1697771300","popular_menu":[{"dish":"烤鳗鱼","price":43,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/kmy.jpg"},{"dish":"三文鱼","price":66,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/swy.jpg"},{"dish":"海胆卷","price":33,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hdj.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/dmx_environment.jpg"}

value6 = {"restaurant":"北京老家","style":"china","tel":"+852-34622518","address":"尖沙咀加拿分道25-31號國際商業信貸銀行大廈8樓","latitude":"22.2981890100","longitude":"114.1729666100","popular_menu":[{"dish":"北京烤鸭","price":108,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/bjky.jpg"},{"dish":"小笼包","price":55,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/xlb.jpg"},{"dish":"水煮鱼片","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/syp.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/beijing_environment.jpg"}

value7 = {"restaurant":"南瀛水产","style":"japan","tel":"+852-23688028","address":"香港尖沙咀金马伦道5号太兴广场5楼","latitude":"22.2989970100","longitude":"114.1727866100","popular_menu":[{"dish":"刺身","price":99,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/cs.jpg"},{"dish":"甜虾海胆三文鱼寿司卷","price":68,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/hd.jpg"},{"dish":"杂锦天妇罗","price":62,"img_url":"https://markstone.oss-cn-shenzhen.aliyuncs.com/thl.jpg"}],"environment":"https://markstone.oss-cn-shenzhen.aliyuncs.com/nanyin_environment.jpg"}

value8 = {"restaurant":"登堂","style":"western","tel":"+852-21104103","address":"观塘兴业街4号The Wave2楼","latitude":"22.3096344300","longitude":"114.2244802000","popular_menu":[{"dish":"惠灵顿牛排","price":159,"img_url":"http://p0.meituan.net/overseas/e4247cd53fd2548708ccd1a7c8359b0e204798.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"},{"dish":"西班牙香蒜辣椒油煎虎虾","price":99,"img_url":"https://qcloud.dpfile.com/pc/icLDzMzvwVs1FZ3lgs7Sre1U9Brvf_fyzHI1McpOhOeJnJeEBTbmMVWW6d-43xhFuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"生蚝","price":68,"img_url":"https://qcloud.dpfile.com/pc/9MmnikF1h_YR063vp4WN6fhpEoWRfSFQVMQrlgVKQykxhtwBi2iuEK289FfWyH_euzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/9QOeYgsxMIMGErMspYev8LOBulhczryv43EnUlRDM_Osruo9aopB6dXyWeS-Hugl0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

value9 = {"restaurant":"BRICK LANE Deli","style":"western","latitude":"22.3813921500","longitude":"114.1886985500","tel":"+852-21110480","address":"沙田正街18号新城市广场一期1楼126号铺","popular_menu":[{"dish":"特色顶级美国牛肉汉堡","price":99,"img_url":"https://qcloud.dpfile.com/pc/E2dX_0suxMidDIyLk6mkFZFjpbYzzNNGL8V_hmkpViqgkucm2nCHBzF2FfLQxHNwjoJrvItByyS4HHaWdXyO_I7F0UeCRQYMHlogzbt7GHgNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"},{"dish":"英式炸鱼薯条","price":55,"img_url":"https://qcloud.dpfile.com/pc/wzhYGApgpGe7SV7MrMxZVePvUGYUVMnTrcC-ajLiYsZph2eIJA04NCRvoGqL4_opuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"巴马火腿班尼迪蛋","price":68,"img_url":"https://qcloud.dpfile.com/pc/fzEa6CR1IF6vnWTK0kNYvZsP2TgjXhV8Dt8OVqEenJG_KJSEnm9fiirk3YqIVqWpuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/Ml2e5lNR-qtZn_Tzjw8mtBN0Wg8XeWMvl1u0YdzI5fVyQtPkWzOF1DSEEqmqNrtl0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

value10 = {"restaurant":"爆丼屋","style":"japan","latitude":"22.3167733900","longitude":"114.1713139700","tel":"+852-23322918","address":"旺角豉油街50号","popular_menu":[{"dish":"爆盛慢烧牛肉丼","price":88,"img_url":"https://qcloud.dpfile.com/pc/TpGuc71skRU11Jb8OTQ28328p8cCbFMfs2ganoq3mVR3FBJMSLaCv8bY782i7uhfjoJrvItByyS4HHaWdXyO_I7F0UeCRQYMHlogzbt7GHgNNiIYVnHvzugZCuBITtvjski7YaLlHpkrQUr5euoQrg.jpg"},{"dish":"鳗鱼饭","price":108,"img_url":"https://qcloud.dpfile.com/pc/Gbp5AVUJ8Jf0KQ1eJtMWnvE5hiO5X_tbgXQj9QKXOGBxfOasxB0tol5BWceNMBJQuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"鹅肝","price":55,"img_url":"https://qcloud.dpfile.com/pc/yt03oa4eicLyEjD1d2Hx6YHIoQu0_q4V_YO4Q-war6soLz_lmsyLi2Jw3_LehKdUuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/4tdHNlN0W1mN0wlBBkz7Iu2vW6D9jmaG8wFvhi44iM_kUHq8eUzV5aRIVJoBZSY70scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

value11 = {"restaurant":"海底捞","style":"china","latitude":"22.3141363900","longitude":"114.1702169700","tel":"+852-39967799","address":"香港九龍旺角彌敦道555號九龍行二樓及三樓","popular_menu":[{"dish":"四宫格汤底","price":88,"img_url":"https://qcloud.dpfile.com/pc/RrijOEw9fYztcQ4P4qzrgWWUxMgXeQPctFxgIovqzpWDrHx3403SEg5dUJI6XFiduzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"猪脑","price":55,"img_url":"https://qcloud.dpfile.com/pc/9Jnj4glkxILjW1nJ3W18o1mcxMTZ09J_sILPmND3blQjLIQ8wWhdlE7XjNM2ZqP2uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"捞派毛肚","price":45,"img_url":"http://p1.meituan.net/overseas/06728f6cb8c4fa56ef3c7f2c39d66c6a.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"},{"dish":"日本和牛","price":250,"img_url":"http://p0.meituan.net/overseas/41dd6c9f0192ae3bfc4785e55906d287.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"},{"dish":"虾滑","price":250,"img_url":"https://qcloud.dpfile.com/pc/n9C2JtIWYMruo2L7ZYIU8N1aLTTCjo8DUiErg7bM1OgNdtNylZX1pkGuwDqPCzmhuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/ZtnlHItl7cXwfCE5EaoNgv1s8pLObTR8hAzSUDtKQRRc876hur2KbUBIJPkS4cE_0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}

value12 = {"restaurant":"湘轩","style":"china","latitude":"22.2798612500","longitude":"114.1805182400","tel":"+852-27880897","address":"铜锣湾骆克道405号","popular_menu":[{"dish":"双椒鱼头","price":108,"img_url":"https://qcloud.dpfile.com/pc/-4DJemFjHqZcMbOEGEngK-_PjTIS0KNFTDqT3NzNNP_KztIIMbR82ksDpLlCCe3buzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"土匪猪肝","price":66,"img_url":"https://qcloud.dpfile.com/pc/gGM14RE1bA7m7BLKhX84Yee7dn_Zi5oc5kwEWmrupoamunJDrBxAOxBGYM85OBh1uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"挂花米糕","price":43,"img_url":"https://qcloud.dpfile.com/pc/vRGxKYaRkiCwK9feTByvPKPTudMppuLn7xAjOR3UluE4jyZZRObLs5ym-WtN-3N1uzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"},{"dish":"香辣羊排","price":108,"img_url":"https://qcloud.dpfile.com/pc/11wLoyU_yV6HtnHOxqFqe_7NiuI72O8xGBH2f3R_U5Rph2eIJA04NCRvoGqL4_opuzFvxlbkWx5uwqY2qcjixFEuLYk00OmSS1IdNpm8K8sG4JN9RIm2mTKcbLtc2o2vfCF2ubeXzk49OsGrXt_KYDCngOyCwZK-s3fqawWswzk.jpg"}],"environment":"https://qcloud.dpfile.com/pc/dhAIfGo7up6fB-qQmUTQKtFgYE2V2pJKEQhVv27_YZn4gmFcC6w6IHbb6AvMuCY_0scohmss9LtJWg-k-u7I4UHdS9p3h7-h2wfpsWVfxX8nY08TQIxe-DkxF3-YDtNHvJLBPMnbGaim65JmQfWVIQ.jpg"}


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





tdb = myclient.admin

post = tdb.restaurant_list
# post.drop()

# post.insert_one(value1)
# post.insert_one(value2)
# post.insert_one(value3)
# post.insert_one(value4)
# post.insert_one(value5)
# post.insert_one(value6)
# post.insert_one(value7)
# post.insert_one(value8)
# post.insert_one(value9)
# post.insert_one(value10)
# post.insert_one(value11)
# post.insert_one(value12)


am = post.find({"style":"china"})
for a in am:
    print(a)






