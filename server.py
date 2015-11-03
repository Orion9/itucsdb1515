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
import sponsorships
import country
import league
import team


from config import *
from flask import *
from passlib.hash import bcrypt

app = Flask(__name__)
app.secret_key = 'come_on_dude_it_is_a_secret'


# Create test user before #
@app.before_first_request
def create_user():
    user_info = user.User("test", "test@test.com", "test")
    user_info.add_user_to_db()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/people')
def show_people():
    person_obj = people.Person()
    people_data = person_obj.get_person_by_id()

    return render_template("people.html", people_data=people_data)

@app.route('/team')
def show_teams():
    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()
    return render_template("teams.html", team_data=team_data)


@app.route('/sponsorships')
def show_sponsorships():
    sponsorship_obj = sponsorships.Sponsorship()
    sponsorships_data = sponsorship_obj.get_sponsorship_by_id()

    return render_template("sponsorships.html", sponsorships_data=sponsorships_data)

@app.route('/countries')
def show_countries():
    return render_template("countries.html")

@app.route('/leagues')
def show_leagues():
    return render_template("leagues.html")

@app.route('/penalties')
def show_penalties():
    return render_template("penalties.html")


@app.route('/cities')
def show_cities():
    return render_template("cities.html")

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

    return render_template("manager/cities.html")

@app.route('/manage/countries', methods=['GET', 'POST'])
def manage_countries():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    
    country_obj = country.Country()
    country_data = country_obj.get_country_by_id()
    
    return render_template("manager/countries.html", country_data=country_data)

@app.route('/manage/leagues', methods=['GET', 'POST'])
def manage_leagues():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    
    league_obj = league.League()
    league_data = league_obj.get_league_by_id()

    return render_template("manager/leagues.html", league_data=league_data)

@app.route('/manage/people/<int:person_id>', methods=['GET', 'POST'])
def show_person(person_id):
    pass




@app.route('/manage/people', methods=['GET', 'POST'])
def manage_people():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    # Create empty person and get all data from db #
    person = people.Person()
    people_data = person.get_person_by_id()
    # Same for types and city objects #
    types_obj = people.PersonType()
    types_data = types_obj.get_person_type()

    city_obj = cities.City()
    cities_data = city_obj.get_city()

    return render_template("manager/people.html", people_data=people_data, types=types_data, cities=cities_data)


@app.route('/manage/sponsorships', methods=['GET', 'POST'])
def manage_sponsorships():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    # Create empty sponsorship and get all data from db #
    sponsorship = sponsorships.Sponsorship()
    sponsorships_data = sponsorship.get_sponsorship_by_id()

    return render_template("manager/sponsorships.html", sponsorships_data=sponsorships_data)


@app.route('/search', methods=['POST'])
def search():
    pass


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
    # Get request header #
    json_user_info = request.json

    # Convert it into user #
    user_info = user.User(
        user_alias=json_user_info['alias'],
        user_email=json_user_info['user_email'],
        user_pass=json_user_info['user_password']
    )

    # Add user to database #
    status = user_info.add_user_to_db()

    return jsonify({'result': status})


@app.route('/api/login', methods=['POST'])
def api_user_login():
    # Get request header #
    json_user_data = request.get_json()

    # Get user object #
    user_info = user.User(None, None, None, None)
    user_info.get_user(json_user_data['user_email'])

    # Check user credentials #
    if user_info is not None and user_info.password_hash is not None:
        if bcrypt.verify(json_user_data['user_password'], user_info.password_hash) is True:
            # Create session for user #
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
    # Pop session #
    session.pop('email', None)
    session.pop('logged_in', None)

    return jsonify({'result': 'success'})


###############################################################################################
# Data API                                                                                    #
# GETs your data in JSON format from the routes. It will be automatically processed.          #
# API access for Add, Update and Delete abilities is restricted to logged in users to         #
# prevent unauthorized access through API.                                                    #
#                                                                                             #
# Usage: (using curl lib)                                                                     #
#                                                                                             #
# curl http://localhost:5000/api/<route>/<id>                                                 #
###############################################################################################
@app.route('/api/search/<string:keywords>')
def api_db_search(keywords):
    pass

@app.route('/api/country', methods=['GET'])
def api_get_country_all():
    country_obj = country.Country()
    country_data = country_obj.get_country_by_id()
    country_json = json.dumps(country_data)

    return Response(country_json, mimetype="application/json")


@app.route('/api/league', methods=['GET'])
def api_get_league_all():
    league_obj = league.League()
    league_data = league_obj.get_league_by_id()
    league_json = json.dumps(league_data)

    return Response(league_json, mimetype="application/json")


@app.route('/api/person', methods=['GET'])
def api_get_person_all():
    # Create empty person then get all data from db #
    person = people.Person(None, None, None, None)
    people_data = person.get_person_by_id()
    # jsonify function does not work for arrays #
    people_json = json.dumps(people_data)

    # Return JSON response. #
    return Response(people_json, mimetype="application/json")


