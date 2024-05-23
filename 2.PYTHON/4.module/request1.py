#. pip install requests

import requests
#->리퀘스트 모듈 안에 있는 함수를 사용할 수 있음.

#1. 웹 페이지에 있는 컨텐츠 가져올 수 있음. 
# response = requests.get("http://www.example.com")
response = requests.get("http://jsonplaceholder.typicode.com/users")
print("웹 페이지 내용: ")
print(response)
print(response.status_code)
print(response.text)


#text 결과물 받아온 것을 json이라는 데이터 타입으로 변환
data = response.json()
# print("JSON 데이터: ", data)
userId = data['userId']
title = data['title']
print(f"사용자ID: {userId}, 타이틀: {title}")

users = data
for user in users:
    print("이름: {}, ID: {}, 이메일: {}".format(user['name'], user['username'], user['email']))
