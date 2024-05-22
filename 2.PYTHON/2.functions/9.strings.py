s = 'Hello World sesac'
l = 'hello'
u = "HELLO"
print(s)

print(s.lower()) #이것은 객체(class) 안에 있는 함수를 호출하는 거다... str=객체.. cf.빌트인함수 : e.g. len
print(s.upper()) #<--많이 사용됨
print(s.islower()) #<--많이 사용됨
print(s.isupper())
print(l.islower())
print(u.isupper())
print(s.capitalize())
print(s.title())

s2 = "hello world  ! !  "
print(s2.strip()) #<--매우 많이 사용됨. 단, 중간 말고 앞뒤의 공백만 제거함.

s3 = "apple, banana,cherry, orange"
print(s3.split()) #<--매우 많이 사용됨. 기본값은 스페이스를 기준으로 잘라줌.
print(s3.split(','))

s3_list = s3.split(',')
print(s3_list)

s3_clean_list = []
for fruit in s3_list:
    clean_name = fruit.strip()
    s3_clean_list.append(clean_name)
    #.s3_cleant_list.append(fruit.strip()): 위에 쓴 거를 줄여서 쓰면 이렇게 된다.
    
print(s3_clean_list)












