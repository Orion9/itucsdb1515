Parts Implemented by Oğuz Kerem Tural
=====================================
Front End Design
----------------
Application user interface uses Bootstrap framework for responsive UI, jQuery framework for much more dynamic design and
DataTables framework for glorious tables. Main aim for the design was simplicity. Any type of user could easily use the
application without losing its way. Thus, color scheme selection and content placement has been done accordingly.
On top of the Bootstrap, a hand written CSS file has been added to extend both its responsivity and design.

Different enhancements has been applied on both *front body* and *manager body* classes. *Pagination* has been fixed, columns
in front page has been hidden in *smaller screens*. Also **navigation bar** and **sidebar** has been changed in *smaller screens*.

    .. code-block:: css

        .sidebar {
            display: none;
        }

        @media (min-width: 768px) {
            .sidebar {
                background-color: #f5f5f5;
                position: fixed;
                top: 31px;
                left: 0;
                bottom: 0;
                display: block;
                padding: 20px;
            }
        }

For show **sidebar** minimum *screen width* has been selected as **768px**. If *screen width* is smaller than this, **sidebar**
will be hidden and a **navigation bar** on top would be displayed. Both **navigation bar** and **sidebar** uses *Jinja2*'s
variable switching ability. Both front and manager layout contains a *Jinja2* block that contains all menu items.

    .. code-block:: python

      {% set navigation_bar = [
        ('/manage', 'main', 'Main'),
        ('/manage/people', 'people', 'People'),
        ('/manage/penalties', 'penalties', 'Penalties'),
        ('/manage/popularity', 'popularity', 'Popularity'),
        ('/manage/cities', 'cities', 'Cities'),
        ('/manage/teams', 'teams', 'Teams'),
        ('/manage/team_stats', 'team_stats', 'Team Statistics'),
        ('/manage/players', 'players', 'Players'),
        ('/manage/sponsorships', 'sponsorships', 'Sponsorships'),
        ('/manage/stadiums', 'stadiums', 'Stadiums'),
        ('/manage/countries', 'countries', 'Countries'),
        ('/manage/tournaments', 'tournaments', 'Tournaments'),
        ('/manage/matches', 'matches', 'Matches'),
        ('/manage/leagues', 'leagues', 'Leagues')] -%}
      {% set active_page = active_page|default('main') -%}

This code block creates links, names, alternatives and also determines which page is active.
Design also gives extreme importance to the dynamism. To create dynamic pages, design utilizes jQuery and JavaScript's
AJAX capabilities. All submit operations handled with an AJAX handler that written for operation-specific purposes.
This will be discussed in later parts.

Configuration File
------------------
Configuration file hs been written in order to maintain simplicity when implementing other methods.
All configuration methods has been stored in **config.py** file. It contains two methods one for parsing
database parameters and another one is for creating a connection to database.

   .. code-block:: python

      def db_connect():
        # Connecting db by checking VCAP credentials. By courtesy of Turgut Hoca. #
        VCAP_SERVICES = os.getenv('VCAP_SERVICES')
        if VCAP_SERVICES is not None:
            dsn = get_elephantsql_dsn(VCAP_SERVICES)
        else:
            # Change this line according to your local db credentials #
            dsn = """user='postgres' password='password'
                                   host='localhost' port=5432 dbname='itucsdb1515'"""

        try:
            db_connection = connect(dsn)
            return db_connection
        except Error as error:
            print(error)
            return None


First this method checks for OS environment for environment variable called ''**VCAP_SERVICES**''. If this variable exists
then it takes and parses the connection information from deployment server. If it is not exists then it works on **localhost**,
thus it takes local information to connect the database.

REST API Skeleton
-----------------
All operations have done through the **REST API** that has written from scratch. The power of **REST API** is flexibility. It
creates an abstract layer for all operations that needed to be done. By this way, without using any interface all operations
can be completed through API. Application's user interface utilizes this ability and uses **AJAX handlers** for completing operations.
API can be accessible through ``/api`` route. If user send request to the route ``http://localhost/api`` the answer will be in
**JSON** format. All information in REST APIs are handled in JSON format. This makes it easier for AJAX handlers to understand data.

      .. code-block:: bash

            $ curl http://localhost:5000/api

            {
                  "welcome_message": "Welcome to the DBall API v1.0"
            }

    Example API usage.

