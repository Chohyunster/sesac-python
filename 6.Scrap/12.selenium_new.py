#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#크롬 실행시에 필요한 옵션들 추가하기
chrome_options = Options()
# chrome_options.add_argument("--headless") #브라우저는 숨겨서 실행
chrome_options.add_argument("--window-size=1128,2544") #저장되는 스샷의 해상도 지정

#크롬드라이버 서비스 생성
# service = Service(executable_path="./chromedriver.exe")  #이건 로컬에 있는 파일을 쓰는 명령어
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
#이건 크롬드라이버 알아서 가져와서 깔아주는 것 ==> #이거 해주면 로컬의 chromedriver 지워도 됨.

#웹페이지 열기
driver.get('https://www.google.com')

#검색창에다 내가 원하는 글자 입력하기
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('python programming')

#엔터를 치든지 검색 버튼을 가져와서 그걸 클릭을 하든지
# search_box.submit()
search_box.send_keys(Keys.RETURN)
#위 두줄은 결과적으로 같음.

time.sleep(5)

#결과 페이지를 스크린샷 뜨고 싶으면?
driver.save_screenshot('search_result_002.png')

#브라우저 닫기
driver.quit