import selenium
from selenium import webdriver

wd = webdriver.Chrome('D:\chromedriver.exe')

wd.get('http://47.97.51.50:8090/test/#/login')


name = wd.find_element(by='name',value='username')
pwd = wd.find_element(by='name',value='password')

name.send_keys('丈子头网点')
pwd.send_keys('123456')

#button = wd.find_element(by='class',value='el-button login_btn el-button--primary')
#print(button)
