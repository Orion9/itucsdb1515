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
    def __init__(self, player_name=None, player_team=None,
                 player_goals=None, player_id=None):
        self.id = player_id
        self.name = player_name
        self.goals = player_goals
        self.team = player_team

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

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # query to get referenced team by its id
        query_team = """SELECT team_id FROM team
                                WHERE team_name = %s"""

        # query to add given league tuple to database
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
