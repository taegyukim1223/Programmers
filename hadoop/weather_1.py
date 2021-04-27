import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp?type=t99&mode=0&stn=0&reg=100&auto_man=m&tm=2021.04.27.17:00&dtm=-1'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

table = soup.find("table", attrs = {"class" : "table_develop3"})
# print(table)

table1 = table.find_all("tr")
print(table1)

# data1 = []
# for i in table1 :
#     point = table1[0].text
#     tem = table1[5].text
#     humi = table1[9].text
#     data1.append([point, tem, humi])

# print(data1)

# print(table1)
# soup_local = soup1.find_all("a").get_text()
# soup_locals = soup1.a.get_text()
# for soup_local in soup_locals :
#     print(soup_local)