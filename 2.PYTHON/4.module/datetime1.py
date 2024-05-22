# https://docs.python.org/ko/3/library/datetime.html
import datetime

#모듈명.객체명.함수명
current_time = datetime.datetime.now()
print(current_time)

#내가원하는시간생성
my_time = datetime.datetime(2024, 1, 11, 10, 30, 0)
print(my_time)
print(type(my_time))
