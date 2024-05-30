import random
import csv

from generators.idgen import generate_id

def generate_orderday():
    year = random.randint(2000, 2024)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return f"{year}-{month:02d}-{day:02d}"

def generate_orderat():
    hour = random.randint(0, 23)
    min = random.randint(0, 60)
    sec = random.randint(0, 60)
    return f"{hour}:{min:02d}:{sec:02d}"

def bring_storeid():
    store_list = []
    with open('c:/SESAC/2.PYTHON/11.myproject/Newstorelist.csv', 'r', encoding = 'utf-8', newline = '') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            store_list.append(row)

    return random.choice(store_list[1:])[0]


def bring_userid():
    user_list = []

    with open('c:/SESAC/2.PYTHON/11.myproject/Newuserlist.csv', 'r', encoding = 'utf-8', newline = '') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            user_list.append(row)
          
    return random.choice(user_list[1:])[0]


#=====Order Data 만들기 ======================
orderdata = [("Id", "OrderAt", "StoreId", "UserId")]

def generate_orderdata():
    for _ in range(10):
        orderid = generate_id()
        orderdate = generate_orderday()
        ordertime = generate_orderat()
        storeid = bring_storeid()
        userid = bring_userid()

        an_orderdata = (orderid, orderdate, ordertime, storeid, userid)
        orderdata.append(an_orderdata)

    return orderdata

result = generate_orderdata()

#===========오더 리스트 csv로 출력====================
import csv

def print_csv():
    with open('Neworderlist.csv', 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)
        
print_csv()
