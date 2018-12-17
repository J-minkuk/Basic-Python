import urllib.request
from bs4 import BeautifulSoup

url = "http://www.kyeonggi.com/?mod=news&act=articleList&view_type=S&sc_code=1439458030"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

list_title = []
list_content = []

for news_title in soup.find_all("div", "list-titles"):
    list_title.append(news_title.get_text())

for news_content in soup.find_all("p", "list-summary"):
    list_content.append(news_content.get_text().strip("\n|\t"))

print(list_title)
print(list_content)
