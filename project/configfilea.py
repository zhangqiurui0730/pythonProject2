import time
import requests

now_time = '%.0f' % (time.time() * 1000)
t1 = now_time[:5]
t2 = now_time[-4:]
t3 = now_time[5:-4]
userId = t1 + t2 + t3
headers1={
    "userId": '1617148888357',
    "Accept": "application/json, text/plain, */*",
    "module": "login",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "8.136.132.172:8090",
    "terminal": "PC"
}
url='http://8.136.132.172:8090/tms-ylpt-test-a/token/login'
params={
    "username":"丈子头网点",
    "password":"123456",
    "terminal":"PC",
    "module":"login"
}
res=requests.post(url,data=params,headers=headers1)
token=res.json()['rows']['token']


headers={
    "userId": userId,
    "Accept": "application/json, text/plain, */*",
    "module": "departureTransScheme",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "8.136.132.172:8090",
    "Authorization":token,
    "terminal": "PC"
}

curl='http://8.136.132.172:8090/tms-ylpt-test-a/voyage/addVoyageHdr'#创建车次
surl='http://8.136.132.172:8090/tms-ylpt-test-a/voyage/selectOrderAndPackageForLoad'#查询运单
purl='http://8.136.132.172:8090/tms-ylpt-test-a/voyage/loadOrderToVoyage'#推送运单
furl='http://8.136.132.172:8090/tms-ylpt-test-a/voyage/confirmVoyage'#发车出库
scurl='http://8.136.132.172:8090/tms-ylpt-test-a/arriveManage/selectVoyageHdrList'#查询车次
dcurl='http://8.136.132.172:8090/tms-ylpt-test-a/arriveManage/updateVoyageArrivedByVoyageId'#到车确认
qsurl='http://8.136.132.172:8090/tms-ylpt-test-a/arriveManage/arrivedSign'#到货确认


ddczffa='http://8.136.132.172:8090/tms-ylpt-test-a/operatorScheme/selectOperatorSchemeList'

cparams={
    "loadPlaceId": "012318",
    "discPlaceId": "001880",
    "estimatedTimeOfArrival": now_time,
    "voyageMode": "23202",
    "orderDate": "NaN",
    "transportType": "19403",
    "isActive": "true",
    "terminal": "PC",
    "module": "transportOutAdd"
}

pparams={
    "voyageId": "823888662180659200",
    "loadType": "1",
    "terminal": "PC",
    "module": "transportOutAdd"
}
fparams={
    "voyageId": "825018906560827392",
    "truckCode": "豫A34567",
    "driverId1": "820330633850527744",
    "driverName1": "张天",
    "driverMobile1": "16616616616",
    "estimatedTimeOfArrival": now_time,
    "totalOrder": "1",
    "totalQty": "1",
    "totalCbm": "1",
    "totalKgs": "1",
    "amountZcx": "0",
    "amountLdx": "0",
    "unloadType": "60402",
    "isForceLingDanXie": "false",
    "affixName": [],
    "terminal": "PC",
    "module": "transportOutAdd"
}

scparams={
    "voyageStatus": "11403",
    "transportTimeBegin": "1616774400000",
    "transportTimeEnd": now_time,
    "pageNum": "1",
    "pageSize": "100",
    "terminal": "PC",
    "module": "voyageHdr"
}
dcparams={
    "voyageIds":	"825394168221683712",
    "terminal":	"PC",
    "module":	"voyageHdr"
}

qsparams={
"voyageId": "825045353870032896",
"voyageDtlListJson": [{"packageId":"","orderId":"825043121918210048","detailType":"13701"}],
"transOrderDtlListJson": [],
"terminal": "PC",
"module": "signArrivalGoods"
}