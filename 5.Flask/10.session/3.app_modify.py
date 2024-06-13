from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'thisisanothersecret'

#사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},

]

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['password']

    # 이 사용자가 목록에 있는지 검사

    user = None 
    for u in users:
        if u['id'] == id and u['pw'] == pw:
            u = user

    #위에 것을 list comprehension으로 표현했을 떄:
    #user = next((u for u in users if u['id'] == id and u['pw'] == pw, None))

        if user:
            session['user'] = user 
            return redirect(url_for('profile'))
        else:
            return render_template('index.html', error='사용자 없음')

    #get 요청일 때는, 페이지를 보내줌    
    return render_template('index.html')

#미션1: profile에도 get하는데, post 할수 있어야 함.
@app.route('/profile', methods = ['GET', 'POST'])
def profile():
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
        return render_template('profile_3.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None) #세션에서 유저 정보 삭제
    return redirect(url_for('home')) #로그아웃 이후 홈 페이지로 보내주기 

if __name__ == '__main__':
    app.run(debug=True)