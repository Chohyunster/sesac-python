#a = input('숫자를 입력하세요: ')
#print(a)

#.미션3. 숫자를 두개 입력 받아서, 덧셈 결과를 출력하시오. 

str_a = input('첫번째 숫자를 입력하세요: ')
str_b = input('두번째 숫자를 입력하세요: ')

#.input값의 모든 것은 다 문자열로 처리된다.
#우리가 해야할 것은 형 변환..! = type casting

int_a = int(str_a)
int_b = int(str_b)

print(f'두 숫자의 합은{int_a + int_b}입니다.')


