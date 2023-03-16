import os
import time

from flask import Flask
from flask import render_template, jsonify, request, make_response, redirect, url_for


app = Flask(__name__, template_folder='templates')

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
    
@app.route("/gta")
def gta():
    return "<p>gta key</p>"

@app.route("/travel")
def travel():
    if os.getcwd().find('GitHub') == -1:   # 路徑沒有GitHub字樣，代表在server上跑的。否則就是在local跑的
        dir_ = 'Might_Calculate/'
        t0 = time.time()
        t1 = t0 + 60*60*8   # GMT +8
        GMT8_time = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(t1))
        with open(dir_+'login_travel.txt', 'a') as f_write:
            f_write.write(GMT8_time + '\n')
    
    return render_template("travel.html")

@app.route('/form')
def formPage():
    return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        print(request.form)
        print(type(request.form))
        user = request.form['user']
        print("post : user => ", user)
        FLAG = 'False'
        dir_ = 'Might_Calculate/'
        
        # if user == '18c04d299e34':
            # FLAG = 'True'
            
        
        if user != '18c04d299e34':
            t0 = time.time()
            t1 = t0 + 60*60*8   # GMT +8
            GMT8_time = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(t1))
            with open(dir_+'login.txt', 'a') as f_write:
                f_write.write(user + ' | ' + GMT8_time)
                f_write.write('\n')
        
        with open(dir_+'mac.txt', 'r') as f:
            lines = f.readlines()
        for item in lines:
            if user == item.split('\n')[0]:
                FLAG = 'True'
                break
                
        if FLAG == 'False':
            with open(dir_+'new_user.txt', 'a') as f_write:
                f_write.write(user)
                f_write.write('\n')
            FLAG = 'True'        # 先開給Win11使用者使用，因為win11重新開機後，主機板碼都會一直變
        
        # time.sleep(2)
        return redirect(url_for('check', FLAG=FLAG))

@app.route('/check/<FLAG>')
def check(FLAG):
    return '{}'.format(FLAG)



@app.route("/Might/")
def Might():
    datas = ['1','2','3']
    return render_template("01.html", datas = datas)

@app.route("/chatgpt")
def chatgpt():
    return render_template("chatgpt.html")

@app.route("/travel_test")
def travel_test():
    return render_template("travel_test.html")

@app.route("/travel/<select_name>")
def travel_select_name(select_name):
    return render_template(select_name + ".html")

@app.route("/<id>")
def test(id):

    user_cookies = request.cookies.get('a', None)

    heros = []
    weapons = []
    dragons = []
    wps = []
    for file_name in os.listdir('Might_Calculate/static/img/adventure_tmp'):
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

    for file_name in os.listdir('Might_Calculate/static/img/weapon'):
        # name, hp, str, might = file_name.split('_')
        # might = might.split('.')[0]
        # hero = {
        #     'name':name,
        #     'hp':int(hp),
        #     'str':int(str),
        #     'might':int(might),
        #     'file_name':file_name
        # }
        weapons.append(file_name)
    
    for file_name in os.listdir('Might_Calculate/static/img/dragon'):
        # name, hp, str, might = file_name.split('_')
        # might = might.split('.')[0]
        # hero = {
        #     'name':name,
        #     'hp':int(hp),
        #     'str':int(str),
        #     'might':int(might),
        #     'file_name':file_name
        # }
        dragons.append(file_name)

    for file_name in os.listdir('Might_Calculate/static/img/wyrmprint'):
        # name, hp, str, might = file_name.split('_')
        # might = might.split('.')[0]
        # hero = {
        #     'name':name,
        #     'hp':int(hp),
        #     'str':int(str),
        #     'might':int(might),
        #     'file_name':file_name
        # }
        wps.append(file_name)
    resp = make_response(render_template(id+".html", heros=heros, weapons=weapons, dragons=dragons, wps=wps, user_cookies=user_cookies))

    if not user_cookies:
        resp.set_cookie(key='a', value='123')

    return resp

@app.route("/api/heros/<page>")
def get_heros(page):
    page = int(page)

    return jsonify()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)