from selenium import webdriver
from time import time

dri = webdriver.Chrome('chromedriver')
dri.get('http://zzzscore.com/color2/')
dri.implicitly_wait(200)

start = time()
while time() - start <= 60:
    btn = dri.find_element_by_class_name('main')
    btn.click()