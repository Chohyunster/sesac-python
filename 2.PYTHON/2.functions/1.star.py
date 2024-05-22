# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

# print('hello' * 10)


# for i in range(1,6):
#     print(i)

# for i in range(1,10):
#     print('*' * i)    

# #.아래 세개는 다 같은 결과가 나온다. 

# row = input('출력을 원하는 높이를 입력하세요:')
# num_rows = int(row)
# for i in range(1,num_rows + 1):
#     print('*' * i)

# row = int(input('출력을 원하는 높이를 입력하세요:'))
# for i in range(1,row + 1):
#     print('*' * i)

# row = int(input('출력을 원하는 높이를 입력하세요:'))
# for i in range(1,int(row+1)):
#     print('*' * i)

# rows = 5
# for i in range(1, rows + 1):
#     print(' ' * (rows-i), '*' * i)

rows = 5

for i in range(1, rows+1):
    print(rows-i, i)

for i in range(1, rows+1):
    print(' ' * (rows-i), '*' * i)

for i in range(1, rows+1):
    print(' ' * (rows-i), '*' * (2*i-1))

for i in range(1, rows+1):
    print(' ' * (rows-i), '*' * (2*i-1))
