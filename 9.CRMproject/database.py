#app2.py에서 필요한 거 위에다가 갖다가 붙인다. 그러면 아래 두 함수는 분리해서 깨끗하게 파일을 만들 수 있음.

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