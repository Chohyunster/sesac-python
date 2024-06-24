from bs4 import BeautifulSoup
import requests

#웹 페이지에 get 요청 보내기
url = "http://www.cine21.com/rank/boxoffice/domestic"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

boxoffice_list_content = soup.select('#boxoffice_list_content')
print(boxoffice_list_content)

#답: JS는 크롬이 실행해주는데, 그게 안돼서 scrap이 안된다.