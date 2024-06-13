from flask import Blueprint, render_template


#app = Flask(__name__) 
#admin = Flask(__name__) 이런거를 아래와 같이 만드는 것이다. 
admin_app = Blueprint('admin', __name__)

@admin_app.route('/')
def home():
    return render_template('/admin/index.html')


