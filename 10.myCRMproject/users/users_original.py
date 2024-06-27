from flask import Flask, render_template, request, jsonify
import sqlite3, math

app = Flask(__name__)

DATABASE = './newcrmdb.db'

user_data = []

def load_user_data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    conn.close()
    for user in users:
        user_data.append(user)

@app.route('/')
def home():
    return jsonify(user_data)

@app.route("/users", methods=['POST', 'GET'])
@app.route("/users/<int:page>", methods=['POST', 'GET'])
def index(page=1):
    per_page = 10
    totalpages = math.ceil(len(user_data) / per_page)

    search_name = request.form.get('name')
    search_gender = request.form.get('gender')

    filtered_user = user_data

    if search_name:
        filtered_user = [u for u in filtered_user if search_name.lower() in u[1].lower()]

    if search_gender:
        filtered_user = [u for u in filtered_user if search_gender == u[2].lower()]
    
    
    return render_template('page.html', page=page, users=filtered_user[(page-1)*per_page:page*per_page], totalpages=totalpages) 
    

if __name__ == "__main__":
    load_user_data(DATABASE)
    app.run(host="0.0.0.0", debug=True)

