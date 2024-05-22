#1.일반문자열 출력
print("-1-")
print("hello")
print('hello world')
print('hello', 'world')
print(1,2,3)

#2. f-문자열 (f-string)을 활용한 출력
print("-2-")
print(f"hello {1}")
내변수 = '123'
print(f"hello {내변수}")
myvariable = '456'
print('hello {내변수}는 {myvariable}')

#3. 문자열 포멧팅 {}을 사용한 치환
print("-3-")
name = "honggil"
print("hello, {}".format(name))
print("hello, {} x {} = {}".format(내변수, myvariable, name))

#4.문자열 포멧팅에 순번 부여하기
print("-4-")
print("hello, {0} x {1} = {2}".format(내변수, myvariable, name))
print("hello, {2} x {0} = {1}".format(내변수, myvariable, name))
print("hello, {2} x {1} = {0}".format(내변수, myvariable, name))

#5.문자열 연결 연산자
print("-5-")
print("hello", end = "")
print('world', end = "")
print("sesac")

#6. %연산자 : 예전에 가장 보편적인 방식
print("-6-")
age = 18
print('hello, %s' % name) #%s는 문자열(string)
print('hello, %d' % age) #%d는 숫자(decimal)
print('hello, %s' % age)

