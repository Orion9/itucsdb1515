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

    .. code-block:: sql

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

Penalty Records
---------------

Popularity Records
------------------

City Records
------------
