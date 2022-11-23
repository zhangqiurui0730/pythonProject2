# encoding = utf-8

def str_change_json(string: str):
    """
    form 表单参数转 json
    :param string: form表单直接复制的参数
    :return: json result
    """
    data_list = [i.strip() for i in string.split('\n') if i != '' and i.strip() != '']
    result = {}
    for i in data_list:
        # 如果参数为list 则特殊处理
        if not i.endswith(']'):
            items = [j.strip() for j in i.split(":")]
            result[items[0]] = items[1]
        else:
            items = [k.strip() for k in i.split(": ")]
            result[items[0]] = items[1]

    return str(result).replace("'", '"').replace('"[', "[").replace(']"', "]")


data = '''amountBxfRate: 
amountXf: 
amountCcf: 
amountBzfPt: 10301
itemName: 
savePrint: 
amountBzf: 
expectedArriveTime: 
forAmountOts6: true
forFreeItem: 0
forAmountOts7: true
modeOfSettlement: 10301
amountDff: 
unitPrice: 
amountGjFwf: 
amountOts15Pt: 10301
amountZzf: 
consignee: 张三
consigneeAddr: 河南省郑州市管城回族区紫辰路
standardFreight: 10.32
amountOts11Pt: 10301
amountOts2Pt: 10301
standardShf: 
forReceive: true
shipperName: 
amountOts1: 0.05
truckTypeId: 12325
amountOts2: 1
amountOts3: 
amountOts6Pt: 10301
amountOts4: 
amountOts5: 
saveShipper: 
amountJhfPt: 10301
forUpstairs: 
inputMode: 15601
carrierCode: 
amountShfPt: 10301
shipperTel: 
orderSales: 丈子头网点
billDeptId: 001881
amountReturn: 
amountTransfer: 
yjPayeeMobile: 
contractNo: 
save: 
hdPickType: 
amountOts6: 50
amountOts7: 50
orderRefNo: 
amountOts8: 
shipperAddr: 
amountOts9: 
amountTransferPt: 10301
discountFreight: 10.32
hdCount: 
amountOts12Pt: 10301
amountOts3Pt: 10301
amountTfyj: 
amountOts7Pt: 10301
itemDesc: 
amountCcfPt: 10301
forHd: 0
amountThf: 
serviceProduct: CP003
hdType: 
amountYjPt: 11102
consigneeContractNo: 
itemPrice: 
amountFreight: 89.00
amountDffPt: 11101
serviceType: 10101
itemQty: 
shipper: 张三
amountBelow: 
discDeptId: 000065
amountCod: 1000
amountTf: 89.00
shipperMobile: 111111111111
consigneeMobile: 111111111111
itemPkg: 
amountCodService: 10201
bankAccount: 
amountOts13Pt: 10301
hdMode: 10503
orderNo: 
amountOts10: 
amountOts12: 
itemKgs: 
amountOts11: 
amountOts14: 
amountOts13: 
amountOts15: 
amountOts4Pt: 10301
amountOts8Pt: 10301
yjPayeeAccount: 
paidType: 
businessAttributes: 55702
amountDffQf: 
totalAmount: 
totalIncome: 200
amountReturnPt: 10301
amountKf: 
amountShf: 
orderDate: 1621579859995
forDelivery: 0
totalCost: 121.32
amountGjFwfPt: 
isAutoNo: 1
itemType: 
orderRemark: 
bankName: 
amountCodStuff: 3
consigneeName: 
gis: 
orderUrl: 
amountBelowPt: 10301
amountBxf: 
amountOts1Pt: 10301
destDeptName: 
contractName: 
amountOts14Pt: 10301
customerRemark: 
amountAlloc3: 
amountXfyj: 
amountOts10Pt: 10301
amountCodeFrtPt: 
consigneeTel: 
forPrintDff: 
amountAlloc1: 
amountAlloc2: 
amountCodFreight: 
deliveryType: 
shipperIdcard: 
amountQf: 
amountDffXf: 
amountOts5Pt: 10301
amountOts9Pt: 10301
amountYj: 
discArea: 410000,410100,410104
unitPriceType: 
itemCbm: 
amountJhf: 10
businessType: 29101
amountHdf: 
isSendMessage: 0
yjPayee: 
destDeptId: 
discProvince: 410000
discCity: 410100
discDistrict: 410104
isRoute: true
consigneeXLong: 113.71571965407709
consigneeYLati: 34.698239853883464
itemJson: [{"itemDesc":"DF-41","itemType":"其他类","itemTypeId":"13A4488B265A4940AEA2638DB49F163D","itemPkg":"10907","itemQty":1,"itemKgs":1,"itemCbm":0.1,"itemPrice":21}]
amountBelowXf: 
amountShfXf: 
amountJhfXf: 
amountTransferXf: 
amountBzfXf: 
amountOts1Xf: 
amountOts2Xf: 
amountOts3Xf: 
amountOts4Xf: 
amountOts5Xf: 
amountOts6Xf: 
amountOts7Xf: 
amountOts8Xf: 
amountOts9Xf: 
amountOts10Xf: 
amountOts11Xf: 
amountOts12Xf: 
amountOts13Xf: 
amountOts14Xf: 
amountOts15Xf: 
amountCcfXf: 
amountTaxesXf: 
totalAmountXf: 
totalAmountCb: 121.32
amountBqf: 
cost: 2.69
amountTcf: 
shipperXLong: 
shipperYLati: 
isBusinessDepartment: true
price: 10.32
totalAmountMdcb: 2.69
durationText: 
standardDeliveryRange: 
amountBqfPt: 10301
amountTaxesPt: 10301
paidMode: 26001
orderType: 11301
orderRoute: [{"deptName":"丈子头网点","companyId":"0046","isVoyage":"0","isAllowSkip":"0","deptId":"001881","deptType":"12001","profitRate":0,"deptNo":"YLFNF-001","isAutoMove":"0","routeShortNum":1},{"deptName":"山西省内分拨","companyId":"0046","isVoyage":"0","isAllowSkip":"0","deptId":"002060","deptType":"12003","profitRate":0,"deptNo":"SXSNFB-001","isAutoMove":"0","routeShortNum":2},{"deptName":"山西省际分拨中心","companyId":"0046","isVoyage":"0","isAllowSkip":"0","deptId":"000006","deptType":"12003","profitRate":0,"deptNo":"SJFB-001","isAutoMove":"0","routeShortNum":3},{"deptName":"郑州分拨中心","companyId":"0045","isVoyage":"0","isAllowSkip":"0","deptId":"001877","deptType":"12003","profitRate":0,"deptNo":"001","isAutoMove":"0","routeShortNum":4},{"deptName":"四十部","companyId":"0045","isVoyage":"0","isAllowSkip":"0","deptId":"000065","deptType":"12001","profitRate":0,"deptNo":"TDFLC-575","isAutoMove":"0","routeShortNum":5}]
terminal: PC
module: orderHdrAddNew'''
if __name__ == '__main__':
    print(str_change_json(data))
