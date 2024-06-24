#pip install selenium
#내 크롬 브라우저 버전을 확인하고, 그거에 맞는 크롬 드라이버를 선택한다. 
# 크롬 버전 올라갈 때마다 설치해줘야 함. -> 그래서 이 파일을 관리해주는 라이브러리가 또 있음 => 21번 파일로!

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#크롬드라이버 서비스 생성
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

#크롬 드라이버 초기화

#웹페이지 열기
driver.get('https://www.naver.com')

#브라우저 닫기
driver.quit