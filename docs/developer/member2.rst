Parts Implemented by Umut Can Ozyar
===================================
Sponsorships
------------
All the sponsorships data interaction with the database happens with queries send to the server from the objects created
by the sponsorship class. This table has three foreign keys, sponsorship_league, sponsorship_team and sponsorship_person,
which refers to leagues, teams and people table respectively. Id is in type serial, therefore it's generated automatically,
with each new entry. The rest of the fields requires new user input.

.. code-block:: python

    class Sponsorship(object):
        def __init__(self, sponsorship_name=None, sponsorship_start_date=None, sponsorship_league=None,
                     sponsorship_team=None, sponsorship_person=None, sponsorship_id=None):
            self.id = sponsorship_id
            self.name = sponsorship_name
            self.start_date = sponsorship_start_date
            self.league = sponsorship_league
            self.team = sponsorship_team
            self.person = sponsorship_person

Get Sponsorship
+++++++++++++++
This operation is the most essential one as it's used for several key actions. Either by sending an id to get a specific
tuple or to get the whole table get_sponsorshop_by_id method is called by the API. Then the SELECT queries found below,
will be called with the only difference of WHERE sponsorship_id = %s which indicates that a unique id is specified. Three
different OUTER JOIN operations are made to get the league, team and person names by joining these tables over their ids.

.. code-block:: python

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

.. code-block:: python

    def get_sponsorship_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT sponsorship.sponsorship_id, sponsorship.sponsorship_name, sponsorship.sponsorship_start_date,
                            sponsorship.sponsorship_league, sponsorship.sponsorship_team, sponsorship.sponsorship_person,
                            person.person_name FROM sponsorship
                            LEFT OUTER JOIN league ON league.league_id = sponsorship.sponsorship_league
                            LEFT OUTER JOIN team ON team.team_id = sponsorship.sponsorship_team
                            LEFT OUTER JOIN person ON person.person_id = sponsorship.sponsorship_person
                            WHERE sponsorship_id = %s"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.start_date = data[2]
                self.league = data[3]
                self.team = data[4]
                self.person = data[5]
                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT sponsorship.sponsorship_id, sponsorship.sponsorship_name,
                            sponsorship.sponsorship_start_date, sponsorship.sponsorship_league,
                            sponsorship.sponsorship_team, sponsorship.sponsorship_person,
                            league.league_id, league.league_name,
                            team.team_id, team.team_name,
                            person.person_id, person.person_name FROM sponsorship
                            LEFT OUTER JOIN league ON league.league_id = sponsorship.sponsorship_league
                            LEFT OUTER JOIN team ON team.team_id = sponsorship.sponsorship_team
                            LEFT OUTER JOIN person ON person.person_id = sponsorship.sponsorship_person"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            sponsorship_array = []
            data = cursor.fetchall()
            for sponsorship in data:
                sponsorship_array.append(
                    {
                        'id': sponsorship[0],
                        'name': sponsorship[1],
                        'start_date': sponsorship[2].strftime('%d/%m/%Y'),
                        'league': sponsorship[7],
                        'team': sponsorship[9],
                        'person': sponsorship[11]
                    }
                )

            cursor.close()
            connection.close()
            return sponsorship_array

Add Sponsorship
+++++++++++++++
After the forms on the modal for adding sponsorship are submitted, first the authorization process is made for the user by
the API. If the authorization is successful, the API gets the json request from the AJAX handler. This data is then used
to create a sponsorship object by calling the sponsorship constructor. Then add_to_db function is called on this object
to perform the insertion query for sponsorship that can be found below. Note that the INSERT query is called by using
foreign keys to league, team and person tables ids. Thus their ids should be fetched by using provided names.

.. code-block:: python

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

        if result:
            description = "Added " + json_post_data['sponsorship_name'] + " to Sponsorships"
            log_info = log.Log(description, session['alias'], datetime.datetime.now())
            log_status = log_info.add_to_db()

        return jsonify({'result': result})

