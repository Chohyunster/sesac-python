import random
import csv
from itertools import chain

class NameGenerator:
    names = []

    def __init__(self):       
        with open('names.txt', 'r', encoding = 'utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_names = [n for n in csvreader]
            names_list = list(chain(*csv_list_names))
            self.names = [n.strip() for n in names_list] #cf.콤마로 구분된 이름 리스트를 수정하려면: 위에 import csv 쓰고, csvreader = csv.reader(file) /n names = [n.strip() for n in csvreader][0] #여기서 strip은 불필요한 space를 제거해주는 기능. 
            
    def generate_name(self):
        return random.choice(self.names)