###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

import user
import people
import cities
import sponsorships
import stadiums
import country
import league
import team
import player
import penalties


from config import *
from flask import *
from passlib.hash import bcrypt

app = Flask(__name__)
app.secret_key = 'come_on_dude_it_is_a_secret'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
    pass


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


@app.route('/people')
def show_people():
    person_obj = people.Person()
    people_data = person_obj.get_person_by_id()

    return render_template("people.html", people_data=people_data)


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
    cities_data = city_obj.get_city_by_id()

    # print(cities_data)

    return render_template("manager/people.html", people_data=people_data, types=types_data, cities=cities_data)


@app.route('/teams')
def show_teams():
    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()
    return render_template("teams.html", team_data=team_data)


@app.route('/manage/teams', methods=['GET', 'POST'])
def manage_teams():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()

    person_obj = people.Person()
    people_data = person_obj.get_person_by_id()

    return render_template("manager/teams.html", team_data=team_data, people=people_data)


@app.route('/sponsorships')
def show_sponsorships():
    sponsorship_obj = sponsorships.Sponsorship()
    sponsorships_data = sponsorship_obj.get_sponsorship_by_id()

    return render_template("sponsorships.html", sponsorships_data=sponsorships_data)


@app.route('/manage/sponsorships', methods=['GET', 'POST'])
def manage_sponsorships():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    # Create empty sponsorship and get all data from db #
    sponsorship = sponsorships.Sponsorship()
    sponsorships_data = sponsorship.get_sponsorship_by_id()

    league_obj = league.League()
    league_data = league_obj.get_league_by_id()

    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()

    person_obj = people.Person()
    people_data = person_obj.get_person_by_id()

    return render_template("manager/sponsorships.html", sponsorships_data=sponsorships_data, leagues=league_data, teams= team_data, people=people_data)


@app.route('/stadiums')
def show_stadiums():
    stadium_obj = stadiums.Stadium()
    stadiums_data = stadium_obj.get_stadium_by_id()

    return render_template("stadiums.html", stadiums_data=stadiums_data)


@app.route('/manage/stadiums', methods=['GET', 'POST'])
def manage_stadiums():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    # Create empty stadium and get all data from db #
    stadium = stadiums.Stadium()
    stadiums_data = stadium.get_stadium_by_id()

    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()

    city_obj = cities.City()
    cities_data = city_obj.get_city_by_id()

    return render_template("manager/stadiums.html", stadiums_data=stadiums_data, teams= team_data, cities=cities_data)


@app.route('/countries')
def show_countries():
    country_obj = country.Country()
    country_data = country_obj.get_country_by_id()

    return render_template("countries.html", country_data=country_data)


@app.route('/manage/countries', methods=['GET', 'POST'])
def manage_countries():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    country_obj = country.Country()
    country_data = country_obj.get_country_by_id()

    return render_template("manager/countries.html", country_data=country_data)


@app.route('/players')
def show_players():
    player_obj = player.Player()
    player_data = player_obj.get_player_by_id()

    return render_template("players.html", player_data=player_data)


@app.route('/manage/players', methods=['GET', 'POST'])
def manage_players():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    player_obj = player.Player()
    player_data = player_obj.get_player_by_id()

    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()

    return render_template("manager/players.html", player_data=player_data, team_data=team_data)


@app.route('/leagues')
def show_leagues():
    league_obj = league.League()
    league_data = league_obj.get_league_by_id()

    return render_template("leagues.html", league_data=league_data)


@app.route('/manage/leagues', methods=['GET', 'POST'])
def manage_leagues():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    league_obj = league.League()
    league_data = league_obj.get_league_by_id()

    country_obj = country.Country()
    country_data = country_obj.get_country_by_id()

    return render_template("manager/leagues.html", league_data=league_data, country_data=country_data)


@app.route('/penalties')
def show_penalties():
    return render_template("penalties.html")


@app.route('/manage/penalties', methods=['GET', 'POST'])
def manage_penalties():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    # Create empty person and get all data from db #
    person = people.Person()
    people_data = person.get_person_by_id()

    penalty = penalties.Penalty()
    penalties_data = penalty.get_penalty_by_id()

    # Same for types and city objects #
    types_obj = penalties.PenaltyType()
    types_data = types_obj.get_penalty_type()

    # print(cities_data)

    return render_template("manager/penalties.html", penalties_data=penalties_data,
                           people_data=people_data, types=types_data)


@app.route('/cities')
def show_cities():
    city_obj = cities.City()
    cities_data = city_obj.get_city_by_id()
    return render_template("cities.html", cities_data=cities_data)


@app.route('/manage/cities', methods=['GET', 'POST'])
def manage_cities():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))

    city_obj = cities.City()
    cities_data = city_obj.get_city_by_id()
    return render_template("manager/cities.html", cities_data=cities_data)


