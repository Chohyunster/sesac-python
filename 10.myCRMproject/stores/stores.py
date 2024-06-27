from flask import Flask, Blueprint, render_template
import sqlite3, math

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
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

