operator = input("사칙연산 중 하나 선택하세요.: ")    
def operator_option(operator):
    if operator == "+":
        print("덧셈 선택")
    elif operator == "-":
        print("뺄셈 선택")
    elif operator == "*":
        print("곱셈 선택")
    elif operator == "/":
        print("나눗셈 선택")
    else:
        print("사칙연산자를 입력하세요.")

    result = operator
    return result

operator_option(operator)

num1 = input("첫번째 숫자를 입력하세요: ")
num2 = input("두번째 숫자를 입력하세요: ")

def calculation():
    if not num1.isdigit():
        print("숫자를 입력하세요.")
    if not num2.isdigit():
        print("숫자를 입력하세요.")
    else:
        if operator == "+":
            print(int(num1) + int(num2))
        if operator == "-":
            print(int(num1) - int(num2))
        if operator == "*":
            print(int(num1) * int(num2))
        if operator == "/":
            print(int(num1) / int(num2))

calculation()

# answer = input("다른 계산을 원하면 Y, 종료하려면 N을 입력하세요.:")
# def infinite_calc(answer):
#     if answer == "Y":
#         operator = input("사칙연산 중 하나 선택하세요.: ")
#         operator_option(operator)
#         num11 = input("첫번째 숫자를 입력하세요: ")
#         num22 = input("두번째 숫자를 입력하세요: ")
#         def calculation():
#             if not num11.isdigit():
#                 print("숫자를 입력하세요.")
#             if not num22.isdigit():
#                 print("숫자를 입력하세요.")
#             else:
#                 if operator == "+":
#                     print(int(num11) + int(num22))
#                 if operator == "-":
#                     print(int(num11) - int(num22))
#                 if operator == "*":
#                     print(int(num11) * int(num22))
#                 if operator == "/":
#                     print(int(num11) / int(num22))
#         calculation()
#         answer = input("다른 계산을 원하면 Y, 종료하려면 N을 입력하세요.:")
#         infinite_calc(answer)
#     if answer == "N":
#         print("계산 종료")
#     else:
#         print("Y 또는 N으로 대답하세요.")

#     return None

# infinite_calc(answer)

