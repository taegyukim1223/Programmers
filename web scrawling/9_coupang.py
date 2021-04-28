import requests
import lxml
import re
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs = {'class' : re.compile("^search-product")})

# print(items[0].find("div", attrs = {'class' : 'name'}).get_text())
for item in items :
    
    # 광고제품 제외
    ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
    if ad_badge :
        # print("광고상품제외합니다.")
        continue

    name = item.find("div", attrs = {'class' : 'name'}).get_text()

    # 애플제품 제외
    if "Apple" in name :
        # print("애플제품입니다.")
        continue


    price = item.find("strong", attrs = {'class' : 'price-value'}).get_text()

    # 리뷰 200개이상 평점 4.5이상 되는 것만 조회
    score = item.find("em", attrs = {'class' : 'rating'})
    if score :
        score = score.get_text()
    else :
        score = "평점없음"
        # print("평점없는 제품입니다.")
        continue

    score_cnt = item.find("span", attrs = {'class' : 'rating-total-count'})
    if score :
        score_cnt = score_cnt.get_text()
        score_cnt = score_cnt[1:-1]
    else :
        score_cnt = "평점없음"
        # print("평점없는 제품입니다.")
        continue
    
    link = item.find("a", attrs = {'class' : 'search-product-link'})["href"]
    
    # f string으로 깔끔하게 출력하기, 문자열안에 변수 넣고 싶을 때 쓰자.
    if float(score) >= 4.5 and int(score_cnt) >= 100 : 
        print(f'이름 : {name}')
        print(f'가격 : {price}')
        print(f'평점 : {score} 평점수 : {score_cnt} ')
        print("https://www.coupang.com" + link)
        print("-" * 100)
        


