from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'D:\chromedriver.exe')
driver.get('https://www.baidu.com/')


driver.find_element(By.ID, 'kw').send_keys('selenium')  #搜索框输入selenium
driver.find_element(By.ID, 'su').click()