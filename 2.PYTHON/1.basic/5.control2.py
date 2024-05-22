x = 12

if x < 10:
    print('x가 10보다 작습니다')
else:
    print('x가 10보다 큽니다')

#---
score = 72

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score,grade)

print("score: {}, grade: {}".format(score,grade))
print("score: {0}, grade: {1}".format(score,grade))
print("score: {1}, grade: {0}".format(score,grade))

print(f'점수는 {score}이고, 성적은 {grade}입니다') #포멧팅
print('점수는 {score}이고, 성적은 {grade}입니다') #문자열

math = 70
eng = 90

if math >= 90 or eng >= 90: #and/or
    print('졸업조건 충족')
    print('안녕히 가세요')
else:
    print('졸업 미흡')



