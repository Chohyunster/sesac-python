# def remove_duplicate(numbers):
#     unique_list = []

#     for n in numbers:
#         duplicate_check = False

#         for u in unique_list:
#             print(f'입력값: {n}, 유닠목록: {u}')

#             if n == u:
#                 print(f'중복': {n} == {u})
#                 duplicate_check = True
#                 break

#         if not duplicate_check:
#             print(f'중복이아닌것:{n}')
#             unique_list.append(n)       
        
        
#     return unique_list

numbers = [1, 3, 5, 4, 7, 8, 1, 6, 6, 5, 5, 4, 1]
unique_numbers = remove_duplicate(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)

#조금더 파이썬스러운 스타일
def remove_duplicate2(numbers):
    unique_list = []
    for n in numbers:
        if n in unique_list:
            pass
        else:
            unique_list.append(n)

    return unique_list

#more
def remove_duplicate3(numbers):
    unique_list = []

    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)

    return unique_list

#modern python code
def remove_duplicate4(numbers):
    return list(set(numbers)) 
    #여기서 list는 list 형태로 만들어주는 역할.

