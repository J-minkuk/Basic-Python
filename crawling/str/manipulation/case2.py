import urllib.request
from bs4 import BeautifulSoup

url = "http://www.newsis.com/eco/list/?cid=10400&scid=10404"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

for div in soup.find_all("div", "lst_p6 mgt21"):
    for strong in div.find_all("strong", "title"):
        flag_index = strong.get_text().find("…")

        if flag_index != -1:
            print(strong.get_text()[0:flag_index])
        else:
            print(strong.get_text())
