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
import people
import cities

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
    return render_template("manager/main.html")


@app.route('/manage/users', methods=['GET', 'POST'])
def manage_users():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    return render_template("manager/users.html")


@app.route('/manage/users/<int:user_id>', methods=['GET', 'POST'])
def show_user(user_id):
    pass


@app.route('/manage/penalties', methods=['GET', 'POST'])
def manage_penalties():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    return render_template("manager/penalties.html")


@app.route('/manage/penalties/<int:penalty_id>', methods=['GET', 'POST'])
def show_penalty(penalty_id):
    pass


@app.route('/manage/cities', methods=['GET', 'POST'])
def manage_cities():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    people_json = api_get_person_all()
    return render_template("manager/cities.html")


@app.route('/manage/people/<int:person_id>', methods=['GET', 'POST'])
def show_person(person_id):
    pass


@app.route('/manage/people', methods=['GET', 'POST'])
def manage_people():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    api_response = api_get_person_all()

    person = people.Person(None, None, None, None)
    people_data = person.get_person_by_id()

    types_data = people.get_person_types()
    city_obj = cities.City(None)
    cities_data = city_obj.get_city()

    return render_template("manager/people.html", people_data=people_data, types=types_data, cities=cities_data)


# API START #
@app.route('/api')
def api_welcome_screen():
    data = {"welcome_message": "Welcome to the DBall API v1.0"}
    return jsonify(data)


###############################################################################################
# Auth API                                                                                    #
# Send your data in JSON format                                                               #
# to the routes. It will be automatically                                                     #
# processed.                                                                                  #
#                                                                                             #
# Usage: (using curl lib)                                                                     #
#                                                                                             #
# curl -H "Accept: application/json" -H "Content-type: application/json"                      #
# -X POST -d '{"alias": "testuser", "user_email": "test@test.com", "user_password": "test"}'  #
# http://localhost:5000/api/register                                                          #
###############################################################################################
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
        cursor.execute(
            """INSERT INTO users (user_name, password_hash, user_email, is_admin) VALUES (%s, %s, %s, %s);""",
                       (user_info.alias, user_info.password_hash, user_info.email, user_info.user_type)
        )
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
            session['email'] = json_user_data['user_email']

            status = True
        else:
            status = False
    else:
        status = False

    return jsonify({'result': status})


@app.route('/api/logout')
def api_user_logout():
    session.pop('email', None)
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


###############################################################################################
# Data API                                                                                    #
# GETs your data in JSON format to the routes. It will be automatically processed.            #
#                                                                                             #
# Usage: (using curl lib)                                                                     #
#                                                                                             #
#  curl http://localhost:5000/api/<route>/<id>                                                #
###############################################################################################
@app.route('/api/person', methods=['GET'])
def api_get_person_all():
    person = people.Person(None, None, None, None)
    people_data = person.get_person_by_id()
    people_json = json.dumps(people_data)
    return Response(people_json, mimetype="application/json")


@app.route('/api/person/<int:data_id>', methods=['GET'])
def api_get_person(data_id):
    person_obj = people.Person(None, None, None, None)
    person_obj.get_person_by_id(data_id)
    data = {
        'id': person_obj.id,
        'name': person_obj.name,
        'birth_date': person_obj.birth_date.strftime('%d/%m/%Y'),
        'birth_place': person_obj.birth_place
    }

    return jsonify(data)


@app.route('/api/person/add', methods=['POST'])
def api_add_person():
    if not session.get('logged_in'):
        return jsonify({"result":  "Unauthorized Access. Please identify yourself"})

    json_post_data = request.get_json()
    # print(json_post_data)
    person_info = people.Person(json_post_data['person_name'], json_post_data['person_birth_date'],
                                json_post_data['person_birth_place'], json_post_data['person_type'])

    result = person_info.add_to_db()
    return jsonify({'result': result})


@app.route('/api/person/delete', methods=['POST'])
def api_delete_person():
    if not session.get('logged_in'):
        return jsonify({"result":  "Unauthorized Access. Please identify yourself"})

    status = False
    person_id_json = request.get_json()
    print(person_id_json)
    for person_id in person_id_json:
        person_obj = people.Person(None, None, None, None)
        person_obj.get_person_by_id(person_id)
        print(person_id)
        status = person_obj.delete_from_db()

    return jsonify({'result': status})


if __name__ == '__main__':
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        # Enable following line only if you need it. It will show call stack and so.#
        app.debug = True
        # Change this line according to your local db credentials #
        app.config['dsn'] = """user='postgres' password='password'
                               host='localhost' port=5432 dbname='itucsdb1515'"""

    PORT = int(os.getenv('VCAP_APP_PORT', '5000'))
    app.run(host='0.0.0.0', port=int(PORT))
