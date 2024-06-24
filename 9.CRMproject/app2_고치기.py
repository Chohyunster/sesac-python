#FE, BE 분리하기
from flask import Flask, jsonify, request
import sqlite3
from database import get_stores_by_name, get_stores

app = Flask(__name__)

DATABASE = './newcrmdb.db'

#웹 서버를 대신해주는 코드임. (지금은 웹서버가 없으니..)
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/stores')
def api_stores():
    #데이터베이스 연결해서 데이터 가져오기#

    name = request.args.get('name')
    if name:
        stores = get_stores_by_name(name)
    else:
        stores = get_stores()

    return jsonify(stores)

def get_stores():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row #출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores')  #WHERE name LIKE ?', ('스타벅스%', ) 이걸 붙이면 스타벅스 지점만 나온다.
    stores = cur.fetchall()
    stores = [dict(row) for row in stores] #jsonify된 걸 dict로 인식 못하겠대서 이 줄을 넣음.
    conn.close()

    return jsonify(stores)

def get_stores_by_name(name):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row #출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores WHERE name LIKE ?', ('%' + name + '%', ))
    stores = cur.fetchall()
    stores = [dict(row) for row in stores] #jsonify된 걸 dict로 인식 못하겠대서 이 줄을 넣음.
    conn.close()

    return jsonify(stores)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

