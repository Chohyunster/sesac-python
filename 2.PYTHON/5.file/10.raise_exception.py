#.아래방법을 사용해도 되지만(좋지만), raise를 사용해서 짜도 된다. 
# def input_age(age):
#     if age < 0:
#         print("음수를 넣을 수 없습니다")
#         return None
    
#     print(age)

#     return(age)

# input_age(10)
# input_age(15)
# input_age(17)
# input_age(-2)

#==================================
#내가 원하는 에러를 강제로 발생시키기 = raise
#이걸 다시 잡아서 처리하기 try ~ except

def input_age(age):
    if age < 0:
        raise ValueError("음수를 넣을 수 없습니다")
    
    print(age)

    return(age)

try:
    input_age(10)
    input_age(15)
    input_age(17)
    input_age(-2)
except ValueError as e:
    print("입력값에 오류가 있습니다: ", e)