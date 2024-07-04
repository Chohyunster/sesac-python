from flask import Flask, Blueprint, render_template
import sqlite3, math
from database import get_query

app = Flask(__name__)

orderitems_app = Blueprint('orderitems', __name__)

DATABASE = './newcrmdb.db'

orderitem_data = []

def load_orderitem_data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM orderitems')
    orderitems = cur.fetchall()
    conn.close()
    for orderitem in orderitems:
        orderitem_data.append(orderitem)

load_orderitem_data(DATABASE)

@orderitems_app.route("/")
@orderitems_app.route("/<int:page>")
def index(page=1):

    per_page = 20
    totalpages = math.ceil(len(orderitem_data) / per_page)

    return render_template('orderitems/orderitems.html', page=page, orderitems=orderitem_data[(page-1)*per_page:page*per_page], totalpages=totalpages) 

@orderitems_app.route("/orderitem_detail/<id>")
def orderitem_detail(id):
    query = '''SELECT oi.Id AS orderitem_id, o.Id AS order_id, i.Id AS item_id, i.name AS item_name
            From orders o JOIN orderitems oi ON o.id = oi.OrderId
            JOIN items i ON oi.ItemId = i.Id
            WHERE o.id = ?'''
    orderitem_detail = get_query(query, (id, ))

    return render_template('orderitems/orderitemdetail.html', orderitem_detail=orderitem_detail)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

