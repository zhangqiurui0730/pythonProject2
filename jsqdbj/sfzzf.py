import requests
import  time
from project import configfilea
from jsqdbj import qdbjurla

def create():#查询始发中转费方案
    rescc = requests.post(qdbjurla.sfzzfurl, data=qdbjurla.param, headers=configfilea.headers)#查询到达操作费方案
    assert len(rescc.json()['rows'])>0
    print("查询成功")
if __name__ == '__main__':
    create()