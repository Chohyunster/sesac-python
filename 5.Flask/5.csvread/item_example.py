my_dict = {'name': "Alice", 'age': 25, 'phone': '123-456-7890'}

#빌트인 함수 = 내장함수 = 파이썬에 기본 탑재된 함수. cf. 빌트인 모듈안에 있는 빌트인함수도 있음. 
items = my_dict.items()
print(items)

print(type(items)) #타입은 dict_items이다. 리스트처럼 생겼지만 리스트 아님.
items_list = list(items) #type casting = 형변환.

print('-' * 50)

a = '25'
print(a)
print(type(int(a)))

print('-' * 50)

for item in items_list:
    print(item)

for key, value in items_list:
    print(f'키: {key}, 값: {value}')


print('-' * 50)

for key, value in my_dict.items():
    print(f'키: {key}, 값: {value}')

print('-' * 50)

for key, value in sorted(my_dict.items()): #알파벳순으로 소팅됨.
    print(f'키: {key}, 값: {value}')


print('-' * 50)

my_dict['car'] = 'K5'
print(my_dict)

#딕트에 딕트를 추가하기 방법1
update_dict = {'car': 'k5', 'city': 'Seoul'}

for key, value in update_dict.items():
    my_dict[key] = value

#딕트에 딕트를 추가하기 방법2 (이 방법은 파이썬 3.9 이상에서 가능하다.)
new_dict = my_dict | update_dict
print(f'통합본: {new_dict}')

print('-' * 50)

users = [ {'name': "Alice", 'age': 25, 'phone': '123-456-7890'},
          {'name': "Bob", 'age': 19, 'phone': '123-456-7890'},
          {'name': "NewBob", 'phone': '123-456-7890'},
            {'name': "Charlie", 'age': 22, 'phone': '123-456-7890'}, 
]

# filtered_user = []
# for user in users: 
#     if user['age'] >= 20:
#         filtered_user.append(user)

filtered_user = []
for user in users: 
    if user.get('age', 0) >= 20:
        filtered_user.append(user)
print(filtered_user)

#코드 한줄로 줄이기.
filtered_user = []
filtered_user = [user for user in users if user.get('age', 0) >= 20]
print(filtered_user)

#또 다른 방법으로.
filtered_user_ages = [{key: value for key, value in u.items() if key == 'age' and value >= 20} for u in users]
print(filtered_user_ages)

