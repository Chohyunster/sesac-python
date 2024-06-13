from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'thisisascret' #아무 문자열이나 쓰면 도기ㅗ, 이게 실제로 세션데이터를 저장하는 암호키로 사용됨. 

@app.route('/')
def index():
    #세션에 데이터 저장하기 
    session['username'] = 'user1234' 
    session['data'] = '1234'
    return '헬로우'


@app.route('/get_session')
def get_session_data():
    username = session.get('username', '없음')
    data = session.get('data', '데이터도없음')

    return f'사용자이름: {username}, 사용자데이터: {data}'

if __name__ == "__main__":
    app.run(debug=True)