from flask import Flask, Blueprint, render_template
import sqlite3, math

app = Flask(__name__)

orders_app = Blueprint('orders', __name__)

DATABASE = './newcrmdb.db'

order_data = []

def load_order_data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    conn.close()
    for order in orders:
        order_data.append(order)

load_order_data(DATABASE)

@orders_app.route("/")
@orders_app.route("/<int:page>")
def index(page=1):

    per_page = 20
    totalpages = math.ceil(len(order_data) / per_page)

    return render_template('orders/orders.html', page=page, orders=order_data[(page-1)*per_page:page*per_page], totalpages=totalpages) 
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

