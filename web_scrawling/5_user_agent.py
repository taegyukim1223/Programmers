import requests
res = requests.get("http://nadocoding.tistory.com")
# res.raise_for_status()
#res가 오류 뜨면 프로그램 종료
print(res.text)
with open("nadocoding.html", "w", encoding="utf8") as f :
    f.write(res.text)
# mygoogle.html 파일 만들었다. res.text로


