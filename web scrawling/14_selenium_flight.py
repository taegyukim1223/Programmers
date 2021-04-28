from selenium import webdriver as wd

#로딩 기다리는 코드
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = wd.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()
# 이번달 27일 28일 선택 -> 텍스트로 찾기

browser.find_elements_by_link_text("30")[0].click()
browser.find_elements_by_link_text("2")[1].click()

# 제주도 선택 x path 
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div').click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# x패스가 열릴때 까지 대기, 10초 최대 대기
try :  
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)

finally:
    browser.quit()

#첫번쨰결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.txt)