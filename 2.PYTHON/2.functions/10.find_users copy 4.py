users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Busan", "car": "K5"},
]

# #.get: 있는지 없는지 모르겠지만 있으면 줘줘
# def find_user2(search):
#     result = []

#     for u in users:
#         if (search.get('age') is None or u.get('age') == search['min_age']) and \
#            (search.get('min_age') is None or u.get('age') >= search['min_age']) and \
#            (search.get('name') is None or u.get('name') == search['name']) and \
#            (search.get('location') is None or u.get('location') == search['location']) and \
#            (search.get('car') is None or u.get('nacarme') == search['car']):
            
#             result.append(u)

#     return result


# search_criteria1 = {"name" : "Bob"}
# search_criteria2 = {"name" : "Alice", "age" : 25}
# search_criteria3 = {"location" : "Jeju", "car" : "BMW"}
# search_criteria4 = {"name": "Alice", "min_age" : 20} #기대치는 2명
search_criteria5 = {"name": "Alice", "min_age" : 30} 
search_criteria6 = {"name": "Alice", "min_age" : 30} 


# print(find_user2(search_criteria4))

def find_user3(search):
    result = []

    for u in users:
        if match_criteria(u, search):
            result.append(u)

    return result

def match_criteria(user, criteria):
    for key, value in criteria.items(): #딕셔너리 안에 있는 k,v쌍을 하나씩 추출하는 함수 = items
        if key == "age":
            if user["age"] != value:
                return False
        if key == "name":
            if user["name"] != value:
                return False    
        if key == "location":
            if user["location"] != value:
                return False
        if key == "car":
            if user["car"] != value:
                return False

    return True


print(find_user3(search_criteria5))




