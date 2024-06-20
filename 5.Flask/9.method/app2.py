from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    return "<h1>정보제공</h1>"

@app.route('/user', methods=['POST'])
def post_user():
    return "<h1>요청에 의한 데이터 생성</h1>"

@app.route('/user', methods=['DELETE'])
def delete_user():
    return "<h1>요청에 의한 데이터 삭제</h1>"

if __name__ == "__main__":
    app.run(debug=True)


#cmd 창에서 curl 127.0.0.1:5000/user -X GET/POST/DELETE 이런 것들 쳐보기