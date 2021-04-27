import urllib.request
url = "http://www.naver.com"
html = urllib.request.urlopen(url)
html.read()