Even though application has user interface, it also serves as a REST server. User interface connects API through AJAX
handlers which handles the data that came from inputs. It formats the data in JSON and passes data to API. Then API methods
does operation from the data which has been taken from request and sends a respond. According to this respond AJAX handler
either creates an error message or shows the changes.

    .. code-block:: javascript

        $('#modal-submit-form').submit(function() {
            var user_data = {
                // User data in dictionary form
            };

            $.ajax({
                url: "/api/login",
                contentType: 'application/json',
                data: JSON.stringify(user_data),
                type: "POST",
                dataType : "json",
                success: function( json ) {
                    if ( json.result ) {
                        // Operation Success.
                    } else {
                        // Operation Failure
                    }
                    console.log( json );
                },
                error: function( ) {
                    console.log( "TROUBLE!" );
                }
            });
            return false;
        });

    Skeleton for all AJAX handlers which has been used as a template on all AJAX handlers.

Get Operation
^^^^^^^^^^^^^
API can both pull and push information to the application. To pull information, users should use specific routes that has been designed
for that record. Users can either pull information for specific ID or they can pull all the records that has been stored in
database. All responses will be in JSON format. **GET** routes are only allows *GET* method. Thus if it encounters with a *POST*
request it would give a 405 error.

      .. code-block:: bash

            $ curl http://localhost:5000/api/<record_name>/<id>

      Example request for **GET** operation.

Add Operation
^^^^^^^^^^^^^
To complete add operation through API, user must be logged in. In other words, it should have a **session** in computer.
This prevents unauthorized users to alter records. After login operation user can add using ``/api/<record_name>/add``
route to add new record to the system. It only accepts *POST* method.

      .. code-block:: bash

            $ curl -X POST -d "{...}" http://localhost:5000/api/<record_name>/add

      Example request for **ADD** operation.

Update Operation
^^^^^^^^^^^^^^^^
Again to complete update operation user should be logged in. After logged in, user can use ``/api/<record_name>/update``
route to update records that have been stored in database. It only accepts *POST* method.

      .. code-block:: bash

            $ curl -X POST -d "{...}" http://localhost:5000/api/<record_name>/update

      Example request for **UPDATE** operation.

Delete Operation
^^^^^^^^^^^^^^^^
After login operation user can delete records on database from the route ``/api/<record_name>/delete``.
It only accepts *POST* method.

    .. code-block:: bash

            $ curl -X POST -d "{...}" http://localhost:5000/api/<record_name>/delete

    Example request for **DELETE** operation.

User Login and Register System
------------------------------
Another ability of API is handling user operations for application. User system something that relies on Auth API a lot.
It uses sessions in order to recognize user and store its data. Login operation can be done thorough either from user
interface or through API. Further, add, delete and update operations need authorization to complete thorough API. On the
other hand register operations only can be done through API.

    .. code-block:: python

        class User(object):
            def __init__(self, user_alias=None, user_email=None, user_pass=None,
                         is_admin=False, user_id=None):
                self.id = user_id
                self.alias = user_alias
                self.email = user_email

                if user_pass is not None:
                    self.password_hash = bcrypt.encrypt(user_pass)
                else:
                    self.password_hash = user_pass

                self.user_type = is_admin

            def get_user(self, email=None):
                pass

            def add_user_to_db(self):
                pass

    Class hierarchy in User class.

User Login
^^^^^^^^^^
User login is secure and critical process for users to alter records that have been stored in database. Since API is open,
we had to require users to login before done any operation on records to prevent data persistence. When user tries to login
through user interface data which user entered, gathered by AJAX and formatted into JSON notation. From here AJAX handler
generates a request to the API. API gets JSON-formatted data and creates a respond again in JSON format. According to respond
message AJAX handler either generates an error message or reloads the window.

    .. code-block:: python

        def api_user_login():
        # Get request header #
        json_user_data = request.get_json()

        # Get user object #
        user_info = user.User()
        user_info.get_user(json_user_data['user_email'])

        # Check user credentials #
        if user_info is not None and user_info.password_hash is not None:
            if bcrypt.verify(json_user_data['user_password'],
               user_info.password_hash) is True:
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

    API method for user login.

