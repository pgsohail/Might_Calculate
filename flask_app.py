from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/test/')
def test():
    datas = ['1','2','3']
    return render_template('index.html', datas = datas)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)