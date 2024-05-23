import csv

file_path = "mydata.csv"
data = [
        ["Name", "Age", "City"],
        ["John", 20, "Seoul"],
        ["Jane", 25, "Busan"],
        ["Bob", 35, "Jeju"],
        ]

with open(file_path, "w", encoding="UTF=8", newline="") as file:
        csv_w = csv.writer(file)
        # csv_w.writerow(["이름"], ["나이"])
        # csv_w.writerow(["Alice", 30])
        # csv_w.writerow(["Alice.Jr", 5])
        # csv_w.writerow(["Bob", 35])
        # csv_w.writerow(["Bob.Jr", 7])
        csv_w.writerows(data)