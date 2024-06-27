from flask import Flask, render_template
from admin.admin import admin_app
from users.users import users_app
from orders.orders import orders_app
from orderitems.orderitems import orderitems_app
from items.items import items_app
from stores.stores import stores_app

app = Flask(__name__)

app.register_blueprint(admin_app, url_prefix='/admin')
app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(orders_app, url_prefix='/orders')
app.register_blueprint(orderitems_app, url_prefix='/orderitems')
app.register_blueprint(items_app, url_prefix='/items')
app.register_blueprint(stores_app, url_prefix='/stores')

@app.route('/')
def home():
    return render_template('/admin/admin.html')

if __name__ == "__main__":
    app.run(debug=True)

