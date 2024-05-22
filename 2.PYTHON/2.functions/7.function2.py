

def print_gugudan(dan=2, max=9):
    print(f'{dan}단')
    for i in range(1,max+1):
        print(f'{dan} x {i} = {dan * i}')

print_gugudan(3, 9)
print_gugudan(dan=3, max=9)
print_gugudan(max=9, dan=3)

print('실험')
print_gugudan(max=9)
print_gugudan(9)