API is heavily dependent on **User class** which has multiple methods for completing database operations. API method
first creates an **User class** object. Then it gets data from database and compares entered password with stored salt.
If they match it returns success message, otherwise error message.

      .. code-block:: bash

            $ curl -X POST -d '{"user_email":"test@test.com", "user_password":"ali"}' http://localhost:5000/api/login

      Example request for user login operation through.


User Register
^^^^^^^^^^^^^
User registration has been only implemented in API level. From user interface there is not possible to register a new user.
When user creates and sends a request to API path, API generates a new **User class** object. Then it invokes ``add_user_to_db()``
method to store record in database. Before it stores data to database, it encrypts user password with **bcrypt** key derivation
function to increase security.

    .. code-block:: python

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

    API method for user register.

    .. code-block:: python

        """INSERT INTO users (user_name, password_hash, user_email, is_admin)
                VALUES (%s, %s, %s, %s);"""

    SQL Query used to store user information to database.

    .. code-block:: bash

        $ curl -X POST -d '{"alias":"tester", "user_name":"test", "user_password":"ali"}'
                http://localhost:5000/api/register

    Example request for user register operation through.

People Records
--------------

People records are again completed in the same way. Request generated by AJAX handler, comes into API. API parses request
gets data, and then it invokes ``add_to_db()`` method to store record in database.

As in terms of database design, it has a foreign key in ``person_birth_place`` column which is designated as city.
Also it has another foreign key to ``person_type`` table. This table has only add operation and it makes possible user to
add and thus select an type of person such as players, coaches, sponsors etc.

    .. code-block:: python

        class Person(object):
            def __init__(self, name=None, birth_date=None, birth_place=None, user_type=None, user_id=None):
                self.id = user_id
                self.name = name
                self.birth_date = birth_date
                self.birth_place = birth_place
                self.type = user_type

            def get_person_by_id(self, get_id=None):
                pass

            def add_to_db(self):
                pass

            def delete_from_db(self):
                pass

            def update_db(self):
                pass

        class PersonType(object):
            def __init__(self, type_name=None, type_id=None):
                self.id = type_id
                self.type = type_name

            def get_person_type(self, type_id=None):
                pass

            def add_to_db(self):
                pass

    Class hierarchy for Person class.

Get Operation
^^^^^^^^^^^^^
Because of foreign keys, when getting person information ``JOIN`` SQL operation has been used. Tables has been joined where
their keys has been intersect and data derived according to resulted table.

    .. code-block:: python

        # Get person type #
        type_obj = people.PersonType()
        type_obj.get_person_type(type_id)
        # Create a dict #
        data = {
            'id': type_obj.id,
            'type': type_obj.type
        }

        return jsonify(data)

    API method for get operation

    .. code-block:: python

        """SELECT * FROM person
                    JOIN city ON city.city_id = person.person_birth_location
                    JOIN person_types ON person_types.id = person.person_type
                    WHERE person_id = %s"""

    SQL query used for get operation.

Add Operation
^^^^^^^^^^^^^
Since person table has two foreign keys, thus before saving record into database it should have take foreign ids
from ``city_id`` attribute from City table and ``id`` attribute from person type table. After it got the ``city_id`` and ``id``
it can store data to database. It uses name attribute for both foreign keys as search point because it is *unique*.

    .. code-block:: python

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

            if result:
                description = "Added " + json_post_data['person_name'] + " to Persons"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})


    API method for person add operation.

    .. code-block:: python

        """SELECT id FROM person_types WHERE person_type_name = %s"""
        """SELECT city_id FROM city WHERE city_name = %s"""
        """INSERT INTO person(person_name, person_birth_date, person_birth_location, person_type)
                            VALUES (%s, %s, %s, %s)"""

    SQL Queries used to store information to database.

Update Operation
^^^^^^^^^^^^^^^^
Update operation is rather similar to add operation. After data passes from AJAX handler, API invokes ``update_db()`` method.

    .. code-block:: python

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

            # Log operations #

            return jsonify({'result': result})

    API method for person update operation.

    .. code-block:: python

        """SELECT city_id FROM city WHERE city_name=%s"""
        """SELECT id FROM person_types WHERE person_type_name=%s"""
        """UPDATE person
                   SET person_name=%s, person_birth_date=%s, person_birth_location=%s, person_type=%s
                   WHERE person_id=%s"""

    SQL Queries used to update stored information on database.