.. code-block:: python

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_league = None
        new_team = None
        new_person = None

        select_league = """SELECT league_id FROM league WHERE league_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_person = """SELECT person_id FROM person WHERE person_name = %s"""

        statement = """INSERT INTO sponsorship (sponsorship_name, sponsorship_start_date,
                        sponsorship_league, sponsorship_team, sponsorship_person )
                        VALUES (%s, %s, %s, %s, %s)"""
        try:
            cursor.execute(select_league, (self.league,))
            connection.commit()
            new_league = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_person, (self.person,))
            connection.commit()
            new_person = cursor.fetchone()

            cursor.execute(statement, (self.name, self.start_date, new_league, new_team, new_person))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

Delete Sponsorship
++++++++++++++++++
Delete operation is a single DELETE query. delete_from_db function is called after the id of the selected rows' data is
fetched and corresponding objects are found.

.. code-block:: python

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

            if status:
                description = "Deleted " + sponsorship_obj.name + " from Sponsorships"
                log_info = log.Log(description, session['alias'], datetime.datetime.now())
                log_status = log_info.add_to_db()

        return jsonify({'result': status})

.. code-block:: python

    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """DELETE FROM sponsorship WHERE sponsorship_id = %s"""

        try:
            cursor.execute(statement, (self.id,))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

Update Sponsorship
++++++++++++++++++
Update operation works similar to the add operation except the fact that there is existing data. The AJAX handler provides
the data to the API which assigns them to corresponding data members. Finally the UPDATE query is executed to apply the
changes to the database

.. code-block:: python

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

        if result:
            description = "Updated element with id=" + json_data['sponsorship_id'] + " in Sponsorships"
            log_info = log.Log(description, session['alias'], datetime.datetime.now())
            log_status = log_info.add_to_db()

        return jsonify({'result': result})

.. code-block:: python

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()
        status = False

        new_league = None
        new_team = None
        new_person = None

        select_league = """SELECT league_id FROM league WHERE league_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_person = """SELECT person_id FROM person WHERE person_name = %s"""

        statement = """UPDATE sponsorship
                       SET sponsorship_name=%s, sponsorship_start_date=%s, sponsorship_league=%s,
                       sponsorship_team=%s, sponsorship_person=%s
                       WHERE sponsorship_id=%s"""

        try:
            cursor.execute(select_league, (self.league,))
            connection.commit()
            new_league = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_person, (self.person,))
            connection.commit()
            new_person = cursor.fetchone()

            cursor.execute(statement, (self.name, self.start_date, new_league, new_team, new_person, self.id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

Team Statistics
---------------
Team statistics class functions are mostly given as prototypes except for their queries and class data members as they
are constructed in a relatively simple manner. The API functions are also omitted for the sake of simplicity since the
only meaningful difference is the table names.

Team_stat table also has an id as its primary key. The rest of the data members are all in integer type and required to
be provided by the user.

.. code-block:: python

    class Team_stat(object):
        def __init__(self, team_stat_name=None, team_stat_run=None, team_stat_hit=None,
                     team_stat_save=None, team_stat_win=None, team_stat_draw=None,
                     team_stat_loss=None, team_stat_id=None):
            self.id = team_stat_id
            self.name = team_stat_name
            self.run = team_stat_run
            self.hit = team_stat_hit
            self.save = team_stat_save
            self.win = team_stat_win
            self.draw = team_stat_draw
            self.loss = team_stat_loss

        def get_team_stat_by_id():

        def add_to_db():

        def delete_from_db():

        def update_db():

Please refer to :ref:`sponsorship` for examples of the omitted parts of the team statistics class and API functions.

Get Team Statistics
+++++++++++++++++++
Fetching a team's statistics is done when def get_team_stat_by_id function is called by the API which executes the following
query. It's a select query that gets the only tuple from the database for the provided id since all ids are unique.

.. code-block:: python

    statement = """SELECT team_stat.team_stat_id, team_stat.team_stat_name, team_stat.team_stat_run,
                    team_stat.team_stat_hit, team_stat.team_stat_save, team_stat.team_stat_win,
                    team_stat.team_stat_draw, team_stat.team_stat_loss
                    FROM team_stat
                    WHERE team_stat_id = %s"""

Add Team Statistics
+++++++++++++++++++
Adding team statistics can be cumbersome since the matches data is not structured taking total wins, draws and losses into
consideration. Therefore a few SELECT queries should be executed prior to the main insertion query. Extra queries for draws
and losses as well as the foreign key related queries are omitted for the sake of simplicity. The different tables are counted
to get home and away wins. These values are then summed before inserted into the table. Draws and losses are calculated
in the same manner. Each team's total matches are also counted with a simple SELECT count query.

.. code-block:: python

    count_win1 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_1
                    WHERE (matches.match_team1_score > matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

    count_win2 = """SELECT COUNT(*) FROM matches
                    LEFT OUTER JOIN team ON team.team_id = matches.match_team_2
                    WHERE (matches.match_team1_score < matches.match_team2_score AND team.team_name = %s)
                    GROUP BY team.team_name"""

    total_wins = count_win1 + count_win2

    statement = """INSERT INTO team_stat (team_stat_name, team_stat_run,
                    team_stat_hit, team_stat_save, team_stat_win,
                    team_stat_draw, team_stat_loss )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    count_matches = """SELECT count(match_id) FROM matches"""

Delete Team Statistics
++++++++++++++++++++++
Deletion is a simple operation which is executed after getting the ids of the selected rows from the table.

.. code-block:: python

    statement = """DELETE FROM team_stat WHERE team_stat_id = %s"""

Update Team Statistics
++++++++++++++++++++++
Update also has several extra queries like the add function which calculates total wins, draws and losses. Runs, hits and
saves fields can also be updated when provided with new data.

.. code-block:: python

    statement = """UPDATE team_stat
                   SET team_stat_name=%s, team_stat_run=%s, team_stat_hit=%s, team_stat_save=%s,
                   team_stat_win=%s, team_stat_draw=%s, team_stat_loss=%s
                   WHERE team_stat_id=%s"""

Stadiums
--------
Stadiums class functions are mostly given as prototypes except for their queries and class data members as they
are constructed in a relatively simple manner with the sponsorship class. The API functions are also omitted for the sake
of simplicity since the only meaningful difference is the table names.

Stadium table also has an id as its primary key. The rest of the data members are all in integer type and required to
be provided by the user. Location is a foreign key to the city_id column of the city table. Another foreign key is
stadium_team which points to the team table.

.. code-block:: python

    class Stadium(object):
        def __init__(self, stadium_name=None, stadium_team=None, stadium_location=None,
                     stadium_capacity=None, stadium_id=None):
            self.id = stadium_id
            self.name = stadium_name
            self.team = stadium_team
            self.location = stadium_location
            self.capacity = stadium_capacity

        def get_team_stat_by_id():

        def add_to_db():

        def delete_from_db():

        def update_db():

Please refer to :ref:`sponsorship` for examples of the omitted parts of the stadium class and API functions.

Get Stadium
+++++++++++
Fetching a team's stadium is done when def get_stadium_by_id function is called by the API which executes the following
query. It's a select query that gets the only tuple from the database for the provided id since all ids are unique.

.. code-block:: python

    statement = """SELECT stadium.stadium_id, stadium.stadium_name, stadium.stadium_team,
                    stadium.stadium_location, stadium.stadium_capacity,
                    team.team_id, team.team_name,
                    city.city_id, city.city_name
                    FROM stadium
                    LEFT OUTER JOIN team ON team.team_id = stadium.stadium_team
                    LEFT OUTER JOIN city ON city.city_id = stadium.stadium_location
                    WHERE stadium_id = %s"""

Add Stadium
+++++++++++
There are only two foreign keys for stadium table which are teams and locations. Id is automatically generated for each
new entry therefore the rest of the fields like name and capacity should be provided by the user. After the API gets the
data from the AJAX handler add_to_db function of the stadium is called which executes the following query to add the new
stadium to the database.

.. code-block:: python

    statement = """INSERT INTO stadium (stadium_name, stadium_team,
                    stadium_location, stadium_capacity )
                    VALUES (%s, %s, %s, %s)"""

Delete Stadium
++++++++++++++
Deletion is just a single query which is executed after getting the ids of the selected rows from the table.

.. code-block:: python

    statement = """DELETE FROM stadium WHERE stadium_id = %s"""

Update Stadium
++++++++++++++
After selecting the correct team_id for the chosen team and city_id for the chosen city name, all the inputs are passed
to the UPDATE query which applies the changes to the database.

.. code-block:: python

    statement = """UPDATE stadium
                   SET stadium_name=%s, stadium_team=%s, stadium_location=%s, stadium_capacity=%s
                   WHERE stadium_id=%s"""

