import reqests
from project import configfile
from yunying import yundanParam

def create():
    rescc = requests.post(yundanParam.ludanurl,data=yundanParam.orderdata,headers=configfile.headers)
    ord = rescc.status_code
    print(ord)
    print(rescc.json())

if __name__ == '__main__':
    create()
