#<<<미션: 모든 페이지 영화 목록 다 가져오기>>>
    #1. 2페이지로 이동한다
    #2. 2페이지의 내용을 다시 다 출력한다.
    #3. 어? 복붙했네.. 함수를 만든다.
    #4. 함수에 저 페이지 번호를 인자값으로 준다.
    #5. 1~10페이지까지 모든 내용 다 가져온다.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup => selenium 쓸거라 지우기
#bs4를 통해서 우리가 하는건? => 이 함수를 통해서 원하는 DOM을 찾아오는 것. -> 이 기능은 selenium에도 있다:
#: find_element(By.NAME)
#  find_element(By....)
import time

import cine_database as my_db

#db 초기화
conn, cur = my_db.init_db()

#크롬 실행시에 필요한 옵션들 추가하기
chrome_options = Options()
# chrome_options.add_argument("--headless") #브라우저는 숨겨서 실행

#크롬드라이버 서비스 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 

#페이지 대기를 위한 웨이터 생성 : 내가 시킨 일에 대해서 최대 10초까지 기다려라
wait = WebDriverWait(driver, 10)

#웹페이지 열기
base_url = "http://www.cine21.com"
ranking_url = base_url + '/rank/boxoffice/domestic'
driver.get(ranking_url)


#영화목록 담기위한 변수
data = []

def get_movie_list():
    #영화 순위, 영화 제목, 관객수 출력
    boxoffice_list_content = driver.find_element(By.ID, 'boxoffice_list_content')
    boxoffice_li_list = boxoffice_list_content.find_elements(By.CSS_SELECTOR, 'li.boxoffice_li')
    
    for boxoffice_li in boxoffice_li_list:
        mov_name_div = boxoffice_li.find_element(By.CSS_SELECTOR, 'div.mov_name')
        people_num_div = boxoffice_li.find_element(By.CSS_SELECTOR, 'div.people_num')
        rank_num_span = boxoffice_li.find_element(By.CSS_SELECTOR, 'span.grade')

        # mov_link = boxoffice_li.find_element('a')['href']
        a_link = boxoffice_li.find_element(By.TAG_NAME, 'a')
        mov_link = base_url + a_link.get_attribute('href')

        rank = rank_num_span.text.strip()
        mov_name = mov_name_div.text.strip()
        people_num = people_num_div.text.strip().replace('관객수|', '')

        data.append({'순위': rank, '영화제목': mov_name, '관객수': people_num, '웹사이트정보': mov_link})
    
        my_db.save_to_db(conn, cur, rank, mov_name, people_num, mov_link)
    
    #첫페이지 부르기
    get_movie_list()

    #잠시 기다리기 5초간 대기
    #time.sleep(5)

    #2번째 페이지 가져오기     
    for page in range(2, 10):
        print(f'현재 {page}를 분석중입니다.')

        #페이지 목록 div가 뜰 때까지 기다린다.
        #page_tags = driver.find_elements(By.CSS_SELECTOR, "div.page a") => 이거 대신에,
        page_tags = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.page a')))
        page_tags[page].click()

        #time.sleep(5)
        #혹시 모르니 클릭한 이후에 내가 원하는 내용이 떴는지 확인
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#boxoffice_list_content li.boxoffice_li')))
        time.sleep(2) #이걸 대체할만한 요소를 찾으면 더 좋음. b/c 위 div는 페이지 넘어가기 전 전 페이지에도 있는 것이므로,, 정확하게 하려면 각 페이지의 고유한 것을 넣어줘야 맞음.

        get_movie_list()

print(data)

print('-' * 50)

my_db.query_movie(cur)

#연결 종료
my_db.close_db(conn)

#브라우저 닫기
driver.quit()

# ==================================
# 미션2. 가져온 내용 우리 DB에 넣기
# 1. 디비 테이블 생성한다. (스키마 설계하기)
# 2. 위에 리스트에 있는 내용을 DB에 삽입한다. (SQL 쿼리문...)