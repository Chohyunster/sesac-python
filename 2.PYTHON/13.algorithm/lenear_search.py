#선형탐색 (Linear Search) : 앞에서부터 하나하나 찾아나가는 것

import time

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return -1

my_list = [5,3,3,12,5,7,11]
target = 7

start_time = time.time()
result = linear_search(my_list, target)
end_time = time.time()

result = linear_search(my_list, target)
if result != -1:
    print("타겟을 찾았습니다: index: ", result)
else:
    print("타겟이 존재하지 않습니다.")

import random
def generate_random_num(count):
    random_num = [random.randint(1, count) for _ in range(count)]
    return random_num

my_sec_list = generate_random_num(1000000)

start_time = time.time()
result = linear_search(my_sec_list, target)
end_time = time.time()
