#1.문자를 입력받아, 대소문자를 변경하시오.
# 문자내의 대분자->소문자, 소문자->대문자 ex.HeLLO => hEllo

def convert_case(text):
    converted = ""
    for char in text:
        if char.islower():
            converted += char.upper()
            # converted = converted + char.upper() 이것과 윗줄은 같다.
        elif char.isupper():
            converted += char.lower()
        else:
            converted += char

    return converted

print(convert_case('HEllo'))
print(convert_case('GoodBye'))
print(convert_case('Good Bye'))
print(convert_case('This is a long message. haha1234'))

def convert_case_advanced(text):
    return ''.join([char.upper() if char.islower() else char.lower90 for char in text])
#for char in text #text를 읽어서 char 추출한다.
#맨앞에 char는 for문의 결과인 char가 담기는 곳이다.


print(convert_case_advanced("HelLo"))
