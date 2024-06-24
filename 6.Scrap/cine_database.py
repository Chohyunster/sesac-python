
import sqlite3

my_db = 'movies.db'

def init_db():
    #테이블 생성 코드 추가
    conn = sqlite3.connect(my_db)
    cur = conn.cursor()
    cur.execute('''
                create table if not exists movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rank TEXT NOT NULL, title text not null,
                audience text not null,
                link text not null)''')
    conn.commit()

    return conn, cur #커넥션과 커서를 반납한다.

def save_to_db(conn, cur, rank, title, audience, link):
    cur.execute('''
                insert into movies (rank, title, audience, link) VALUES (?, ?, ?, ?)
                ''', (rank, title, audience, link))
    conn.commit()

def query_movie(cur):
    #영화 목록 모두다 출력하기
    cur.execute('SELECT rank, title, audience FROM movies')
    rows = cur.fetchall()
    for row in rows:
        print(f'순위: {row[0]}, 영화제목: {row[1]}, 관객수: {row[2]}')

def close_db(conn):
    #db 연결 종료함수
    conn.close()