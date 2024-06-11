import random

def generate_address():
    cities = ["서울", "대전", "부산", "대구", "영월", "단양", "고양", "부천", "인천", "전주" "광주", "제주", "서귀포"]
    gus = ["송파구", "서대문구", "강남구", "동대문구", "강동구", "강서구", "은평구", "성북구", "종로구", "노원구"]
    return f'{random.choice(cities)}시 {random.choice(gus)}'

generate_address()