# -*- coding : utf-8 -*-

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests as req

usr = '01089338561'
pw = '!whdals401!'

driver = webdriver.Chrome('chromedriver')
driver.get('http://www.facebook.org')
assert "Facebook" in driver.title
elem = driver.find_element_by_id('email')
elem.send_keys(usr)
elem = driver.find_element_by_id('pass')
elem.send_keys(pw)
elem.send_keys(Keys.RETURN)

a = driver.find_element_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')
driver.get(a[0].get_attribute('href'))


