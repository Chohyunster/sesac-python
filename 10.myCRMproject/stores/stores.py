from flask import Flask, Blueprint, render_template
import sqlite3, math
from database import get_query

app = Flask(__name__)

stores_app = Blueprint('stores', __name__)

DATABASE = './newcrmdb.db'

store_data = []

def load_store_data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores')
    stores = cur.fetchall()
    conn.close()
    for store in stores:
        store_data.append(store)

load_store_data(DATABASE)

@stores_app.route("/")
@stores_app.route("/<int:page>")
def index(page=1):

    per_page = 20
    totalpages = math.ceil(len(store_data) / per_page)

    return render_template('stores/stores.html', page=page, stores=store_data[(page-1)*per_page:page*per_page], totalpages=totalpages) 

@stores_app.route("/<id>")
def store_detail(id):
    query = "SELECT * FROM stores WHERE id = ?"
    store = get_query(query, (id,))[0]

    query = '''SELECT strftime('%Y-%m', o.OrderAt) AS yearmonth, COUNT(oi.id) AS count, SUM(i.unitprice) AS revenue
            FROM stores s
            JOIN orders o ON o.storeid = s.id
            JOIN orderitems oi ON oi.orderid = o.id
            JOIN items i ON oi.itemid = i.id
            WHERE s.id = ? GROUP BY yearmonth'''
    salesinfo = get_query(query, (id, ))


    query = '''SELECT u.id AS userid, u.name AS username, COUNT(u.id) AS frequency
            FROM stores s 
            JOIN orders o ON s.id = o.storeid
            JOIN users u ON o.userid = u.id
            WHERE s.id = ?
            GROUP BY u.id ORDER BY frequency DESC LIMIT 10'''
    regularinfo = get_query(query, (id, ))


    return render_template('stores/storedetail.html', store=store, regularinfo=regularinfo, salesinfo=salesinfo)
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

