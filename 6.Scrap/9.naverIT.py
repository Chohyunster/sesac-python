from bs4 import BeautifulSoup
import requests

url = "https://news.naver.com/section/105"

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

# 헤드라인과 그 아래 일반 뉴스 제목/링크 뽑아오기

headline_list = soup.select('.sa_list')
print(headline_list)