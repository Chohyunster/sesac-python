#목표: BE와 FE 분리하기.
# 1. render_template 삭제한다
# 2. jsonify 로 변경한다
# 3. 모든 url경로를 "/api/xxxx" 으로 변경한다
# 4. 필요한 메소드들 정라하고 데이터 타입들 확인한다. (status, message, json/form 등등)
# 5. front-end (html) 코드를 작성한다. (static 폴더내에 index.html, profile.html)
# 6. fetch 로 요청한다.
# 7. 이때, CORS 라는 문제가 발생할 수 있음 (유투브 영상볼것)
# 8. 그래서, 7번 문제를 해결하고자 (임시방편으로) 다시 우리의 @app.route('/') 와 '/profile' 을 살렸음
# 9. FE 로 돌아가서 나머지 코드 작성할것

from flask import Flask, session, request, jsonify, send_from_directory
from flask import url_for, redirect

app = Flask(__name__)
app.secret_key = 'thisisanothersecret'

#사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},

]

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/api/login', methods = ['POST'])
def api_login():
    data = request.json
    id = data.get('id')
    pw = data.get('pw')
    # id = request.form['id']
    # pw = request.form['password']

    # 이 사용자가 목록에 있는지 검사

    user = None 
    for u in users:
        if u['id'] == id and u['pw'] == pw:
            u = user

    #위에 것을 list comprehension으로 표현했을 떄:
    #user = next((u for u in users if u['id'] == id and u['pw'] == pw, None))

        if user:
            session['user'] = user 
            return jsonify({'status': 'success', 'message': '로그인 성공'})
        else:
            return jsonify({'status': 'error', 'message' : '로그인 실패'})

    #get 요청일 때는, 페이지를 보내줌    
    # return render_template('index.html')

#미션1: profile에도 get하는데, post 할수 있어야 함.
@app.route('/api/profile', methods = ['GET', 'POST'])
def api_profile():
    user = session.get('user') 
    # print(user)

    #미션2: if POST 요청이 왔으면? 
    if request.method == 'POST':
        new_pw = request.form['new_password']

    #세션에서 user 정보 가져와서, 이것을 우리의 user DB에서 검색해서
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw  #pw를 변경한다.

        #나의 세션 정보 변경 (지금 안해도 됨)
        user['pw'] = new_pw
        session['user'] = user   

    #미션3: 사용자에게 성공결과 보낸다.
        # return render_template('profile_3.html', user=user, message = '비밀번호 변경 성공')
        return jsonify({'status': 'success', 'message': '비밀번호 변경 성공'})
    
    return jsonify({'status': 'success', 'user':user})
    

@app.route('/api/logout')
def api_logout():
    session.pop('user', None) #세션에서 유저 정보 삭제
    return jsonify({'status': 'success', 'message': 'logout 성공'})

if __name__ == '__main__':
    app.run(debug=True)