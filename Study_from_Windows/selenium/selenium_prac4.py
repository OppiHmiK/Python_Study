from selenium import webdriver
from time import time

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

start = time()
while time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name('main')
        btn.click()
    except:
        pass