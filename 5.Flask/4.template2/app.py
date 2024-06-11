from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name' : 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name' : 'Alice', 'age': 30, 'phone': '666-666-666'},
    {'name' : 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name' : 'Charlie', 'age': 35, 'phone': '555-555-555'},
]


@app.route('/')
def main():
    return render_template("index.html", users=users)

@app.route("/user")
def get_user():
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    print(f"검색한 이름: {search_name}, 검색한 나이: {search_age}")

    filtered_user = users

    if search_name:   
        filtered_user = [u for u in filtered_user if search_name.lower() in u['name'].lower()]    

    if search_age:   
        filtered_user = [u for u in filtered_user if int(search_age) == u['age']]    

        return render_template("index.html", users = filtered_user)            


if __name__ == '__main__':
    app.run(debug=True)

