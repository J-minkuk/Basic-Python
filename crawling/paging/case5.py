import urllib.request
from bs4 import BeautifulSoup

url = "https://news.nate.com/recent?mid=n0100"

req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

for a in soup.find_all("div", "mlt01"):
    print("https:" + a.find("a")["href"])
