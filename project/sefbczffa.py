import requests
import threading
import time
import random
from project import configfile
def create():#时间戳
    configfile.headers['userId'] = configfile.userId
    rescc = requests.post(configfile.ddczffa, data=configfile.cparams, headers=configfile.headers)#查询到达操作费方案
    print(rescc.json())
    assert len(rescc.json()['rows'])>0
    print("查询成功")
if __name__ == '__main__':
    create()