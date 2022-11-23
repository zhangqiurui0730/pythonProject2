import requests
import ludana
import time
from project import configfilea
from yunying import yundanParam
from urllib.parse import urlencode
import random

url='http://8.136.132.172:8090/tms-ylpt-test-a/token/login'
daohuourl='http://8.136.132.172:8090/tms-ylpt-test-a/arriveManage/arrivedSign'

#生成token
params={
    "username":"四十部",
    "password":"123456",
    "terminal":"PC",
    "module":"login"
}
rest=requests.post(url,data=params,headers=yundanParam.headers1)
token=rest.json()['rows']['token']
#生成头信息
headers3={
    "userId": yundanParam.userId,
    "Accept": "application/json, text/plain, */*",
    "module": "departureTransScheme",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "8.136.132.172:8090",
    "Authorization":token,
    "terminal": "PC"
}

#app到货入库方法
def daohuo():
    json1=urlencode(yundanParam.orderdata3)
    rescc = requests.post(daohuourl,data=json1,headers=headers3)
    ord = rescc.status_code
    print(ord)

#app客户签收
def qianshou():


#创建运单并且到货入库
if __name__ == '__main__':
    dhorder_no=ludana.create_order()
    print(dhorder_no)
    yundanParam.orderdata3["transOrderDtlListJson"]=[{"detailType": "13701", "orderBarNo": dhorder_no}]
    daohuo()