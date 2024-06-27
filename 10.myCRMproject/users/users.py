from flask import Flask, Blueprint, render_template, request
import sqlite3, math

app = Flask(__name__)

users_app = Blueprint('users', __name__)

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

load_user_data(DATABASE)

@users_app.route("/", methods=['POST', 'GET'])
@users_app.route("/<int:page>", methods=['POST', 'GET'])
def index(page=1):
    
    per_page = 20
    totalpages = math.ceil(len(user_data) / per_page)

    search_name = request.form.get('name')
    search_gender = request.form.get('gender')

    filtered_user = user_data

    if search_name:
        filtered_user = [u for u in filtered_user if search_name.lower() in u[1].lower()]

    if search_gender:
        filtered_user = [u for u in filtered_user if search_gender == u[2].lower()]
    
    
    return render_template('users/users.html', page=page, users=filtered_user[(page-1)*per_page:page*per_page], totalpages=totalpages) 
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

