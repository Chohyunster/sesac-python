a = 5
a2 = [5]
b = [1, 2, 3, 4, 5]

print(a)
print(b)

print(b[0])
print(b[4])
#print(b[5]) #indexerror발생

print(len(b))

print(b[1:3])

fruit = ['apple', '사과', 'grape', '포도']
print(fruit)

print(fruit[1:3])

members = [3, '"my" desk and chair', 2, -1, "chair"]
print(members)

b.remove(1)
print(b)

fruit.remove('apple')
print(fruit)

#insert는 삽입, append는 덧붙이기
#b.append(20)
#print(b)

b.insert(0, 20)
print(b)

#a.insert(0,10) : typeerror
a2.insert(0,10)
print(a2)

#-----------
#3.튜플 (tuple) : 리스트와 동일한데, 변경 불가한 리스트를 생성
c = (1,2,3,4,5)
print(c)

#c.remove(2)
#c.appen(2)

#.c.remove(2) #삭제불가
#.c.append(2) #삽입불가

print(c[3], c[4])
print(c[2:])
print(b[2:])
print(c[:2])
print(b[:2])

#--------
#3.딕셔너리

user1 = {
    "name":"park",
    "age":10,
    "city":"seoul"

}

print(user1)
print(user1["name"])
print(user1["age"])
print(user1["city"])

user1["email"] = 'hello@gmail.com'
print(user1)

user1['email'] = ''
print(user1)

del user1['email']
print(user1)

