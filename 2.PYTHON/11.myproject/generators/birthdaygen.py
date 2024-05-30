import random

def generate_birthday():
    year = random.randint(1960, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)    
    return f'{year}-{month:02}-{day:02}'

generate_birthday()