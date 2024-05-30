from generators.idgen import generate_id
from generators.itemnamegen import *


#======아이템 데이터 생성========================================

itemdata = [("Id", "Name", "Type", "UnitPrice")]
def generate_items():
    
    for _ in range(10):
        itemname=generate_itemname()
        
        ID = generate_id()
        item_name = itemname["name"]
        item_type = itemname["type"]
        unitprice = itemname["unitprice"]

        an_item = (ID, item_name, item_type, unitprice)
        print(an_item)
        itemdata.append(an_item)

    return itemdata

result = generate_items()

#=========csv 파일로 저장==================================
import csv

def print_csv():
    with open('Newitemlist.csv', 'w', encoding='utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)

print_csv()

# #==========screen으로 보기===============================
# def print_scr():
#     print(result)
