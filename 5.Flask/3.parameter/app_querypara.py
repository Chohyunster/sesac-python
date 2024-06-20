from flask import Flask, jsonify, json
from flask import request

app = Flask(__name__)

users = [
    {'name' : 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name' : 'Alice', 'age': 30, 'phone': '666-666-666'},
    {'name' : 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name' : 'Charlie', 'age': 35, 'phone': '555-555-555'},
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')     #127.0.0.1:5000/search?name=xxx&age=xxx&phone=xxxx
def search():
    name_query = request.args.get('name')  #/search?q=phython
    age_query = request.args.get('age')
    phone_query = request.args.get('phone')
    result = users

#미션1. 위에 있는 users에서 query 구문이 name인 사람을 찾아서 출력하시오.
    if name_query:
        result = [u for u in users if name_query.lower() == u['name'].lower()]

#미션2. 나이도 검색하기

    if age_query:
        try:
            age_query = int(age_query)
            result = [u for u in result if age_query == u['age']]
        except ValueError:
            # return jsonify({'error': 'age paramter must be an interger'}), 400
            return json.dumps({'error': '나이는 숫자로 입력해야 합니다.'}, ensure_ascii=False), 400
        

#미션3. 전화번호 끝 4자리로 검색하기

    if phone_query:
        try:
            phone_query = int(phone_query)
            result = [u for u in result if phone_query == int(u['phone'][-3:])]
        except ValueError:
            return json.dumps({'error': '번호는 숫자로 입력해야 합니다.'}, ensure_ascii=False), 400
    

    print(result)

    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True)

