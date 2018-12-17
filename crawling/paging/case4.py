import urllib.request
from bs4 import BeautifulSoup

list_href = []
list_content = []

url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

for href in soup.find_all("div", "mfn_inner"):
    list_href.append("https://news.sbs.co.kr" + href.find("a")["href"])

for i in range(0, len(list_href)):
    url = list_href[i]
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    list_content.append(soup.find("div", "text_area").get_text())

for i in list_content:
    if "한국" in i:
        print("OK")
    else:
        print("NOPE")
