Parts Implemented by Mert Şeker
===============================


Database Operations for Each Entity
+++++++++++++++++++++++++++++++++++
For each database operations of entities, appropriate SQL queries are written and
they are executed within the functions in the .py class files.

Team
----

Team tuples have three columns; id, name and coach. Coach is a foreign key to the person table.

Get Team By Id
++++++++++++++

In order to get teams and use them in functions, the primary key(team_id) is used.
A dictionary is created with the chosen team's data and it is returned.
You can see how this operation is done in the code below:

    .. code-block:: python

      def get_team_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT t.team_id, t.team_name, t.team_couch,person.person_name
                       FROM team AS t
                       LEFT OUTER JOIN person ON person.person_id = t.team_couch
                       WHERE team_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.couch = data[2]
                    cursor.close()
                    connection.close()
                    return self

                else:
                    cursor.close()
                    connection.close()
                    return None

            except connection.Error as error:
                print(error)
                connection.rollback()

        else:
            query = """SELECT team.team_id, team.team_name,team.team_couch,person.person_id,person.person_name FROM team
                       LEFT OUTER JOIN person ON person.person_id = team.team_couch"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                array = []
                data = cursor.fetchall()
                for team in data:
                    array.append(
                        {
                            'id': team[0],
                            'name': team[1],
                            'couch': team[4]
                        }
                        )
                cursor.close()
                connection.close()

                return array

            except connection.Error as error:
                print(error)
                connection.rollback()


Add Team To Database
++++++++++++++++++++

In order to add team tuples to the database, INSERT INTO queries are used and executed.
The foreign keys are selected from the referenced tables by id.You can see it in the code below:

    .. code-block:: python

      def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_person = """SELECT person_id FROM person WHERE person_name = %s"""



        # query to add given team tuple to database
         query = """INSERT INTO team (team_name, team_couch)
                        VALUES (%s, %s)"""

        try:
            cursor.execute(select_person, (self.couch,))
            connection.commit()
            new_person = cursor.fetchone()

            cursor.execute(query, (self.name, new_person))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


Delete Team From Database
+++++++++++++++++++++++++
The team to be deleted is selected by id and deleted by using DELETE FROM query.
You can see it in the code below:

    .. code-block:: python

      def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query = """DELETE FROM team WHERE team_id = %s"""

        try:
            cursor.execute(query, (self.id,))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


Update Team
+++++++++++
The team to be updated is selected by id and updated by the UPDATE query. Just like in add operation,the foreign
keys are selected from the referenced table by id.
You can see it in the code below:

    .. code-block:: python

      def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_person = """SELECT person_id FROM person WHERE person_name = %s"""

        query = """UPDATE team
                   SET team_name=%s, team_couch=%s
                   WHERE team_id=%s"""

        try:
            cursor.execute(select_person, (self.couch,))
            connection.commit()
            person_id = cursor.fetchone()

            cursor.execute(query, (self.name, person_id, self.id))
            connection.commit()
            status = True
        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

Player
------

Player tuples have four columns; id,name, team and number of goals. Team is a foreign key to the teams table.

Get Player By Id
++++++++++++++++

In order to get players and use them in functions, the primary key(player_id) is used.
A dictionary is created with the chosen player's data and it is returned.
You can see how this operation is done in the code below:

    .. code-block:: python

      def get_player_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT *
                                FROM player
                                JOIN team ON team.team_id = player.player_team
                                WHERE player_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.goals = data[3]
                    self.team = data[5]

                    cursor.close()
                    connection.close()
                    return self

                else:
                    cursor.close()
                    connection.close()
                    return None

            except connection.Error as error:
                print(error)
                connection.rollback()

        else:
            query = """SELECT * FROM player
                                JOIN team ON team.team_id = player.player_team"""
            try:
                cursor.execute(query)
                connection.commit()
            except connection.Error as error:
                print(error)
                connection.rollback()

            array = []
            data = cursor.fetchall()

            for player in data:
                array.append(
                    {
                        'id': player[0],
                        'name': player[1],
                        'goals': player[3],
                        'team': player[5]
                    }
                )
            print(array)

            cursor.close()
            connection.close()

            return array




Add Player To Database
++++++++++++++++++++++

In order to add player tuples to the database, INSERT INTO queries are used and executed.
The foreign keys are selected from the referenced tables by id.You can see it in the code below:

    .. code-block:: python

      def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # query to get referenced team by its id
        query_team = """SELECT team_id FROM team
                                WHERE team_name = %s"""

        # query to add given player tuple to database
        query = """INSERT INTO player (player_name, player_team, player_goals)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query_team, (self.team,))
            connection.commit()
            team_id = cursor.fetchone()

            cursor.execute(query, (self.name, team_id, self.goals,))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()

        return status


