import sqlite3

# 사용자 DB
DATABASE = './newcrmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # 행을 sqlite3.Row 라는 객체 타입으로 반환
                                   # 이걸 설정하면 각 Row의 결과는 Dict 유형으로 반환됨.
    return conn

def get_query(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    result = cur.fetchall()
    # result = [dict(row) for row in result] 위에서 이미 dict 타입으로 받았으므로 넣어주지 않아도 되는 것인가???
    conn.close()
    return result

# def execute_query(query, params):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute(query, params)
#     conn.commit()
#     conn.close()

# def init_db():
#     conn = get_db_connection()
#     cur = conn.cursor()

#     # 데이터 조회
#     cur.execute('SELECT * FROM users')
#     rows = cur.fetchall()

#     print('-' * 30)
#     for row in rows:
#         print(row['id'], row['username'], row['password']) # 열 이름을 사용(Dict) 해서 접근 가능함
#     print('-' * 30)

#     conn.close()