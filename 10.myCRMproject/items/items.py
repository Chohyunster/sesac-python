from flask import Flask, Blueprint, render_template
import sqlite3, math

app = Flask(__name__)

items_app = Blueprint('items', __name__)

DATABASE = './newcrmdb.db'

item_data = []

def load_item_data(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    items = cur.fetchall()
    conn.close()
    for item in items:
        item_data.append(item)

load_item_data(DATABASE)

@items_app.route("/")
@items_app.route("/<int:page>")
def index(page=1):

    per_page = 10
    totalpages = math.ceil(len(item_data) / per_page)

    return render_template('items/items.html', page=page, items=item_data[(page-1)*per_page:page*per_page], totalpages=totalpages) 
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

