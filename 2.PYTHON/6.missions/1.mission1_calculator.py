#계산기 코드 작성하기
#연산자 & 두개의 숫자를 입력받아 그 결과를 출력하시오.
#무한반복하기 

# 1. 연산자 4개 중에 한 개를 입력 받는다. 

# 2. 4개 외 다른 문자/숫자를 입력 받았으면 오류를 발생시킨다. 
# 3. 사용자로부터 1번 숫자를 입력받는다.
# 4. 1번 숫자가 숫자가 아니면 오류를 발생시킨다. 
# 5. 사용자로부터 2번 숫자를 입력받는다. 
# 6. 2번 숫자가 숫자가 아니면 오류를 발생시킨다.
# 7. 입력받은 연산자, 1번 2번 숫자를 수식으로 만들어서 프린트한다. 
# 8. 다른 계산도 할 거냐고 묻는다. Y/N
# 9. if Y, back to 1. 
# 10. if N, return None

# 1. 연산자 4개 중에 한 개를 입력 받는다. 
operator = input("사칙연산만 가능함: ")    
# 2. 4개 외 다른 문자/숫자를 입력 받았으면 오류를 발생시킨다. (return None)
if operator == "+":
    print("덧셈 선택")
if operator == "-":
    print("뺄셈 선택")
if operator == "*":
    print("곱셈 선택")
if operator == "/":
    print("나눗셈 선택")
# if operator not in ["+", "-", "*", "/"]:
#     print("사칙연산만 가능합니다.")
#     result = None

# 3. 사용자로부터 1번 숫자를 입력받는다.
num1 = input("첫번째 숫자를 입력하세요: ")

# 4. 1번 숫자가 숫자가 아니면 오류를 발생시킨다.
if num1.isdigit():
    print("두번째 숫자를 입력하세요: ")

else:
    print("숫자를 입력하세요.")
# 5. 사용자로부터 2번 숫자를 입력받는다. 
num2 = input()
# 6. 2번 숫자가 숫자가 아니면 오류를 발생시킨다. 
# 7. 입력받은 연산자, 1번 2번 숫자를 수식으로 만들어서 프린트한다. 
def operation_complete():
    result = operation_complete()
    print(result)

if operator == "+":
    print(int(num1) + int(num2))
if operator == "-":
    print(int(num1) - int(num2))
if operator == "*":
    print(int(num1) * int(num2))
if operator == "/":
    print(int(num1) / int(num2))

answer = input("다른 계산을 원하면 Y, 종료하려면 N을 입력하세요.:")
if answer == "Y":
if answer == "N":
    
else: 
    result = None





# 8. 다른 계산도 할 거냐고 묻는다. Y/N
# 9. if Y, back to 1. 
# 10. if N, return None


