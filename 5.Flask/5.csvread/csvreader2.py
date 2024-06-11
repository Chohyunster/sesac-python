import csv
from flask import Flask, render_template
import math

app = Flask(__name__)

csv_data = []
headers = []

def load_csv_data(filename):
    global headers #밖에 있는 변수(글로벌변수)를 가져다가 변경할 때 이렇게 선언해야 함.

    with open(filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile) #파일명 안에 딕셔너리 형태로 읽어줘라. -> list of dictionary
        headers = csv_reader.fieldnames
        headers = [fieldname.strip() for fieldname in headers]
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)

#1. 이 파일에 flask 기본 틀을 추가한다.
#2. /에 접속 시 이 사용자의 데이터를 보여준다. 

@app.route("/")
def index():
    return render_template('page.html', users=csv_data)

@app.route("/<int:page>")
def page_loader(page=1): #페이지값 없을 때 대비하여 =1을 넣는다.
    per_page = 10 #한 페이지에 보여줄 항목 수

    totalpages = math.ceil(len(csv_data) / per_page)

    headers = csv_data[0]
    return render_template('page2.html', page=page, users=csv_data[(page-1)*per_page:page*per_page], totalpages=totalpages, headers=headers)


if __name__ == "__main__":
    load_csv_data('./user.csv')
    print(csv_data)
    print(headers)
    # app.run(debug=True)



