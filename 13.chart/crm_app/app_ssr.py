# ssr = server side rendering
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # 아래 data는 딕셔너리타입이다.
    data = {
        'labels' : ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06'],
        "revenue" : [797500, 401500, 665500, 66000, 569820, 245800],
        }
    
    return render_template('index_ssr.html', revenue=data)


if __name__ == "__main__":
    app.run(debug=True)