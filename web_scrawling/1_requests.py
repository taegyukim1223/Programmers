import requests
res = requests.get("https://google.com")
res.raise_for_status()
#res가 오류 뜨면 프로그램 종료
print(res.text)
with open("mygoogle.html", "w", encoding="utf8") as f :
    f.write(res.text)
# mygoogle.html 파일 만들었다. res.text로

