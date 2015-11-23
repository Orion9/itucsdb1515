###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Player (object):
    def __init__(self, player_name=None, player_team=None, player_country=None, player_id=None):
        self.id = player_id
        self.name = player_name
        self.team = player_team
        self.country = player_country

    def get_player_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT p.player_id, p.player_name, p.player_team, p.player=country,
                       person.person_name, team.team_name, country.country_name FROM player AS p
                       LEFT OUTER JOIN person ON person.person_id = p.player_name
                       LEFT OUTER JOIN team ON team.team_name = p.player_team
                       LEFT OUTER JOIN country ON country_name = p.player_country
                       WHERE player_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.team = data[2]
                    self.country = data[3]
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
            query = """SELECT player.player_id, player.player_name,player.player_team,player.player_country,
                       person.person_name, team.team_name, country.country_name
                       FROM team
                       LEFT OUTER JOIN person ON person.person_id = p.player_name
                       LEFT OUTER JOIN team ON team.team_name = p.player_team
                       LEFT OUTER JOIN country ON country_name = p.player_country
                       """
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                array = []
                data = cursor.fetchall()
                for player in data:
                    array.append(
                        {
                            'id': player[0],
                            'name': player[1],
                            'team': player[2],
                            'country': player[3],
                        }
                        )

                print(array)

                cursor.close()
                connection.close()

                return array

            except connection.Error as error:
                print(error)
                connection.rollback()

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_person = """SELECT person_id FROM person WHERE person_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_country = """SELECT country_id FROM country WHERE country_name = %s"""



        # query to add given team tuple to database
        query = """INSERT INTO team (player_name, player_team, player_country)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(select_person, (self.name,))
            connection.commit()
            person_id = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            team_id = cursor.fetchone()

            cursor.execute(select_country, (self.country,))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (person_id, team_id, country_id, self.id))
            connection.commit()

            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        query = """DELETE FROM player WHERE player_id = %s"""

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

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_person = """SELECT person_id FROM person WHERE person_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_country = """SELECT country_id FROM country WHERE country_name = %s"""

        query = """UPDATE player
                   SET player_name=%s, player_team=%s,
                   player_country=%s
                   WHERE team_id=%s"""

        try:
            cursor.execute(select_person, (self.name,))
            connection.commit()
            person_id = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            team_id = cursor.fetchone()

            cursor.execute(select_country, (self.country,))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (person_id, team_id, country_id, self.id))
            connection.commit()

            status = True
        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status