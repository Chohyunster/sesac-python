import random

class NameGenerator:
    names = []

    def __init__(self):       
        with open('names.txt', 'r', encoding = "utf - 8") as file:
            names = file.read().splitlines() #cf.콤마로 구분된 이름 리스트를 수정하려면: 위에 import csv 쓰고, csvreader = csv.reader(file) /n names = [n.strip() for n in csvreader][0] #여기서 strip은 불필요한 space를 제거해주는 기능. 
            print(names)

    def generate_name(self):
        return random.choice(self.names)