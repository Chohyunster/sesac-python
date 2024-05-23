import random

#미션1. 1~100 중 랜덤숫자를 생성하는 함수를 찾아서 출력하시오
print(random.randint(1,100))

#미션2. 주사위를 던지는 함수를 작성하시오
def roll_dice():
    return random.randint(1,6)
    
print("주사위를 던진 결과는: ", roll_dice())

#미션3. 리스트에서 랜덤으로 요소를 선택하기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']

def choose_random_element(elements):
    return random.choice(elements)

print("당신이 선택한 상품은: ", choose_random_element(elements))

#.미션3_1. 수동으로 짜보기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']

def choose_random_element(elements):
    random_index = random.randint(0, len(elements) - 1)
    print(random_index)
    return elements[random_index]
print("당신이 선택한 상품은: ", choose_random_element(elements))

#미션4. 랜덤으로 element 리스트에 숫자 리스트 섞기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
numbers = [1, 2, 3, 4, 5]

def random_list_fruits(elements):
    random.shuffle(elements)
    return elements

def random_list_numbers(numbers):
    random.shuffle(numbers)
    return numbers

print("원본 리스트1: ", elements)
print("원본 리스트2: ", numbers)

print("석인 리스트: ", random_list_fruits(elements))
print("섞인 리스트: ", random_list_numbers(numbers))

#.미션5 랜덤으로 문자열 생성 : 영문 대문자 6자리


#.미션6, 랜덤 초이스에서 가중치를 고려한 랜덤

#.미션7, 랜덤 비밀번호 생성(대소문자, 숫자포함 6자리)

#.미션8, 강력한 비밀번호 생성(대문자, 소문자, 숫자를 각각 1개이상 포함하는 8자리를 만들어라)
