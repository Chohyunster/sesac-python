def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        print(i)
        result = result * i

    print(f'{n}팩토리알은 {result}입니다.')
    

factorial(5)
factorial(7)
factorial(10)
