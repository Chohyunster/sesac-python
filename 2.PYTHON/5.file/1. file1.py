# 파일 입출력을 할 때 사용하는 함수 : open
# 읽기: "r"
# 쓰기모드: "w"
# 더할때: "a" (append의 약자)

#file = open('example.txt', w) 라고 생각하면 됨. 좀 특이한 문법임: with ~ as ~
# with open('example.txt', 'a') as file:
#     file.write("Hello World World\n")

# print('텍스트 파일 기록을 완료하였습니다.')

#. 다른 코드
with open('example.txt', 'r') as file:
    text = file.read()
    print(text)

with open('example.txt', 'r') as file: #파일에 접근하기 위한 포인터(파일 이스트립터)
    for line in file:
        print(line, end ='')

# 다행히 위와 같은 모듈이 있다. 파이썬 기본 라이브러리에 속함.