Delete Player From Database
+++++++++++++++++++++++++++
The player to be deleted is selected by id and deleted by using DELETE FROM query.
You can see it in the code below:

    .. code-block:: python

      def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query = """DELETE FROM player WHERE player_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


Update Player
+++++++++++++
The player to be updated is selected by id and updated by the UPDATE query. Just like in add operation,the foreign
keys are selected from the referenced table by id.
You can see it in the code below:

    .. code-block:: python

      def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query_team = """SELECT team_id FROM team WHERE team_name=%s"""
        query = """UPDATE player
                   SET player_name=%s, player_team=%s, player_goals=%s
                   WHERE player_id=%s"""

        try:
            cursor.execute(query_team, (self.team, ))
            connection.commit()
            team_id = cursor.fetchone()

            cursor.execute(query, (self.name, team_id, self.goals, self.id,))
            connection.commit()
            status = True
        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False
        finally:
            cursor.close()
            connection.close()
            return status


Tournament
----------

Tournament tuples have seven columns; id,name,number of matches,start date,end date,country and prize.
Country is a foreign key to the countries table.

Get Tournament By Id
++++++++++++++++++++

In order to get tournaments and use them in functions, the primary key(tournament_id) is used.
A dictionary is created with the chosen tournament's data and it is returned.
You can see how this operation is done in the code below:

    .. code-block:: python

      def get_tournament_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM tournament
                                JOIN country ON country.country_id = tournament.tournament_country
                                WHERE tournament_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.matches = data[2]
                    self.start_date = data[3]
                    self.end_date = data[4]
                    self.country = data[8]
                    self.prize = data[6]

                    cursor.close()
                    connection.close()
                    return self

                else:
                    cursor.close()
                    connection.close()
                    return None

            except connection.Error as error:
                print(error)
                connection.rollback()

        else:
            query = """SELECT * FROM tournament
                                JOIN country ON country.country_id = tournament.tournament_country"""
            try:
                cursor.execute(query)
                connection.commit()
            except connection.Error as error:
                print(error)
                connection.rollback()

            array = []
            data = cursor.fetchall()
            for tournament in data:
                array.append(
                    {
                        'id': tournament[0],
                        'name': tournament[1],
                        'matches': tournament[2],
                        'start_date': tournament[3].strftime('%d/%m/%Y'),
                        'end_date': tournament[4].strftime('%d/%m/%Y'),
                        'country': tournament[8],
                        'prize': tournament[6]
                    }
                )
            cursor.close()
            connection.close()

            return array


Add Tournament To Database
++++++++++++++++++++++++++

In order to add tournament tuples to the database, INSERT INTO queries are used and executed.
The foreign keys are selected from the referenced tables by id.You can see it in the code below:

    .. code-block:: python

      def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # query to get referenced country by its id
        query_country = """SELECT country_id FROM country
                                WHERE country_name = %s"""

        # query to add given tournament tuple to database
        query = """INSERT INTO tournament (tournament_name, tournament_matches, tournament_start_date, tournament_end_date,
                                       tournament_country, tournament_prize)
                        VALUES (%s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(query_country, (self.country,))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.matches, self.start_date, self.end_date, country_id, self.prize))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()

        return status


Delete Tournament From Database
+++++++++++++++++++++++++++++++
The tournament to be deleted is selected by id and deleted by using DELETE FROM query.
You can see it in the code below:

    .. code-block:: python

      def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query = """DELETE FROM tournament WHERE tournament_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


Update Tournament
+++++++++++++++++
The tournament to be updated is selected by id and updated by the UPDATE query. Just like in add operation,the foreign
keys are selected from the referenced table by id.
You can see it in the code below:

    .. code-block:: python

      def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query_country = """SELECT country_id FROM country WHERE country_name=%s"""
        query = """UPDATE tournament
                   SET tournament_name=%s, tournament_matches=%s, tournament_start_date=%s, tournament_end_date=%s, tournament_country=%s, tournament_prize=%s
                   WHERE tournament_id=%s"""

        try:
            cursor.execute(query_country, (self.country, ))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.matches, self.start_date, self.end_date, country_id, self.prize, self.id,))
            connection.commit()
            status = True
        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False
        finally:
            cursor.close()
            connection.close()
            return status