
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://47.97.51.50:8090/test/#/login")
element = driver.find_element(By.__name__,'username')



