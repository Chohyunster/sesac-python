users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Busan", "car": "K5"},
]

#.get: 있는지 없는지 모르겠지만 있으면 줘줘
def find_user2(search):
    result = []

    for u in users:
        if (search.get('age') is None or u.get('age') == search['age']) and \
           (search.get('name') is None or u.get('name') == search['name']) and \
           (search.get('location') is None or u.get('location') == search['location']) and \
           (search.get('car') is None or u.get('nacarme') == search['car']):
            
            result.append(u)

    return result


# search_criteria1 = {"name" : "Bob"}
search_criteria2 = {"name" : "Alice", "age" : 25}
# search_criteria3 = {"location" : "Jeju", "car" : "BMW"}

print(find_user2(search_criteria2))




