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
            session['user'] = user #로그인한 사용자 정보를 세션에 저장
            # return '사용자 맞음'
            return redirect(url_for('profile'))
        else:
            return render_template('index.html', error='사용자 없음')

    #get 요청일 때는, 페이지를 보내줌    
    return render_template('index.html')

@app.route('/profile')
def profile():
    user = session.get('user') #위에서 내가 세션에 저장한 거 다시 찾아오기.
    # user = {'name': '무슨 이름', 'id' : '무슨 아이디', 'pw': '무슨 비번'}
    return render_template("profile.html")

@app.route('/logout')
def logout():
    session.pop('user', None) #세션에서 유저 정보 삭제
    return redirect(url_for('home')) #로그아웃 이후 홈 페이지로 보내주기 

if __name__ == '__main__':
    app.run(debug=True)