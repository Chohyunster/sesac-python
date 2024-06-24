import requests
from bs4 import BeautifulSoup

base_url = "https://news.naver.com/search.naver"

def naver_search(query):
    params = {'query': query}

    response = requests.get(base_url, params=params)  #.https://news.naver.com/search.naver?query=python%programming 이렇게 보내진다.
    return response.text

query = "파이썬 프로그래밍"
soup = naver_search(query)

print(soup)
