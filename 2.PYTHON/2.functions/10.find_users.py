users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Busan", "car": "K5"},
]

def find_user(name=None, age=None):
    found_user = [] #회색으로 돼있는 건 안 쓰이는 코드
    if name is None and age is None:
        return users


    for u in users:
        #둘다 입력값이 있음.
        if name is not None and age is not None: 
            if u["name"].lower() == name.lower() and u["age"] == age:
                return u
        #아니면, 이름만 있음.
        elif name is not None:
            if u["name"].lower() == name.lower():
                return u
        #아니면, 나이만 있음.
        elif age is not None:    
            if u["age"] == age:
                return u
            
          
    return None



        # print(f'가져온것: {u["name"]}, {u["age"]}, 입력받은것: "{name}", "{age}"')
        # if u.get("name").lower() == name.lower():
        #     if age is None:
        #         found_user.append(u)
        #     else:
        #         if u.get("age") == age:
        #             found_user.append(u)

    # return found_user

# found = find_user('alice', 25)
# found = find_user('alice')
# found = find_user(age=25)
found = find_user()

print(f'찾은 사용자: {found}')


