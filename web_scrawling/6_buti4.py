import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# html 문서를 lxml로 뷰리풀숲 객체로 변수에 저장

# print(soup.title)
# #타이틀의 엘리먼트를 전부다 가져옴

# print(soup.title.get_text())
#텍스트만 가져옴

# print(soup.a)
# 처음 발견되는 a 엘리먼트 정보 뿌려준다.

# print(soup.a.attrs)
#처음 발견되는 a 엘리먼트 속성정보를 반환

# print(soup.a["href"] )
# a element 의 href 속성 값 정보를 출력

# print(soup.find("a", attrs = {"class" : "Nbtn_upload"}))
# class = "Nbtn_pload"인 a element를 찾아줘

# print(soup.find(attrs = {"class" : "Nbtn_upload"}))
# class = "Nbtn_pload"인 어떤 element를 찾아줘

# print(soup.find("li", attrs = {"class" : "rank01"}))
rank1 = soup.find("li", attrs = {"class" : "rank01"})
# print(rank1.a) # 이중에서 a 랭크를 가진걸 또찾을수 있다.

# print(rank1.a.get_text())
# print(rank1.next_sibling) # 다음 정보 받기
# rank2 = rank1.next_sibling.next_sibling #넥스트 시블링을 두번쓰기 그렇다. rank1.find_next_sibling("li")
# rank3 = rank2.next_sibling.next_sibling

# print(rank3.a.get_text()) # 3위 정보가 텍스트만 나온다.

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent) # 태그간의 이동..

# rank2 = rank1.find_next_sibling("li")
# # print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.get_text())

# print(rank1.find_next_siblings("li")) # siblings를 통해 전부 가져오기.

webtoon = soup.find("a", text = "여신강림-154화")
조건 넣을 수 있다.
print(webtoon)