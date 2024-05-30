import random

# def generate_storetype():
#     with open('c:/SESAC/2.PYTHON/11.myproject/generators/storelist.txt', 'r', encoding = 'utf-8') as file:
#         storetype = file.read().splitlines()
#         print(storetype)

# generate_storetype()

def generate_storename():
    with open('c:/SESAC/2.PYTHON/11.myproject/generators/storelist.txt', 'r', encoding = 'utf-8') as file:
        storetype = file.read().splitlines()
    with open('c:/SESAC/2.PYTHON/11.myproject/generators/storeaddresslist.txt', 'r', encoding = 'utf-8') as file2:
        storeaddress = file2.read().splitlines()
    ho = random.randint(1,10)
    ty = random.choice(storetype)
    return f"{ty} {random.choice(storeaddress)} {ho}호점, {ty}"

