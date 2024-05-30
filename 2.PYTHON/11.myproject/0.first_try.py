import random

surname = ["김", "박", "이", "송", "차", "길", "황", "최"]
middlename = ["가", "나", "다", "라", "마", "바", "사", "아", "자"]
lastname = ['차', "카", "타", "파", "하", "림", "현", "인", "미"]

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    return name

# for _ in range(10):
#     print(generate_name())

#==========================================================

def generate_gender():
    gender = ["Male", "Female"]
    gender = random.choice(gender)
    return gender

# for _ in range(10):
#     print(generate_gender())

#====생년월일 + 나이================

def generate_birthday():
    year = random.randint(1960, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)    
    return f'{year}-{month:02}-{day:02}'

generate_birthday()

# for _ in range(10):
#     print(generate_birthday())

#=======주소=========

def generate_address():
    cities = ["서울", "대전", "부산", "대구", "영월", "단양", "고양", "부천", "인천", "전주" "광주", "제주", "서귀포"]
    gus = ["송파구", "서대문구", "강남구", "동대문구", "강동구", "강서구", "은평구", "성북구", "종로구", "노원구"]
    return f'{random.choice(cities)}시 {random.choice(gus)}'

generate_address()

# for _ in range(10):
#     print(generate_address())

#==========나이===========
def generate_age():
    age = random.randint(15, 85)
    return age

generate_age()

#======사용자 데이터 생성============
userdata = [["Name", "Birthday", "Age", "Gender", "address"]]
for _ in range(10):
    name = generate_name()
    birthday = generate_birthday()
    age = generate_age()
    gender = generate_gender()
    address = generate_address()

    a_user = (name, birthday, age, gender, address)
    userdata.append(a_user)

print(userdata)

#====================================
#=========csv 파일로 저장=============
import csv

file = open('userlist.csv', 'w', encoding = 'utf-8')

writer = csv.writer(file)
writer.writerows(userdata)


