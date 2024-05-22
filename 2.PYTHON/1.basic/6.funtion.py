def hello():
    print('hello1')
    print('hello2')
    print('hello3')

hello()

def numbers(num1):
    result = num1 + 4
    return result

#numbers(3) 이렇게 하면 아무것도 안나옴
print(numbers(3))

num1 = numbers(3)
num2 = numbers(4)

print(num1)
print(num1, num2)

#--------------
#미션1: 덧셈을 하는 함수를 작성하시오. 숫자 두개를 입력 받아서, 해당 숫자의 합산을 반납한다. 

print('sum practice')

def add(num1, num2):
    result = num1 + num2
    return result

print(add(3,5))

def add(num1, num2):
    return num1 + num2

print(add(5,9))

def add3(num1, num2):
    return num1, num2, num1+num2

print(add3(1,2))
#이것의 결과는 (1,2,3)으로 나오는데, 이것은 tuple이다.

#미션2. 뺄셈, 곱셈, 나눗셈 함수도 만들어보기

def minus(num1, num2):
    result = num1 - num2
    return result

print(minus(10,5))

def multi(num1, num2):
    result = num1 * num2
    return result
print(multi(10,5))

def div(num1, num2):
    return num1 / num2
print(div(10,2))
#print(div(10,0)) 이렇게 0으로 나누려 하면 zero division error 뜬다. 이걸 해결하기 위해 try를 씀.










