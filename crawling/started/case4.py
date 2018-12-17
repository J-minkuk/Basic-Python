import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=168058#"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

reviews_title = []

for review in soup.find_all("ul", "rvw_list_area"):
    for li in review.find_all("li"):
        for title in li.find_all("strong"):
            reviews_title.append(title.get_text())

print(reviews_title)
