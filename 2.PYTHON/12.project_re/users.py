from generators.idgen import generate_id
from generators.namegen import generate_name
from generators.birthdaygen import generate_birthday
from generators.agegen import generate_age
from generators.gendergen import generate_gender
from generators.addressgen import generate_address


#======사용자 데이터 생성========================================
userdata = [("ID", "Name", "Birthday", "Age", "Gender", "address")]
def generate_users():
    num = int(input("생성하고자 하는 유저 개수 입력하세요.: "))
    for _ in range(num):
        ID = generate_id()
        name = generate_name()
        birthday = generate_birthday()
        age = generate_age()
        gender = generate_gender()
        address = generate_address()

        a_user = (ID, name, birthday, age, gender, address)
        userdata.append(a_user)

    return userdata

if __name__ == "__main__":

    result = generate_users()


#=========csv 파일로 저장==================================
import csv

def print_user_csv():
    with open('Newuserlist.csv', 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)

#==========screen으로 보기===============================
def print_user_scr(result):
    print(result)
    

#==========console, csv====================================

if __name__ == "__main__":
    operator = input("프린트 방법을 선택하세요(1.csv / 2.screen): ")
    def operator_option(operator):
        if operator == "1":
            print_csv()
            print("파일 저장 완료")
        elif operator == "2":
            print_user_scr()
        else:
            print("1, 2 중에서 입력하세요.")

        return operator

    operator_option(operator)
        