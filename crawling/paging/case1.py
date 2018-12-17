import urllib.request
from bs4 import BeautifulSoup

list_paging = []

for x in range(0, 5):
    url = "http://sports.donga.com/Enter?p=" + str(x * 20 + 1) + "1&c=02"
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    for span in soup.find_all("span", "tit"):
        list_paging.append(span.get_text())

print(list_paging)
