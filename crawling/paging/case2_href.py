import urllib.request
from bs4 import BeautifulSoup

list_href = []

url = "http://sports.donga.com/Enter"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

for i in range(0 ,23):
    list_href.append(soup.find_all("span", "tit")[i].find("a")["href"])

print(list_href)
