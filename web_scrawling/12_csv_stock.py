import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
f = open('stock.csv', 'w', encoding="utf-8", newline="")
column = "순위 종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE 토론방"
column = column.split()
csv.writer(f).writerow(column)

for page in range(1, 5) :
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_table = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")
        
    for row in data_table :
        columns = row.find_all("td")
        
        if len(columns) > 1 :
            data = [column.get_text().strip() for column in columns]
            csv.writer(f).writerow(data)

        
        
    # writer.write

    