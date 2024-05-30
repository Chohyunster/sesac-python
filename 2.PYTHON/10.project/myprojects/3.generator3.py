import sys

from generators.address import AddressGenerator
from generators.birthdate import BirthdateGenerator
from generators.gender import GenderGenerator
from generators.id import IDGenerator
from generators.name import NameGenerator
from printers.output_printer import DataPrinter

class DataGenerator:
    numbers = 1
    data =[]
    
    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IDGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_users(self):
        self.data = []
        for _ in range (self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            
            a_user = (id, name, birthdate, gender, address)
            self.data.append(a_user)

#메인함수
if __name__ == "__main__":
    my_printer = DataPrinter()
    # print("입력인자 확인: 첫번쨰인자: {}, 두번째인자: {}".format(sys.argv[0], sys.argv[1]))

    if len(sys.argv) <= 1: #사용자 입력인자가 없으면...
        num_data = input('생성을 원하는 데이터 개수를 입력하세요:')
    else: #사용자 입력인자가 있으면...
        num_data = sys.argv[1]

    # print(sys.argv[2])
    # num_data = input("생성을 원하는 데이터의 개수를 입력하세요.")
    
    #우리가 원하는 데이터 형태 생성
    users1 = DataGenerator(int(num_data))
    users1.generate_users()
    
    my_printer.print_screen(users1.data)

# sys.stdout = open('usersfile.csv', 'w', encoding='utf-8')
# print(users1.generate_users())

# sys.stdout.close()


    #우리가 원하는 데이터 출력 - 화면, 파일
    # if len(sys.argv) == 3:
    #     if sys.argv[2] == 'screen':
    #         my_printer.print_screen(users1.data)
    #     elif sys.argv[2] == 'file':
    #         my_printer.print_file(users1.data)
    #     else:
    #         print('지원되지 않는 인자')