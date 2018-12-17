import urllib.request
from bs4 import BeautifulSoup

url = "https://pann.nate.com/talk/344083297"

soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

reply_contents = []

for reply in soup.find_all("div", "cmt_list"):
    for x in reply.find_all("dd", "usertxt"):
        for content in x.find_all("span"):
            reply_contents.append(content.get_text().strip("\n|\t"))

print(reply_contents)
