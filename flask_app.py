from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Might/")
def Might():
    datas = ['1','2','3']
    return render_template("01.html", datas = datas)

@app.route("/<name>")
def test(name):
    return render_template(name+".html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)