from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://www.baidu.com')
time.sleep(1)
title = driver.title
print(title)
driver.close()
