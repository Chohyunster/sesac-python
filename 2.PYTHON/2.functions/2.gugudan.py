dan = 7

def print_gugudan(dan):
    print(dan)
#.여기까지만 하면 함수가 호출되지 않았으므로 아무것도 실행 안된다.
print_gugudan(dan)

dan = int(input('계산을 원하는 단을 입력하시오'))
def print_gugudan(dan):
    print(f'{dan}단')
    for i in range(1,10):
        print(f'{dan} x {i} = {dan * i}')

print_gugudan(dan)