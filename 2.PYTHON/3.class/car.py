class car:
    make = ''
    model = ''
    ordometer = 0

    def get_name(self):
        print(f'{self.make} {self.model}')

    def get_ordometer(self):
        print(f'현재까지의 주행거리는 {self.ordometer}입니다.')

    def drive(self, mileage):
        #self.ordometer = self.ordometer + mileage
        self.ordometer += mileage

mycar = car()
mycar.make = '현대차'
mycar.model = '아이오닉5'

mycar.get_name()
mycar.get_ordometer()
mycar.drive(100)
mycar.get_ordometer()


