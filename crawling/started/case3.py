import urllib.request
from bs4 import BeautifulSoup

url = "https://www.clien.net/service/group/community"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

list_title = []
list_nickname = []

for subject in soup.find_all("span", "subject_fixed"):
    list_title.append(subject.get_text())

for name in soup.find_all("span", "nickname"):
    str = name.get_text().strip("\n")
    if str != '':
        list_nickname.append(str)

print(list_title)
print(list_nickname)
