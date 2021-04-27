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
    name = item.find("div", attrs = {'class' : 'name'}).get_text()
    price = item.find("strong", attrs = {'class' : 'price-value'}).get_text()
    score = item.find("em", attrs = {'class' : 'rating'})
    if score :
        score = score.get_text()
    else :
        score = "평점없음"
    score_cnt = item.find("span", attrs = {'class' : 'rating-total-count'})
    if score :
        score_cnt = score_cnt.get_text()
    else :
        score_cnt = "평점없음"
    print(name, price, score, score_cnt)
