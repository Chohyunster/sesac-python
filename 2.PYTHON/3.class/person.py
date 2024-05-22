class person:
    #명사, property를 정의할 수 있음
    name = ""
    age = 0
    status1 = "playing"

    def __init__(self, name, age): #이 객체의 초기화 함수
        self.name = name
        self.age = age

    #메소드 (함수 = 행위를 지정하는 동사)
    def speak(self):
        print(f'{self.name}: 안녕하세요')

    def walk(self):
        print(f'{self.name}: 저는 걸어가는 중입니다')
        self.status1 = "walk"

    def run(self):
        print(f'{self.name}: 저는 뛰어가는 중입니다')
        self.status1 = "think"

    def motion(self):
        print(f'{self.name}:나의 현재 상태는 {self.status} 중입니다.')

    def introduce(self):
        print(f'안녕하세요, 저는 {self.name}이고 {self.age} 살입니다.')

    def status2(self):
        print(f'현재상태: {self.status1}')

#사람(person)이라는 객체를 만들고,
#사람이 할 수 있는 행위(method)인 speak와 walk를 정의
#사람이라는 객체를 정의(define)한 상태
#이 객체가 만들어지지도 않은 것
#객체의 함수는 첫번쨰 인자가 self여야 한다.(그냥 이건 암기해야) b/c 나중에 필요할 때 객체 자신의 속성 등 필요한 부분에 접근하기 위해서..!

#이 객체를 통해서 사람을 만들기
# alice = person()
# alice.name = 'Alice'
# alice.age = 30

alice = person('Alice', 30)

alice.introduce()
alice.speak()
alice.walk()
alice.run()
alice.status2()

# bob = person()
# bob.name = 'bob'
# bob.age = 25

bob = person('bob', 25)

bob.introduce()
bob.speak()
bob.walk()
bob.run()
bob.status2()

