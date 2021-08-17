import os

from flask import Flask
from flask import render_template, jsonify, request, make_response


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Might/")
def Might():
    datas = ['1','2','3']
    return render_template("01.html", datas = datas)

@app.route("/<id>")
def test(id):

    user_cookies = request.cookies.get('a', None)

    heros = []
    for file_name in os.listdir('static/img/adventure_tmp'):
        name, hp, str, might = file_name.split('_')
        might = might.split('.')[0]
        hero = {
            'name':name,
            'hp':int(hp),
            'str':int(str),
            'might':int(might),
            'file_name':file_name
        }
        heros.append(hero)
    resp = make_response(render_template(id+".html", heros=heros, user_cookies=user_cookies))

    if not user_cookies:
        resp.set_cookie(key='a', value='123')

    return resp

@app.route("/api/heros/<page>")
def get_heros(page):
    page = int(page)

    return jsonify()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)