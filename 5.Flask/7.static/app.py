#tempaltes라는 폴더 안에, 렌더링을 원하는 HTML 파일의 템플릿을 둔다.
#static이라는 폴더 안에는 , 변경이 필요 없는, 최종 클라이언트에 주고 싶은 다양한 내용(img, css, js)을 넣어둔다.

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/admin')
def admin():
    #if 로그인 안한 사용자이면, 홈으로 돌려보내기
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)