@app.route('/manage/users', methods=['GET', 'POST'])
def manage_users():
    if not session.get('logged_in'):
        flash("Unauthorized Access. Please identify yourself")
        return redirect(url_for('home'))
    return render_template("manager/users.html")


@app.route('/manage/users/<int:user_id>', methods=['GET', 'POST'])
def show_user(user_id):
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
    user_info = user.User()
    user_info.get_user(json_user_data['user_email'])

    # Check user credentials #
    if user_info is not None and user_info.password_hash is not None:
        if bcrypt.verify(json_user_data['user_password'], user_info.password_hash) is True:
            # Create session for user #
            session['logged_in'] = True
            session['email'] = json_user_data['user_email']
            session['alias'] = user_info.alias

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
    session.pop('alias', None)

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


# PERSON - start #
@app.route('/api/person', methods=['GET'])
def api_get_person_all():
    # Create empty person then get all data from db #
    person = people.Person()
    people_data = person.get_person_by_id()
    # jsonify function does not work for arrays #
    people_json = json.dumps(people_data)

    # Return JSON response. #
    return Response(people_json, mimetype="application/json")


@app.route('/api/person/<int:data_id>', methods=['GET'])
def api_get_person(data_id):
    # Create empty person and fill it from db #
    person_obj = people.Person()
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
        person_obj = people.Person()
        person_obj.get_person_by_id(person_id)
        # print(person_id)
        status = person_obj.delete_from_db()

    return jsonify({'result': status})
# PERSON - end #


# Penalties API - Begin #
@app.route('/api/penalty', methods=['GET'])
def api_get_penalty_all():
    # Create empty person then get all data from db #
    penalty = penalties.Penalty()
    penalties_data = penalty.get_penalty_by_id()
    # jsonify function does not work for arrays #
    penalty_json = json.dumps(penalties_data)

    # Return JSON response. #
    return Response(penalty_json, mimetype="application/json")


@app.route('/api/penalty/<int:data_id>', methods=['GET'])
def api_get_penalty(data_id):
    # Create empty person and fill it from db #
    penalty_obj = penalties.Penalty()
    penalty_obj.get_penalty_by_id(data_id)

    # Create a dict for jsonify #
    data = {
        'id': penalty_obj.id,
        'person': penalty_obj.person,
        'given_date': penalty_obj.given_date.strftime('%d/%m/%Y'),
        'penalty_type': penalty_obj.type
    }

    return jsonify(data)


@app.route('/api/penalty/add', methods=['POST'])
def api_add_penalty():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create an person object #
    penalty_info = penalties.Penalty(json_post_data['person_name'], json_post_data['penalty_given_date'],
                                     json_post_data['penalty_type'])

    # Add it to db and send result #
    result = penalty_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/penalty/update', methods=['POST'])
def api_update_penalty():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get person from db #
    penalty_obj = penalties.Penalty()
    penalty_obj.get_penalty_by_id(json_data['penalty_id'])

    # Update person object's values #
    penalty_obj.person = json_data['person_name']
    penalty_obj.given_date = json_data['penalty_given_date']
    penalty_obj.type = json_data['penalty_type']

    # Update db #
    result = penalty_obj.update_db()

    return jsonify({'result': result})


@app.route('/api/penalty/type/<int:type_id>', methods=['GET'])
def api_get_penalty_type(type_id):
    # Get person type #
    type_obj = penalties.PenaltyType()
    type_obj.get_penalty_type(type_id)
    # Create a dict #
    data = {
        'id': type_obj.id,
        'type': type_obj.type
    }

    return jsonify(data)


@app.route('/api/penalty/type/add', methods=['POST'])
def api_add_penalty_type():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create a person type object #
    type_info = penalties.PenaltyType(json_post_data['penalty_type'])
    # Add it to db #
    result = type_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/penalty/delete', methods=['POST'])
def api_delete_penalty():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False
    # Get request #
    penalty_id_json = request.get_json()
    # print(person_id_json)
    # Delete every requested id #
    for penalty_id in penalty_id_json:
        penalty_obj = penalties.Penalty()
        penalty_obj.get_penalty_by_id(penalty_id)
        # print(person_id)
        status = penalty_obj.delete_from_db()

    return jsonify({'result': status})
# Penalties API - End  #


# Cities Begin #
@app.route('/api/city/<int:city_id>', methods=['GET'])
def api_get_city(city_id):
    # Create empty city and fill it from db #
    city_obj = cities.City()
    city_obj.get_city_by_id(city_id)

    # Create a dict for jsonify #
    data = {
        'id': city_obj.id,
        'city_name': city_obj.name,
        'city_coordinates': city_obj.name,
        'city_population': city_obj.name
    }

    return jsonify(data)


