from users import *
from store import *
from items import *
from order import *
from orderitem import *
#함수 이름 풀어써주기

def start():
    category = input("원하는 카테고리의 숫자를 써주세요.(1.user, 2.store, 3.item, 4.order, 5.orderitem): ")
    if category == "1":
        users = generate_users()
        print_user_scr(users)
    elif category == "2":
        stores = generate_stores()
        print_store_csv()
    elif category == "3":
        items = generate_items()
        print_item_scr(items)
    elif category == "4":
        users = generate_users()
        print_user_scr(users)
    elif category == "5":
        users = generate_users()
        print_user_scr(users)
    else:
        print("입력 오류")
        

start()




