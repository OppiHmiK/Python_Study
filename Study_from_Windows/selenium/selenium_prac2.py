from selenium import webdriver as wbd

driver = wbd.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50/?ts=1559581781852')
driver.implicitly_wait(300) # NOTE : time.sleep(3)과 동일

num = 1 # NOTE :  현재 찾아야할 숫자

def clickBtn():

    global num # NOTE : num이라는 변수를 함수 안에서도 사용할 수 있도록 전역변수로 선언
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:

        print(btn.text, end = '\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num += 1
            return

while num <= 50:
    clickBtn()