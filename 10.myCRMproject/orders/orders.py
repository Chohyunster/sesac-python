from flask import Flask, Blueprint, render_template
import sqlite3, math
from database import get_query

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
    
@orders_app.route('/<id>')
def order_detail(id):
    # query = '''SELECT o.id AS order_id, orderat AS order_at, storeid AS store_id, userid AS user_id
    # FROM orders o
    # WHERE o.id = ?'''
    # order_detail = get_query(query, (id, ))

    query = '''SELECT o.id AS order_id, oi.Id AS orderitem_id, o.orderat AS order_at, o.storeid AS store_id, o.userid AS user_id, i.Id AS item_id, i.name AS item_name
    FROM orders o
    JOIN orderitems oi ON o.id = oi.OrderId
    JOIN items i ON oi.ItemId = i.Id
    WHERE o.id = ?'''
    order_detail = get_query(query, (id, ))


    # query = '''SELECT oi.Id AS orderitem_id, o.Id AS order_id, i.Id AS item_id, i.name AS item_name
    #         From orders o JOIN orderitems oi ON o.id = oi.OrderId
    #         JOIN items i ON oi.ItemId = i.Id
    #         WHERE o.id = ?'''
    # item_order_info = get_query(query, (id, ))

    return render_template('orders/orderdetail.html', order_detail=order_detail)
# , item_order_info=item_order_info)

if __name__ == "__main:__":
    app.run(host="0.0.0.0", debug=True)