Delete Operation
^^^^^^^^^^^^^^^^
Delete operation is relatively simple when comparing the other operations. API gets a list of ids that wanted to be deleted
from request and just invokes ``delete_from_db()`` method for each.

    .. code-block:: python

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

                if status:
                    description = "Deleted " + person_obj.name + " from Persons"
                    log_info = log.Log(description, session['alias'], datetime.datetime.now())
                    log_status = log_info.add_to_db()

            return jsonify({'result': status})

    API method for person delete operation.

    .. code-block:: python

        """DELETE FROM person WHERE person_id = %s"""

    SQL Query used to delete stored information from database.

Penalty Records
---------------
Penalty records table is relatively same as person table. It has again two foreign keys one for person and another for
penalty type. Again user can add and select which types it wants but cannot delete or update it.

    .. code-block:: python

        class Penalty(object):
            def __init__(self, given_person=None, given_date=None, penalty_type=None, penalty_id=None):
                self.id = penalty_id
                self.person = given_person
                self.given_date = given_date
                self.type = penalty_type

            def get_penalty_by_id(self, get_id=None):
                pass

            def add_to_db(self):
                pass

            def delete_from_db(self):
                pass

            def update_db(self):
                pass

        class PenaltyType(object):
            def __init__(self, type_name=None, type_id=None):
                self.id = type_id
                self.type = type_name

            def get_penalty_type(self, type_id=None):
                pass

            def add_to_db(self):
                pass

    Class hierarchy for Penalty class.

Get Operation
^^^^^^^^^^^^^
Again ``JOIN`` operation has been used for getting all data in same manner as people table.

    .. code-block:: python

        def api_get_penalty(data_id):
            # Create empty penalty and fill it from db #
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

    API method for get operation

    .. code-block:: python

        """SELECT * FROM penalty
                    JOIN person ON penalty_given_person = person.person_id
                    JOIN penalty_type ON penalty_type = penalty_type.id
                    WHERE penalty_id = %s"""

    SQL query used for get operation.

Add Operation
^^^^^^^^^^^^^
Add operation also in same way as person table. But differently, this time it takes person id directly from user, thus
no additional query is needed for penalty add operation.

    .. code-block:: python

        def api_add_penalty():
            # Prevent unauthorized access from API #
            if not session.get('logged_in'):
                return jsonify({"result": "Unauthorized Access. Please identify yourself"})

            # Get json request from AJAX Handler #
            json_post_data = request.get_json()
            # print(json_post_data)
            # Create an penalty object #
            penalty_info = penalties.Penalty(json_post_data['person_name'], json_post_data['penalty_given_date'],
                                             json_post_data['penalty_type'])

            # Add it to db and send result #
            result = penalty_info.add_to_db()

            if result:
                log_person = people.Person().get_person_by_id(json_post_data['person_name'])
                description = "Added Penalty For " + log_person.name + " to Penalties"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})


    API method for add operation.

    .. code-block:: python

       """SELECT id FROM penalty_type WHERE penalty_type_name = %s"""
        """INSERT INTO penalty(penalty_type, penalty_given_person, penalty_given_date)
                  VALUES (%s, %s, %s)"""

    SQL Queries used to store information to database.

Update Operation
^^^^^^^^^^^^^^^^
Again it is similar to add operation when updating record.

    .. code-block:: python

       def api_update_penalty():
            # Get request from AJAX #
            json_data = request.get_json()
            # Get penalty from db #
            penalty_obj = penalties.Penalty()
            penalty_obj.get_penalty_by_id(json_data['penalty_id'])

            # Update penalty object's values #
            penalty_obj.person = json_data['person_name']
            penalty_obj.given_date = json_data['penalty_given_date']
            penalty_obj.type = json_data['penalty_type']

            # Update db #
            result = penalty_obj.update_db()

            if result:
                description = "Updated Element With id=" + json_data['penalty_id'] + " in Penalties"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})

    API method for update operation.

    .. code-block:: python

        """SELECT id FROM penalty_type WHERE penalty_type_name=%s"""
        """UPDATE penalty
                   SET penalty_given_date=%s, penalty_given_person=%s, penalty_type=%s
                   WHERE penalty_id=%s"""

    SQL Queries used to update stored information on database.

