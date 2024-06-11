from generators.idgen import generate_id
from generators.storename_typegen import generate_storename
from generators.addressgen import generate_address


#======사용자 데이터 생성========================================
storedata = [("ID", "Name", "Type", "address")]

def generate_stores():
    num = int(input("생성하고자 하는 스토어 개수 입력하세요.: "))
    for _ in range(num):
        ID = generate_id()
        nametype = generate_storename()
        address = generate_address()

        a_user = (ID, nametype, address)
        storedata.append(a_user)

    return storedata

if __name__ == "__main__":
    result = generate_stores()
    # print(result)

#==== csv 파일생성 ========================

import csv

def print_store_csv():
    result = generate_stores()
    with open('Newstorelist.csv', 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)
        
# print_store_csv()
        
        