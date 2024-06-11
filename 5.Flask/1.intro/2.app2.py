from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello" 

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}님!"

@app.route('/user/<int:age>')
def userage(age):
    return f"age: {age}"

@app.route('/user/<float:weight>')
def userweight(weight):
    return f"Weight: {weight}"

@app.route('/user/<name>/<int:age>')
def usernameage(name, age):
    return f"Hello, {name}님, age는 {age}입니다"

@app.route('/user/<name>/<int:age>/<float:weight>')
def usernameageweight(name, age, weight):
    return f"Hello, {name}님, age는 {age}, weight는 {weight}입니다"

if __name__ == "__main__":
    app.run(port=5000, debug=True) 

