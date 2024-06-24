from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#데이터를 대량으로 다루기 위한 라이브러리 : pandas
import pandas as pd

#크롬 실행시에 필요한 옵션들 추가하기
chrome_options = Options()
chrome_options.add_argument("--headless") #브라우저는 숨겨서 실행

#크롬드라이버 서비스 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

#웹페이지 열기
base_url = "http://www.cine21.com"
ranking_url = base_url + '/rank/boxoffice/domestic'
driver.get(ranking_url)

#페이지소스 가져오기
page_source = driver.page_source

#BS4로 전달해서 파싱하기
soup = BeautifulSoup(page_source, 'html.parser')

#영화목록 담기위한 변수
data = []


boxoffice_list_content = soup.find('div', id='boxoffice_list_content')

#영화 순위, 영화 제목, 관객수 출력
boxoffice_li_list = boxoffice_list_content.find_all('li', class_='boxoffice_li')
for boxoffice_li in boxoffice_li_list:
    mov_name_div = boxoffice_li.find('div', class_='mov_name')
    people_num_div = boxoffice_li.find('div', class_='people_num')
    rank_num_span = boxoffice_li.find('span', class_='grade')

    mov_link = boxoffice_li.find('a')['href']

    rank = rank_num_span.get_text(strip=True)
    mov_name = mov_name_div.get_text(strip=True)
    people_num = people_num_div.get_text(strip=True).replace('관객수|', '')

    # print(f'순위: {rank}, 제목: {mov_name}, 관객수: {people_num}')
    data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})
    print(data)

df = pd.DataFrame(data)
#엑셀로 저장하기
df.to_excel('boxoffice_rankings.xlsx')


#브라우저 닫기
driver.quit