import requests
import threading
import time
import random
from project import configfile
from jsqdbj import qdbjurl
def create():#查询始发分拨操作费
    configfile.headers['userId'] = configfile.userId
    rescc = requests.post(qdbjurl.sffbczfur, data=configfile.cparams, headers=configfile.headers)
    assert len(rescc.json()['rows'])>0
    print("查询成功")
    print(rescc.json())
if __name__ == '__main__':
    create()