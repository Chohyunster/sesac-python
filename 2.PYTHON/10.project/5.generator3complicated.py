#코드를 짜고 재 구조화 하는 것: 리펙토링(refactoring) cf. 기능을 추가하지는 않는다.

import random
import uuid

class IDGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class NameGenerator:
    names = ['John', 'Jane', 'Michael', 'Emily', 'Wiliam', 'Olivia']
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
    cities = ['Seoul', 'London', 'Tokio', 'Newyork', 'Adisababa']

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1,100)
        return f"{street} {city}"

# class DataGenerator:
    
#     numbers = 1

    

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
            id = IDGenerator.generate_id()
            name = NameGenerator.generate_name()
            birthdate = BirthdateGenerator.generate_birthdate()
            gender = GenderGenerator.generate_gender()
            address = AddressGenerator.generate_address()
            
            a_user = (id, name, birthdate, gender, address)
            self.data.append(a_user)

users = DataGenerator(10)
users.generate_users()

for d in users.data: 
    print(d)