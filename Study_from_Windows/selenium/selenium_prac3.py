from selenium import webdriver as wbd
from collections import Counter
from pprint import pprint
import time


driver = wbd.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div') # NOTE : 에스터리스크(*)는 태그 안에 내부요소가 추가적으로 있을때 사용
                                                            # NOTE : 실행할 때마다 웹페이지에서의 값이 div값이 변하는대로 갱신됨.

def analysis():
    colors = [btn.value_of_css_property('background-color') for btn in btns]

    result = Counter(colors)
    # pprint(result)

    # NOTE : value가 1인 것 탐색
    for k, v in result.items():
        if v == 1:
            ans = k
            break
    else:
        ans = None
        print('정답을 찾을 수 없습니다.')

    # NOTE : 정답 클릭
    #        1. colors에서 인덱스 값을 구함.
    #        2. 구한 인덱스 값으로 btns 인덱스에 접근, 클릭

    if ans:
        ind = colors.index(ans)
        btns[ind].click()
start = time.time()
while time.time() - start <= 60:
    analysis()