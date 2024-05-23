#예외처리: try, except, (else, finally)로 한다. 

def div(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "입력값에 숫자가 아닌 값이 있습니다."    
    except:
        print("알 수 없는 이유로 나눌 수 없습니다.")
        return "NaN"
    else:
        print("오류가 안나고 계산을 잘 완료 했습니다")
    finally:
        print("여기는 오류든 성공이든 무조건 호출됩니다.")
    
    return result

print(div(5, 3))
print(div(10, 2))
print(div(15, 5))
print(div(15, 0))
print(div(15, 'a'))