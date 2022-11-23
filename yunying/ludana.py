import request
import time
from project import configfilea
from yunying import yundanParam
from urllib.parse import urlencode
import random
import re




now_time = '%.0f' % (time.time() * 1000)
t1 = now_time[:5]
t2 = now_time[-4:]
t3 = now_time[5:-4]
userId = t1 + t2 + t3

url='http://47.97.51.50:8090/tms-ylpt-test-a/token/login'
urlsxf = 'http://47.97.51.50:8090/tms-ylpt-test-a/orderHdr/addOrderHdr'
params={
    "username":"丈子头网点",
    "password":"123456",
    "terminal":"PC",
    "module":"login"
}
headers1={
    "userId": userId,
    "Accept": "application/json, text/plain, */*",
    "module": "login",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "8.136.132.172:8090",
    "terminal": "PC"
}
rest=requests.post(url,data=params,headers=headers1)
token=rest.json()['rows']['token']
headers2={
    "userId": userId,
    "Accept": "application/json, text/plain, */*",
    "module": "departureTransScheme",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "47.97.51.50:8090",
    "Authorization":token,
    "terminal": "PC"
}
#创建运单
def create_order():
    json1=urlencode(yundanParam.orderdata2)
    rescc = requests.post(urlsxf,data=json1,headers=headers2)
    ord = rescc.status_code
    ord2 = rescc.json()
    order_no=ord2["msg"][12:23]
    print(ord)
    print(ord2)
    print(order_no)
    return order_no





if __name__ == '__main__':
    # 循环创建运单，容易超时需要优化
    # count = 1
    # while count <= 2:
    #     #生成随机电话号码,更新电话号码
    #     rad1 = random.randint(10000000000, 99999999999)
    #     rad2 = random.randint(10000000000, 99999999999)
    #     print(rad1)
    #     print(rad2)
    #     yundanParam.orderdata2["shipperMobile"] = rad1
    #     yundanParam.orderdata2["consigneeMobile"] = rad2
    #     #更新userid（目前没有解决token超时问题）
    #     now_time = '%.0f' % (time.time() * 1000)
    #     t1 = now_time[:5]
    #     t2 = now_time[-4:]
    #     t3 = now_time[5:-4]
    #     userId = t1 + t2 + t3
    #     print(userId)
    #     create()
    #     count = count + 1

    #
    rad1 = random.randint(10000000000, 99999999999)
    rad2 = random.randint(10000000000, 99999999999)
    yundanParam.orderdata2["shipperMobile"] = rad1
    yundanParam.orderdata2["consigneeMobile"] = rad2
    create_order()




