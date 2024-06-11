from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/user')
@app.route('/user/<name>')
def user(name=""):   #none은 없는 거고, ""은 빈 값
    friends = ['bill', 'steve', 'larry']
    return render_template("user.html", username=name, content=friends) #앞 네임은 html에서 지정할 변수명, 뒤 네임은 인자값

@app.route('/admin')
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)