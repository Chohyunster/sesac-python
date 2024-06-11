import random

surname = ["김", "박", "이", "송", "차", "길", "황", "최"]
middlename = ["가", "나", "다", "라", "마", "바", "사", "아", "자"]
lastname = ['차', "카", "타", "파", "하", "림", "현", "인", "미"]

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    return name