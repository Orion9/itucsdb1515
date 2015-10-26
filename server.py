###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

import datetime
import os
import json
import re
import user

from config import *
from flask import *
from passlib.hash import bcrypt

app = Flask(__name__)
app.secret_key = 'come_on_dude_it_is_a_secret'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/logout')
def logout():
    api_user_logout()
    return redirect(url_for('home'))


@app.route('/manage')
def manage():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    return render_template("manager/home.html")


# Auth API #
@app.route('/api/register', methods=['POST'])
def api_user_register():
    json_user_info = request.json
    user_info = user.User(
        user_alias=json_user_info['alias'],
        user_email=json_user_info['user_email'],
        user_pass=json_user_info['user_password']
    )

    conn = db_connect()
    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO users (user_name, password_hash, user_email, is_admin) VALUES (%s, %s, %s, %s);""",
                       (user_info.alias, user_info.password_hash, user_info.email, user_info.user_type))
        conn.commit()

        status = 'success'

    except conn.Error as error:
        print(error)
        status = 'user already there'

    cursor.close()
    conn.close()
    return jsonify({'result': status})


@app.route('/api/login', methods=['POST'])
def api_user_login():
    json_user_data = request.get_json()
    user_info = user.get_user(json_user_data['user_email'])

    if user_info is not None:
        if bcrypt.verify(json_user_data['user_password'], user_info[2]) is True:
            session['logged_in'] = True
            status = True
        else:
            status = False
    else:
        status = False

    return jsonify({'result': status})


@app.route('/api/logout')
def api_user_logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        # Enable following line only if you need it. It will show call stack and so.#
        app.debug=True
        # Change this line according to your local db credentials #
        app.config['dsn'] = """user='postgres' password='password'
                               host='localhost' port=5432 dbname='itucsdb1515'"""

    PORT = int(os.getenv('VCAP_APP_PORT', '5000'))
    app.run(host='0.0.0.0', port=int(PORT))
