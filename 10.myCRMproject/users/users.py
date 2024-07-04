from flask import Flask, Blueprint, render_template, request
from database import get_query
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
    
    
    return render_template('users/users.html', page=page, users=filtered_user[(page-1)*per_page:page*per_page], totalpages=totalpages, search_name=search_name, search_gender=search_gender) 
    
@users_app.route("/<id>")
def user_detail(id):
    query = "SELECT * FROM users WHERE id = ?"
    user = get_query(query, (id,))[0]

    query = '''SELECT o.Id AS orderid, o.OrderAt AS orderat, s.Id AS storeid
            From users u JOIN orders o ON u.Id = o.UserId
            JOIN stores s ON s.Id = o.StoreId
            WHERE u.Id = ?'''
    orderinfo = get_query(query, (id, ))

    query = '''SELECT s.name AS storename, COUNT(s.name) AS visits
            FROM users u
            JOIN orders o
            ON u.id = o.userid
            JOIN stores s
            ON o.storeid = s.id
            WHERE u.id = ?
            GROUP BY s.name ORDER BY visits DESC LIMIT 5            
            '''
    visitinfo = get_query(query, (id, ))

    query = '''SELECT i.name AS itemname, COUNT(i.name) AS frequency
            FROM users u 
            JOIN orders o ON u.id = o.userid
            JOIN orderitems oi ON o.id = oi.orderid
            JOIN items i ON oi.itemid = i.id
            WHERE u.id = ?
            GROUP BY i.name ORDER BY frequency DESC LIMIT 5
            '''
    iteminfo = get_query(query, (id, ))

    return render_template('users/userdetail.html', user=user, orderinfo=orderinfo, visitinfo=visitinfo, iteminfo=iteminfo)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

