#FE + BE
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = './newcrmdb.db'

@app.route('/')
def index():
    #데이터베이스 연결해서 데이터 가져오기#
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores')  #WHERE name LIKE ?', ('스타벅스%', ) 이걸 붙이면 스타벅스 지점만 나온다.
    stores = cur.fetchall()
    conn.close()
    return render_template('index.html', stores=stores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