@app.route('/api/person/<int:data_id>', methods=['GET'])
def api_get_person(data_id):
    # Create empty person and fill it from db #
    person_obj = people.Person(None, None, None, None)
    person_obj.get_person_by_id(data_id)

    # Create a dict for jsonify #
    data = {
        'id': person_obj.id,
        'name': person_obj.name,
        'birth_date': person_obj.birth_date.strftime('%d/%m/%Y'),
        'birth_place': person_obj.birth_place
    }

    return jsonify(data)


@app.route('/api/person/add', methods=['POST'])
def api_add_person():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create an person object #
    person_info = people.Person(json_post_data['person_name'], json_post_data['person_birth_date'],
                                json_post_data['person_birth_place'], json_post_data['person_type'])

    # Add it to db and send result #
    result = person_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/country/add', methods=['POST'])
def api_add_country():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    
    country_info = country.Country(json_post_data['country_name'], json_post_data['country_population'])

    # Add it to db and send result #
    result = country_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/country/delete', methods=['POST'])
def api_delete_country():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    country_json = request.get_json()
    
    for country_id in country_json:
        country_obj = country.Country()
        country_obj.get_country_by_id(country_id)
        status = country_obj.delete_from_db()

    return jsonify({'result': status})


@app.route('/api/person/update', methods=['POST'])
def api_update_person():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get person from db #
    person_obj = people.Person()
    person_obj.get_person_by_id(json_data['person_id'])

    # Update person object's values #
    person_obj.name = json_data['person_name']
    person_obj.birth_date = json_data['person_birth_date']
    person_obj.birth_place = json_data['person_birth_place']
    person_obj.type = json_data['person_type']

    # Update db #
    result = person_obj.update_db()

    return jsonify({'result': result})


@app.route('/api/person/type/<int:type_id>', methods=['GET'])
def api_get_person_type(type_id):
    # Get person type #
    type_obj = people.PersonType()
    type_obj.get_person_type(type_id)
    # Create a dict #
    data = {
        'id': type_obj.id,
        'type': type_obj.type
    }

    return jsonify(data)


@app.route('/api/person/type/add', methods=['POST'])
def api_add_person_type():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create a person type object #
    type_info = people.PersonType(json_post_data['person_type'])
    # Add it to db #
    result = type_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/person/delete', methods=['POST'])
def api_delete_person():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False
    # Get request #
    person_id_json = request.get_json()
    # print(person_id_json)
    # Delete every requested id #
    for person_id in person_id_json:
        person_obj = people.Person(None, None, None, None)
        person_obj.get_person_by_id(person_id)
        # print(person_id)
        status = person_obj.delete_from_db()

    return jsonify({'result': status})


@app.route('/api/sponsorship', methods=['GET'])
def api_get_sponsorship_all():
    # Create empty sponsorship then get all data from db #
    sponsorship = sponsorships.Sponsorship()
    sponsorships_data = sponsorship.get_sponsorship_by_id()
    # jsonify function does not work for arrays #
    sponsorships_json = json.dumps(sponsorships_data)

    # Return JSON response. #
    return Response(sponsorships_json, mimetype="application/json")


@app.route('/api/sponsorship/<int:data_id>', methods=['GET'])
def api_get_sponsorship(data_id):
    # Create empty sponsorship and fill it from db #
    sponsorship_obj = sponsorships.Sponsorship()
    sponsorship_obj.get_sponsorship_by_id(data_id)

    # Create a dict for jsonify #
    data = {
        'id': sponsorship_obj.id,
        'name': sponsorship_obj.name,
        'start_date': sponsorship_obj.start_date.strftime('%d/%m/%Y'),
        'league': sponsorship_obj.league,
        'team': sponsorship_obj.team,
        'person': sponsorship_obj.person
    }

    return jsonify(data)


@app.route('/api/sponsorship/add', methods=['POST'])
def api_add_sponsorship():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create a sponsor object #
    sponsorship_info = sponsorships.Sponsorship(json_post_data['sponsorship_name'],
                                                json_post_data['sponsorship_start_date'],
                                                json_post_data['sponsorship_league'],
                                                json_post_data['sponsorship_team'],
                                                json_post_data['sponsorship_person'])

    # Add it to db and send result #
    result = sponsorship_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/sponsorship/delete', methods=['POST'])
def api_delete_sponsorship():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False
    # Get request #
    sponsorship_id_json = request.get_json()
    # print(sponsorship_id_json)
    # Delete every requested id #
    for sponsorship_id in sponsorship_id_json:
        sponsorship_obj = sponsorships.Sponsorship()
        sponsorship_obj.get_sponsorship_by_id(sponsorship_id)
        status = sponsorship_obj.delete_from_db()

    return jsonify({'result': status})


if __name__ == '__main__':
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        # Enable following line only if you need it. It will show call stack and so. #
        app.debug = True
        # Change this line according to your local db credentials #
        app.config['dsn'] = """user='postgres' password='password'
                               host='localhost' port=5432 dbname='itucsdb1515'"""

    PORT = int(os.getenv('VCAP_APP_PORT', '5000'))
    app.run(host='0.0.0.0', port=int(PORT))
