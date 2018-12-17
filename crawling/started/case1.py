import urllib.request
from bs4 import BeautifulSoup

url = "http://www.naver.com"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

realTimeKeywords = []

for text in soup.find_all("div", class_="ah_roll_area PM_CL_realtimeKeyword_rolling"):
    for keyword in text.find_all("span", class_="ah_k"):
        realTimeKeywords.append(keyword.get_text())

print(realTimeKeywords)