Delete Operation
^^^^^^^^^^^^^^^^
As it was in person table, API invokes ``delete_from_db()`` method to delete given ids.

    .. code-block:: python

        def api_delete_penalty():
            # Prevent unauthorized access #
            if not session.get('logged_in'):
                return jsonify({"result": "Unauthorized Access. Please identify yourself"})

            status = False
            # Get request #
            penalty_id_json = request.get_json()
            # Delete every requested id #
            for penalty_id in penalty_id_json:
                penalty_obj = penalties.Penalty()
                penalty_obj.get_penalty_by_id(penalty_id)
                # print(penalty_id)
                status = penalty_obj.delete_from_db()

                if status:
                    description = "Deleted Penalty For " + penalty_obj.person + " from Penalties"
                    log_info = log.Log(description, session['alias'], datetime.datetime.now())
                    log_status = log_info.add_to_db()

            return jsonify({'result': status})

    API method for delete operation.

    .. code-block:: python

        """DELETE FROM penalty WHERE penalty_id = %s"""

    SQL Query used to delete stored information from database.

Popularity Records
------------------
Popularity table one of the weakest relations in the database. It has three foreign keys to other tables for team, player
and match and also an integer value for supporters.

    .. code-block:: python

        class Popularity(object):
            def __init__(self, team=None, match=None, player=None, supporters=None, popularity_id=None):
                self.id = popularity_id
                self.team = team
                self.match = match
                self.player = player
                self.supporters = supporters

            def get_popularity_by_id(self, get_id=None):
                pass

            def add_to_db(self):
                pass

            def delete_from_db(self):
                pass

            def update_db(self):
                pass

    Class hierarchy for Popularity class.

Get Operation
^^^^^^^^^^^^^
Again ``JOIN`` operation has been used for getting all data in same manner as people table. But this time it as more joins.

    .. code-block:: python

        def api_get_popularity(data_id):
            # Create empty popularity and fill it from db #
            popularity_obj = popularity.Popularity()
            popularity_obj.get_popularity_by_id(data_id)

            # Create a dict for jsonify #
            data = {
                'id': popularity_obj.id,
                'team': popularity_obj.team,
                'match': popularity_obj.match,
                'player': popularity_obj.player,
                'supporters': popularity_obj.supporters
            }

            return jsonify(data)

    API method for get operation

    .. code-block:: python

        """SELECT * FROM popularity
                    JOIN team AS team1 ON popularity.team_name = team1.team_id
                    JOIN matches ON popularity.most_popular_match = matches.match_id
                    JOIN team AS team2 ON matches.match_team_1 = team2.team_id
                    JOIN team AS team3 ON matches.match_team_2 = team3.team_id
                    JOIN person ON popularity.most_popular_player = person.person_id"""

    SQL query used for get operation.

In order to display multiple teams there has been multiple joins on teams used.

Add Operation
^^^^^^^^^^^^^
Add operation takes foreign key values directly from the user in order to optimize queries.

    .. code-block:: python

        def api_add_popularity():
            # Prevent unauthorized access from API #
            if not session.get('logged_in'):
                return jsonify({"result": "Unauthorized Access. Please identify yourself"})

            # Get json request from AJAX Handler #
            json_post_data = request.get_json()
            # print(json_post_data)
            # Create an popularity object #
            popularity_info = popularity.Popularity(json_post_data['team'], json_post_data['match'],
                                                    json_post_data['player'], json_post_data['supporters'])

            # Add it to db and send result #
            result = popularity_info.add_to_db()

            if result:
                description = "Added Popularity Info for " + json_post_data['team'] + " to Popularity"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})


    API method for add operation.

    .. code-block:: python

       """INSERT INTO popularity(team_name, most_popular_match, most_popular_player, supporters)
                            VALUES (%s, %s, %s, %s)"""

    SQL Queries used to store information to database.

