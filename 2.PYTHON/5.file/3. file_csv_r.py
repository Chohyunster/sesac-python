import csv

file_path = "mydata.csv"

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row[0]) #리스트라서 인덱싱
