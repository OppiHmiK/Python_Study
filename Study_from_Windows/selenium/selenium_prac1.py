from selenium.webdriver.common.keys import  Keys
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.youtube.com/')


# NOTE :검색어 창을 찾아 search 변수에 저장
#       xpath는 selenium에서 사용하는 경로방식
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('반원 코딩') # NOTE : 검색창에 '반원코딩'을 입력

time.sleep(1)
search.send_keys(Keys.ENTER) # NOTE : 엔터키를 누름