@app.route('/api/city/add', methods=['POST'])
def api_add_city():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_post_data = request.get_json()
    # print(json_post_data)

    city_info = cities.City(json_post_data['city_name'],
                            json_post_data['city_population'])
    # Add it to db #
    result = city_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/city/update', methods=['POST'])
def api_update_city():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get city from db #
    city_obj = cities.City()
    city_obj.get_city_by_id(json_data['city_id'])

    # Update city object's values #
    city_obj.name = json_data['city_name']
    city_obj.population = json_data['city_population']

    # Update db #
    result = city_obj.update_db()

    return jsonify({'result': result})


@app.route('/api/city/delete', methods=['POST'])
def api_delete_city():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False

    # Get request #
    city_id_json = request.get_json()

    for city_id in city_id_json:
        city_obj = cities.City()
        city_obj.get_city_by_id(city_id)
        status = city_obj.delete_from_db()

    return jsonify({'result': status})
# Cities end #


# TEAM - start #
@app.route('/api/team', methods=['GET'])
def api_get_team_all():
    team_obj = team.Team()
    team_data = team_obj.get_team_by_id()
    team_json = json.dumps(team_data)

    return Response(team_json, mimetype="application/json")


@app.route('/api/team/<int:team_id>', methods=['GET'])
def api_get_team(team_id):
    # Create empty team and fill it from db #
    team_obj = team.Team()
    team_obj.get_team_by_id(team_id)

    # Create a dict for jsonify #
    data = {
        'id': team_obj.id,
        'team_name': team_obj.name,
        'team_couch': team_obj.couch,
    }

    return jsonify(data)


@app.route('/api/team/add', methods=['POST'])
def api_add_team():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create a team type object #
    team_info = team.Team(json_post_data['team_name'], json_post_data['team_couch'])
    # Add it to db #
    result = team_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/team/delete', methods=['POST'])
def api_delete_team():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False

    # Get request #
    team_id_json = request.get_json()

    for team_id in team_id_json:
        team_obj = team.Team()
        team_obj.get_team_by_id(team_id)
        status = team_obj.delete_from_db()
    return jsonify({'result': status})


@app.route('/api/team/update', methods=['POST'])
def api_update_team():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get team from db #
    team_obj = team.Team()
    team_obj.get_team_by_id(json_data['team_id'])

    # Update team object's data values #
    team_obj.name = json_data['team_name']
    team_obj.couch = json_data['team_couch']

    # Update db #
    result = team_obj.update_db()

    return jsonify({'result': result})
# TEAM - end #


# SPONSORSHIP - start #


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


@app.route('/api/sponsorship/update', methods=['POST'])
def api_update_sponsorship():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get sponsorship from db #
    sponsorship_obj = sponsorships.Sponsorship()
    sponsorship_obj.get_sponsorship_by_id(json_data['sponsorship_id'])

    # Update sponsorship object's values #
    sponsorship_obj.name = json_data['sponsorship_name']
    sponsorship_obj.start_date = json_data['sponsorship_start_date']
    sponsorship_obj.league = json_data['sponsorship_league']
    sponsorship_obj.team = json_data['sponsorship_team']
    sponsorship_obj.person = json_data['sponsorship_person']

    # Update db #
    result = sponsorship_obj.update_db()

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
# SPONSORSHIP - end #


# STADIUM - start #
@app.route('/api/stadium', methods=['GET'])
def api_get_stadium_all():
    # Create empty stadium then get all data from db #
    stadium = stadiums.Stadium()
    stadiums_data = stadium.get_stadium_by_id()
    # jsonify function does not work for arrays #
    stadiums_json = json.dumps(stadiums_data)

    # Return JSON response. #
    return Response(stadiums_json, mimetype="application/json")


@app.route('/api/stadium/<int:data_id>', methods=['GET'])
def api_get_stadium(data_id):
    # Create empty stadium and fill it from db #
    stadium_obj = stadiums.Stadium()
    stadium_obj.get_stadium_by_id(data_id)

    # Create a dict for jsonify #
    data = {
        'id': stadium_obj.id,
        'name': stadium_obj.name,
        'team': stadium_obj.team,
        'location': stadium_obj.location,
        'capacity': stadium_obj.capacity
    }

    return jsonify(data)


@app.route('/api/stadium/add', methods=['POST'])
def api_add_stadium():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    # print(json_post_data)
    # Create a sponsor object #
    stadium_info = stadiums.Stadium(json_post_data['stadium_name'],
                                    json_post_data['stadium_team'],
                                    json_post_data['stadium_location'],
                                    json_post_data['stadium_capacity'])

    # Add it to db and send result #
    result = stadium_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/stadium/update', methods=['POST'])
