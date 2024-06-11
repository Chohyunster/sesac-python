import random
import csv

#<수정할 사항> : 공통적인 부분을 리스트에 넣어서 for로 반복 출력하기 
#itemlist = [{'choice': 'coffee', 'filepath': 'coffee.csv'}, {'choice': 'juice', 'filepath': 'juice.csv'}, {'choice': 'cake', 'filepath': 'cake.csv'}]
# for item in itemlist:
#     load_file = item[filepath]


def generate_itemname():
    
    choice_options = ("coffee", "juice", "cake")
    choice = random.choice(choice_options)
    
    if choice == "coffee":
        options = []
        with open("c:/SESAC/2.PYTHON/11.myproject/generators/coffee.csv", 'r', encoding = 'utf-8', newline = '') as coffeefile:
            coffee_reader = csv.DictReader(coffeefile)

            for _ in coffee_reader:
                options.append(_)
                # print(_)

        # print(random.choice(options))

    elif choice == "juice":
        options = []
        with open("c:/SESAC/2.PYTHON/11.myproject/generators/juice.csv", 'r', encoding = 'utf-8', newline = '') as juicefile:
            juice_reader = csv.DictReader(juicefile)

            for _ in juice_reader:
                options.append(_)
                # print(_)
        
        # print(random.choice(options))
                
    elif choice == "cake":
        options = []
        with open("c:/SESAC/2.PYTHON/11.myproject/generators/cake.csv", 'r', encoding='utf-8', newline = '') as cakefile:
            cake_reader = csv.DictReader(cakefile)

            for _ in cake_reader:
                options.append(_)
                # print(_)
    
    return random.choice(options)




                
