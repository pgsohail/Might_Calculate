import os
import time

from flask import Flask
from flask import render_template, jsonify, request, make_response, redirect, url_for, abort
from Crypto.Cipher import AES
import json
from traceback import format_exc
from datetime import datetime, timedelta
from base64 import b64encode, b64decode

app = Flask(__name__, template_folder='templates')

root_dir = '/home/m900054/Might_Calculate/'
VALID_VERSION_AND_DOWNLOAD_FILE = '/home/m900054/cyvisionbot/valid_version_and_download.json'

class Variables:
    def __init__(self):
        # GMT8_time_str = '202312071930'                      # 12 bytes
        # key_str = f'CY_VISION_BOT_1207_{GMT8_time_str}_'    # 32 bytes
        # self.key = key_str.encode(encoding='utf-8')
        self.header =           b'CY_VISION_BOT_HEADER_1207'
        self.PASS_MSG =          'CERTIFICATE_KEY_CHECK_PASSED____'
        self.FAIL_MSG =          'CERTIFICATE_KEY_CHECK_FAILED____'
        self.VERSION_ERROR_MSG = 'VERSION_CHECK_ERROR_____________'

    def get_now_key(self, now_time, retry=0):
        if retry == 0:
            GMT8_time = now_time
        elif retry == 1:
            GMT8_time = now_time - timedelta(minutes=1)
        else:
            GMT8_time = now_time + timedelta(minutes=1)
        GMT8_time_str = GMT8_time.strftime("%Y%m%d%H%M")
        key_str =  f'CY_VISION_BOT_1207_{GMT8_time_str}_'
        # self.key = key_str.encode(encoding='utf-8')
        return key_str.encode(encoding='utf-8')

my_var = Variables()

def encrypt_data(data:str) -> str:
    GMT8_time = datetime.utcnow() + timedelta(hours=8)
    now_key = my_var.get_now_key(now_time=GMT8_time)
    try:
        cipher = AES.new(now_key, AES.MODE_GCM)
        cipher.update(my_var.header)

        cipher_text, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        nonce = cipher.nonce

        # print(cipher_text, len(cipher_text))
        # print(tag)
        # print(nonce)

        encrypt_data = {}
        encrypt_data['1'] = b64encode(cipher_text).decode('utf-8')
        encrypt_data['2'] = b64encode(tag).decode('utf-8')
        encrypt_data['3'] = b64encode(nonce).decode('utf-8')
        post_json_str = json.dumps(encrypt_data)
        # print(post_json_str)
        return post_json_str

    except Exception as e:
        print(e)
        print(format_exc())
        print('Encrypt ERROR')

def decrypt_data(encrypt_json_str:str) -> str:
    GMT8_time = datetime.utcnow() + timedelta(hours=8)
    for i in range(3):
        now_key = my_var.get_now_key(now_time=GMT8_time, retry=i)            
        try:
            encrypt_dict = json.loads(encrypt_json_str)
            cipher_text = b64decode(encrypt_dict['1'])
            tag = b64decode(encrypt_dict['2'])
            nonce = b64decode(encrypt_dict['3'])
            decrypt_cipher = AES.new(now_key, AES.MODE_GCM, nonce=nonce)
            decrypt_cipher.update(my_var.header)
            plain_text = decrypt_cipher.decrypt_and_verify(cipher_text, tag)
            # print(plain_text.decode('utf-8'))
            return plain_text.decode('utf-8')
        except Exception as e:
            print(e)
            print(format_exc())
            print('Decrypt ERROR')


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

'''
@app.route('/submit', methods=['POST'])
def submit():
    #print(request.form)                 # ImmutableMultiDict([('user', '1027f5a0ad77'), ('status', 'login')])
    #print(type(request.form))           # <class 'werkzeug.datastructures.ImmutableMultiDict'>
    
    my_dict = request.form.to_dict()
    #print(my_dict)
    
    FLAG = 'False'
    dir_ = 'Might_Calculate/'
    
    
    if 'user' in my_dict.keys():
        user = my_dict['user']
        #print("post : user => ", user)
    else:
        user = 'None'
        #print('no user key')
        
    if 'status' in my_dict.keys():
        status = my_dict['status']
        #print("post : status => ", status)
    else:
        status = 'None'
        #print('no status key')
        
    if 'version' in my_dict.keys():
        version = my_dict['version']
        #print("post : version => ", version)
    else:
        version = 'None'
        #print('no version key')
        
    with open(dir_+'valid_version.txt', 'r') as f:
        valid_version_lines = f.readlines()
        
    version_check = False
    for line in valid_version_lines:
        if version == line.strip():
            version_check = True
        
    if version_check == False:
        print('version: ' + version)
        return redirect(url_for('check', FLAG='version_error'))
        
    print(f'user: {user}, status: {status}, version: {version}')
    
    
    
    # if user == '1027f5a0ad77':
        # FLAG = 'True'
        
    
    if user != '1027f5a0ad77':
        t0 = time.time()
        t1 = t0 + 60*60*8   # GMT +8
        GMT8_time = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(t1))
        with open(dir_+'login.txt', 'a') as f_write:
            f_write.write(user + ' | ' + GMT8_time + ' | ' + status)
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
        # FLAG = 'True'        # 先開給Win11使用者使用，因為win11重新開機後，mac addr都會一直變
    
    # time.sleep(2)
    return redirect(url_for('check', FLAG=FLAG))
'''

