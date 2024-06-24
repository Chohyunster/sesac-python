from bs4 import BeautifulSoup
import requests

url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

def print_articles(headline=True):
    if headline:
        # 헤드라인섹션 가져오기
        section_articles = soup.find_all('div', class_='section_article as_headline _TEMPLATE')
    else:
        section_articles = soup.select('div.section_article._TEMPLATE') # 웹에서 우클릭해서 copy selector가져와도 됨.

        for section_article in section_articles:
            sa_text_titles = section_article.find_all('a', class_='sa_text_title')  #class와 구분하기 위해 _ 붙인 문법임.
            for sa_text_title in sa_text_titles:
                print(sa_text_title.get_text().strip())