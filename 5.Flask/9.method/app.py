from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},

]

@app.route('/', methods=['POST', 'GET']) #post 방식에서 입력하는 것은 바디라는 영역으로 들어간다.
def home():
    # id = request.args.get('id') #이것은 get방식의 URL 파라미터를 처리할때만 가능하다.!
    
    if request.method == 'POST':
        id = request.form['id'] #여기는 post방식에서 form-data를 처리할 때 payload를 받아오는 방법
        pw = request.form['password']
        # print(f'입력한아이디: {id}, 입력한pw: {pw}')

    #위에있는 유저스 목록과 입력한 아이디패스워드 비교해서 print로 로그인 허용할건가 말건가 구현하기
        user = None
        for u in users:
            if u['id'] == id and u['pw'] == pw:
                print('매치되는 사용자가 있음')
                user = u

                #위 5줄짜리 코드를 1줄로 짜기
                #next()사용
                #user = next((user for user in users if user['id'] == id and user['pw'] == pw), None)

        if user:
            print(f'로그인한 사용자는 {user["name"]}입니다.')
            # return f'로그인 성공! {user["name"]}'
        
        else:
            print(f'로그인 가능한 사용자가 없습니다. id = {id}')
            message = '로그인 실패패'
            # return f'로그인 실패!'
        
        #위 내용을 아래 HTML에 전달하시오.
        return render_template('index.html', user=user)
    
    #메소드가 GET일 때 리턴값
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)