users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Busan", "car": "K5"},
]
#.여러개의 딕셔너리를 가진 리스트

# def find_user(name):
#     for u in users:
#         # print(u['name'])
#         if u.get("name").lower() == name.lower():
#             print(u)
#             return u
        
#     print('찾는 사용자가없습니다')

# find_user('Alice')

def find_user(name):
    found_user = []
    for u in users:
        if u.get("name").lower() == name.lower():
            # print(u)
            found_user.append(u)
            # return u

    return found_user
        
    # print('찾는 사용자가없습니다')

found = find_user('Alice')
print(f'찾은 사용자: {found}')
