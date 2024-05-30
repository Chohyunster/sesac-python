import random

def generate_gender():
    gender = ["Male", "Female"]
    gender = random.choice(gender)
    return gender

# print(generate_gender())