import random
import csv
from itertools import chain

class AddressGenerator():
    cities = []
    
    def __init__(self):
        with open('cities.txt', 'r', encoding = "utf - 8") as file:
            reader = csv.reader(file)
            data = [line for line in reader]
            data = list(chain.from_iterable(data))
            self.cities = [d.strip() for d in data]

    # def __init__(self):
    #     with open('cities.txt', 'r', enconding = "utf = 8") as file:
    #         cities = file.read().splitlines()
    #         print(cities)

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1,100)
        return f"{street} {city}"
    

    
