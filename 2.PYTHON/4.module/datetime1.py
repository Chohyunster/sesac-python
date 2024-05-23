# https://docs.python.org/ko/3/library/datetime.html
import datetime #.내 폴더에 있는 이름과 겹치지 않아야 한다. 겹치면 내 폴더에 있는 게 먼저이므로...

#모듈명.객체(=클래스)명.함수명 (class/object)

current_time = datetime.datetime.now()
print(current_time)

#내가원하는시간생성
my_time = datetime.datetime(2024, 1, 11, 10, 30, 0)
print(my_time)
print(type(my_time))
