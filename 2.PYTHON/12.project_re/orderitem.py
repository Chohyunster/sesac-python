# Id,OrderId,ItemId

import random
import csv

from generators.idgen import generate_id

def bring_orderid():
    order_list = []
    with open('Neworderlist.csv', 'r', encoding = 'utf-8', newline = '') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            order_list.append(row)

    return random.choice(order_list[1:])[0]


def bring_itemid():
    item_list = []

    with open('Newitemlist.csv', 'r', encoding = 'utf-8', newline = '') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            item_list.append(row)
          
    return random.choice(item_list[1:])[0]


#=====Order Data 만들기 ======================
orderitemdata = [("Id", "OrderId", "ItemId")]

def generate_orderitems():
    num = int(input("생성하고자 하는 오더아이템 개수 입력하세요.: "))
    for _ in range(num):
        id = generate_id()
        orderid = bring_orderid()
        itemid = bring_itemid()
        
        an_orderitemdata = (id, orderid, itemid)
        orderitemdata.append(an_orderitemdata)

    return orderitemdata

# result = generate_orderitems()
# print(result)


#===========오더아이템 리스트 csv로 출력====================
import csv

def print_csv():
    result = generate_orderitems()
    with open('Neworderitemlist.csv', 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)
        
# print_csv()