Update Operation
^^^^^^^^^^^^^^^^
Again it is similar to add operation when updating record.

    .. code-block:: python

       def api_update_popularity():
            # Get request from AJAX #
            json_data = request.get_json()
            # Get person from db #
            popularity_obj = popularity.Popularity()
            popularity_obj.get_popularity_by_id(json_data['popularity_id'])

            # Update person object's values #
            popularity_obj.team = json_data['team']
            popularity_obj.match = json_data['match']
            popularity_obj.player = json_data['player']
            popularity_obj.supporters = json_data['supporters']

            # Update db #
            result = popularity_obj.update_db()

            if result:
                description = "Updated Element With id=" + json_data['popularity_id'] + " in Popularity"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})

    API method for update operation.

    .. code-block:: python

        """UPDATE popularity
                   SET team_name=%s, most_popular_match=%s, most_popular_player=%s, supporters=%s
                   WHERE popularity_id=%s"""

    SQL Query used to update stored information on database.

Delete Operation
^^^^^^^^^^^^^^^^
As it was in person table, API invokes ``delete_from_db()`` method to delete given ids.

    .. code-block:: python

        def api_delete_popularity():
            # Prevent unauthorized access #
            if not session.get('logged_in'):
                return jsonify({"result": "Unauthorized Access. Please identify yourself"})

            status = False
            # Get request #
            popularity_id_json = request.get_json()
            # Delete every requested id #
            for popularity_id in popularity_id_json:
                popularity_obj = popularity.Popularity()
                popularity_obj.get_popularity_by_id(popularity_id)
                # print(penalty_id)
                status = popularity_obj.delete_from_db()

                if status:
                    description = "Deleted Popularity Info For " + popularity_obj.team + " from Penalties"
                    log_info = log.Log(description, session['alias'], datetime.datetime.now())
                    log_status = log_info.add_to_db()

            return jsonify({'result': status})

    API method for delete operation.

    .. code-block:: python

        """DELETE FROM popularity WHERE popularity_id = %s"""

    SQL Query used to delete stored information from database.

City Records
------------
City table does not contain any foreign key. It uses Google Maps Geocode API in order to store location information.

    .. code-block:: python

        class City(object):
            def __init__(self, city_name=None, city_population=None, city_coordinates=None, city_id=None):
                self.id = city_id
                self.name = city_name
                self.coordinates = city_coordinates
                self.population = city_population

            def get_city_by_id(self, get_id=None):
                pass

            def add_to_db(self):
                pass

            def delete_from_db(self):
                pass

            def update_db(self):
                pass

    Class hierarchy for City class.

Get Operation
^^^^^^^^^^^^^

Get operation is simple for city table. There is no joins since it does not have any foreign key.

    .. code-block:: python

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

    API method for get operation

    .. code-block:: python

        """SELECT * FROM city WHERE city_id = %s"""

    SQL Queries used for get operation


Add Operation
^^^^^^^^^^^^^
Add operation get city nme and population as input, then sends city name to Maps API and gets geolocation to store.

    .. code-block:: python

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

            if result:
                description = "Added " + json_post_data['city_name'] + " to Cities"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})

    API method for add operation

    .. code-block:: python

        """INSERT INTO city (city_name, city_population, city_coordinates)
                        VALUES (%s, %s, %s)"""

    SQL Queries used for add operation

Update Operation
^^^^^^^^^^^^^^^^
Again update operation also does same thing as ha been done in add operation.
    .. code-block:: python

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

            if result:
                description = "Updated Element With id=" + json_data['city_id'] + " in Cities"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

            return jsonify({'result': result})

    API method for update operation

    .. code-block:: python

        """UPDATE city
                   SET city_name=%s, city_population=%s, city_coordinates=%s
                   WHERE city_id=%s"""

    SQL Queries used for update operation

Delete Operation
^^^^^^^^^^^^^^^^
Delete operation directly deletes data from database.

    .. code-block:: python

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

                if status:
                    description = "Deleted " + city_obj.name + " from Cities"
                    log_info = log.Log(description, session['alias'], datetime.datetime.now())
                    log_status = log_info.add_to_db()

            return jsonify({'result': status})

    API method for delete operation

    .. code-block:: python

        """DELETE FROM city WHERE city_id = %s"""

    SQL Queries used for delete operation