@app.route('/certificate_key_GTA_Auto_Play', methods=['POST'])
def certificate_key_GTA_Auto_Play():
    if request.is_json:
        json_str = request.get_json()
    else:
        abort(404)
    
    decrypt_json_str = decrypt_data(json_str)
    # print(decrypt_json_str, flush=True)
    if decrypt_json_str == None:
        abort(404)

    try:
        my_dict = json.loads(decrypt_json_str)
        # print(my_dict, flush=True)
    except:
        abort(404)

    with open(VALID_VERSION_AND_DOWNLOAD_FILE, 'r', encoding='utf-8') as f:
        version_dict = json.load(f)

    FLAG = my_var.FAIL_MSG
    
    login_file = 'login_GTA_Auto_Play.txt'
    mac_file = 'mac_GTA_Auto_Play.txt'
    new_user_file = 'new_user_GTA_Auto_Play.txt'
    valid_version_list = version_dict['GTA_Auto_Play']['VALID_VERSION']
    
    
    if 'user' in my_dict.keys():
        user = my_dict['user']
        #print("post : user => ", user)
    else:
        user = 'None'
        #print('no user key')
        
    if 'status' in my_dict.keys():
        status = my_dict['status']
        #print("post : status => ", status)
    else:
        status = 'None'
        #print('no status key')
        
    if 'version' in my_dict.keys():
        version = my_dict['version']
        #print("post : version => ", version)
    else:
        version = 'None'
        #print('no version key')
        
    
        
    
    if version in valid_version_list:
        pass
    else:
        # version_check = False
        print(f'version_check FAILED, version: {version}')
        # return redirect(url_for('check', FLAG=my_var.VERSION_ERROR_MSG))
        FLAG = my_var.VERSION_ERROR_MSG
        return encrypt_data(FLAG)
    
    print(f'user: {user}, status: {status}, version: {version}')
    
    
    if user != '1027f5a0ad77':
        t0 = time.time()
        t1 = t0 + 60*60*8   # GMT +8
        GMT8_time = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(t1))
        with open(root_dir + login_file, 'a') as f_write:
            f_write.write(user + ' | ' + GMT8_time + ' | ' + status)
            f_write.write('\n')
    
    with open(root_dir + mac_file, 'r') as f:
        lines = f.readlines()
    for item in lines:
        if user == item.split('\n')[0]:
            FLAG = my_var.PASS_MSG
            break
            
    if FLAG == my_var.FAIL_MSG:
        with open(root_dir + new_user_file, 'a') as f_write:
            f_write.write(user)
            f_write.write('\n')
        # FLAG = my_var.PASS_MSG        # 先開給Win11使用者使用，因為win11重新開機後，mac addr都會一直變
    
    # time.sleep(2)
    # return redirect(url_for('check', FLAG=FLAG))
    return encrypt_data(FLAG)


@app.route('/certificate_key_animal_restaurant', methods=['POST'])
def certificate_key_animal_restaurant():
    if request.is_json:
        json_str = request.get_json()
    else:
        abort(404)
    
    decrypt_json_str = decrypt_data(json_str)
    # print(decrypt_json_str, flush=True)
    if decrypt_json_str == None:
        abort(404)

    try:
        my_dict = json.loads(decrypt_json_str)
        # print(my_dict, flush=True)
    except:
        abort(404)

    with open(VALID_VERSION_AND_DOWNLOAD_FILE, 'r', encoding='utf-8') as f:
        version_dict = json.load(f)

    FLAG = my_var.FAIL_MSG
    
    login_file = 'login_animal.txt'
    mac_file = 'mac_animal.txt'
    new_user_file = 'new_user_animal.txt'
    valid_version_list = version_dict['Animal_Restaurant']['VALID_VERSION']
    
    
    if 'user' in my_dict.keys():
        user = my_dict['user']
        #print("post : user => ", user)
    else:
        user = 'None'
        #print('no user key')
        
    if 'status' in my_dict.keys():
        status = my_dict['status']
        #print("post : status => ", status)
    else:
        status = 'None'
        #print('no status key')
        
    if 'version' in my_dict.keys():
        version = my_dict['version']
        #print("post : version => ", version)
    else:
        version = 'None'
        #print('no version key')
        
    
        
    
    if version in valid_version_list:
        pass
    else:
        # version_check = False
        print(f'version_check FAILED, version: {version}')
        # return redirect(url_for('check', FLAG=my_var.VERSION_ERROR_MSG))
        FLAG = my_var.VERSION_ERROR_MSG
        return encrypt_data(FLAG)
    
    print(f'user: {user}, status: {status}, version: {version}')
    
    
    if user != '1027f5a0ad77':
        t0 = time.time()
        t1 = t0 + 60*60*8   # GMT +8
        GMT8_time = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(t1))
        with open(root_dir + login_file, 'a') as f_write:
            f_write.write(user + ' | ' + GMT8_time + ' | ' + status)
            f_write.write('\n')
    
    with open(root_dir + mac_file, 'r') as f:
        lines = f.readlines()
    for item in lines:
        if user == item.split('\n')[0]:
            FLAG = my_var.PASS_MSG
            break
            
    if FLAG == my_var.FAIL_MSG:
        with open(root_dir + new_user_file, 'a') as f_write:
            f_write.write(user)
            f_write.write('\n')
        # FLAG = my_var.PASS_MSG        # 先開給Win11使用者使用，因為win11重新開機後，mac addr都會一直變
    
    # time.sleep(2)
    # return redirect(url_for('check', FLAG=FLAG))
    return encrypt_data(FLAG)



@app.route('/check/<FLAG>')
def check(FLAG):
    # encrypt_str = encrypt_data(FLAG)
    # return encrypt_str
    return f'{FLAG}'



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