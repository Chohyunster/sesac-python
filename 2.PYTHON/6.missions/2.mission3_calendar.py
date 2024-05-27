import calendar
print(calendar.month(2024, 5))

year = int(input("연도를 입력하세요: "))
month = int(input("월을 입력하세요: "))

print(calendar.month(year, month))

#import library하지 말고 짜보기 
def print_calendar(year, month):
    for i in range(1, 30):
        print(f"{i}", end = "")
        if i % 7 == 0: