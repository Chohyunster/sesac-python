from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<HTML><BODY><H1>나의 헤딩ㅎㅎ</H1><P>my sentence here</P></BODY></HTML>"

@app.route("/user/")
@app.route("/user/<name>") #<name>은 변수임. user마다 페이지를 만들 수 없으니... -> 이 변수명과 함수의 인자를 매칭해서 내부에서 처리한다.
def user(name=None):
    username = name
    print(username)
    return f"""
        <HTML><BODY><H1>사용자 페이지: {username}님 안녕하세요.
        </H1><P>{username}님의 소개내용이 들아갑니다.</P></BODY></HTML>
        """

@app.route("/admin")
def admin():
    return "<HTML><BODY><H1>관리자페이지</H1><P>my sentence here</P></BODY></HTML>"

if __name__ == "__main__":
    app.run(port=5000, debug=True) #<중요>개발환경에서만 사용해야 함. 배포하는 production 에서는 debug는 항상 off여야 함.