def api_update_stadium():
    # Get request from AJAX #
    json_data = request.get_json()
    # Get stadium from db #
    stadium_obj = stadiums.Stadium()
    stadium_obj.get_stadium_by_id(json_data['stadium_id'])

    # Update stadium object's values #
    stadium_obj.name = json_data['stadium_name']
    stadium_obj.team = json_data['stadium_team']
    stadium_obj.location = json_data['stadium_location']
    stadium_obj.capacity = json_data['stadium_capacity']

    # Update db #
    result = stadium_obj.update_db()

    return jsonify({'result': result})


@app.route('/api/stadium/delete', methods=['POST'])
def api_delete_stadium():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    status = False
    # Get request #
    stadium_id_json = request.get_json()
    # print(stadium_id_json)
    # Delete every requested id #
    for stadium_id in stadium_id_json:
        stadium_obj = stadiums.Stadium()
        stadium_obj.get_stadium_by_id(stadium_id)
        status = stadium_obj.delete_from_db()

    return jsonify({'result': status})
# STADIUM - end #


# COUNTRY - start #
@app.route('/api/country', methods=['GET'])
def api_get_country_all():
    # Creates an empty Country object
    country_obj = country.Country()
    # Transfers All Country Rows to country_data
    country_data = country_obj.get_country_by_id()
    country_json = json.dumps(country_data)

    return Response(country_json, mimetype="application/json")


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
    # Deletes every object in the request from database
    status = False
    for country_id in country_json:
        country_obj = country.Country()
        country_obj.get_country_by_id(country_id)
        status = country_obj.delete_from_db()

    return jsonify({'result': status})


@app.route('/api/country/update', methods=['POST'])
def api_update_country():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_data = request.get_json()

    country_obj = country.Country()
    country_obj.get_country_by_id(json_data['country_id'])

    # Update country values #
    country_obj.name = json_data['country_name']
    country_obj.population = json_data['country_population']

    # Update #
    result = country_obj.update_db()

    return jsonify({'result': result})
# COUNTRY - end #


# LEAGUE - start #
@app.route('/api/league', methods=['GET'])
def api_get_league_all():
    league_obj = league.League()
    league_data = league_obj.get_league_by_id()
    league_json = json.dumps(league_data)

    return Response(league_json, mimetype="application/json")


@app.route('/api/league/add', methods=['POST'])
def api_add_league():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    league_info = league.League(json_post_data['league_name'], json_post_data['league_country'],
                                json_post_data['league_start_date'])

    # Add it to db and send result #
    result = league_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/league/delete', methods=['POST'])
def api_delete_league():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    league_json = request.get_json()
    # Deletes every object in the request from database
    status = False
    for league_id in league_json:
        league_obj = league.League()
        league_obj.get_league_by_id(league_id)
        status = league_obj.delete_from_db()

    return jsonify({'result': status})


@app.route('/api/league/update', methods=['POST'])
def api_update_league():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_data = request.get_json()

    league_obj = league.League()
    league_obj.get_league_by_id(json_data['league_id'])

    # Update values #
    league_obj.name = json_data['league_name']
    league_obj.country = json_data['league_country']
    league_obj.start_date = json_data['league_start_date']

    # Update db #
    result = league_obj.update_db()

    return jsonify({'result': result})
# LEAGUE - end #

# Players - start #
@app.route('/api/player', methods=['GET'])
def api_get_player_all():
    player_obj = player.Player()
    player_data = player_obj.get_player_by_id()
    player_json = json.dumps(player_data)

    return Response(player_json, mimetype="application/json")


@app.route('/api/player/add', methods=['POST'])
def api_add_player():
    # Prevent unauthorized access from API #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get json request from AJAX Handler #
    json_post_data = request.get_json()
    player_info = player.Player(json_post_data['player_name'], json_post_data['player_team'],
                                json_post_data['player_goals'])

    # Add it to db and send result #
    result = player_info.add_to_db()

    return jsonify({'result': result})


@app.route('/api/player/delete', methods=['POST'])
def api_delete_player():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    player_json = request.get_json()
    # Deletes every object in the request from database
    status = False
    for player_id in player_json:
        player_obj = player.Player()
        player_obj.get_player_by_id(player_id)
        status = player_obj.delete_from_db()

    return jsonify({'result': status})


@app.route('/api/player/update', methods=['POST'])
def api_update_player():
    # Prevent unauthorized access #
    if not session.get('logged_in'):
        return jsonify({"result": "Unauthorized Access. Please identify yourself"})

    # Get request #
    json_data = request.get_json()

    player_obj = player.Player()
    player_obj.get_player_by_id(json_data['player_id'])

    # Update values #
    player_obj.name = json_data['player_name']
    player_obj.team = json_data['player_team']
    player_obj.goals = json_data['player_goals']

    # Update db #
    result = player_obj.update_db()

    return jsonify({'result': result})
# Players end #

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
