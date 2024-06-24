import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com"

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

#신문기사제목 및 링크 출력하기 

news_list = soup.select('.today_list > li')
# print(len(news_list)) --> 이렇게 해서 뉴스 개수 몇개인지 알아보고, 내가 원하는 돔 요소를 잘 가져왔는지 확인한다.

for news in news_list:
    # a_tag = news.select_one('a')
    # print(a_tag['title'])
    # print(a_tag['href'])
    # break
    div_tag = news.select_one('.title')
    print(div_tag.text.strip())

