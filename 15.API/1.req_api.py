import requests

#외부에 요청: "니가 가지고 있는 정보 좀 주시오"

#특정 사용자 정보 조회하기
user_id = 1
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

response = requests.get(url)

post_data = response.json()
for comment in post_data:
    # print(comment)
    print(comment['title'])

print('-'*20)

#2.게시글 ID를 기준으로, 댓글 가져오기
post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

reponse = requests.get(url)
post_data = response.json()
for comment in post_data:
    print(comment['email'])


#이 파일을 좀더 간편하게 만든 것이 2번 파일과, my_jsonplaceholder파일.

