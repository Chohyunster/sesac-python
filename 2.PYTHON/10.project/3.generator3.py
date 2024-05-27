#코드를 짜고 재 구조화 하는 것: 리펙토링(refactoring) cf. 기능을 추가하지는 않는다.

import random
import uuid

class IDGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class NameGenerator:
    names = []

    def __init__(self):       
        with open('names.txt', 'r', enconding = "utf = 8") as file:
            names = file.read().splitlines() #cf.콤마로 구분된 이름 리스트를 수정하려면: 위에 import csv 쓰고, csvreader = csv.reader(file) /n names = [n.strip() for n in csvreader][0] #여기서 strip은 불필요한 space를 제거해주는 기능. 
            print(names)

    def generate_name(self):
        return random.choice(self.names)

class BirthdateGenerator:
    year_start = 1980
    year_end = 2005

    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f"{year}-{month:02d}-{day:02d}" #month를 찍되 두자리의 수로 찍을 거야: 02d

class GenderGenerator:
    gender = ['Male', 'Female']
    def generate_gender(self):
        return random.choice(self.gender)

class AddressGenerator():
    cities = []
    
    def __init__(self):
        with open('cities.txt', 'r', enconding = "utf = 8") as file:
            cities = file.read().splitlines()
            print(cities)

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1,100)
        return f"{street} {city}"

class DataGenerator:
    numbers = 1
    data =[]
    
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IDGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_users(self):
        self.data = []
        for _ in range (10):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            
            a_user = (id, name, birthdate, gender, address)
            self.data.append(a_user)

#메인함수
if __name__ == "__main__":
    
    users = DataGenerator(10)
    users.generate_users()

    for d in users.data: 
        print(d)