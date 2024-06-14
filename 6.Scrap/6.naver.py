import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com"

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

#신문기사제목 및 링크 출력하기 

news_list = soup.select('.today_list > li')
# print(len(news_list)) --> 이렇게 해서 뉴스 몇개인지 알아본다.

for new in news_list:
    a_tag = new.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])
    break
