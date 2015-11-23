###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Player(object):
    def __init__(self, player_name=None, player_team=None, player_goals=None, player_id=None):
        self.id = player_id
        self.name = player_name
        self.team = player_team
        self.goals = player_goals

    def get_player_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT player.player_id, player.player_name, player.player_team,
                            player.player_goals,
                            team.team_id, team.team_name
                            FROM player
                            LEFT OUTER JOIN team ON team.team_id = player.player_team
                            WHERE player_id = %s"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.team = data[2]
                self.goals = data[3]
                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT player.player_id, player.player_name, player.player_team,
                            player.player_goals,
                            team.team_id, team.team_name
                            FROM player
                            LEFT OUTER JOIN team ON team.team_id = player.player_team"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            player_array = []
            data = cursor.fetchall()
            for player in data:
                player_array.append(
                    {
                        'id': player[0],
                        'name': player[1],
                        'team': player[5],
                        'goals': player[3],
                    }
                )
            print(player_array)
            cursor.close()
            connection.close()
            return player_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""

        statement = """INSERT INTO player (player_name, player_team,
                        player_goals)
                        VALUES (%s, %s, %s)"""
        try:
            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(statement, (self.name, new_team, self.goals))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """DELETE FROM player WHERE player_id = %s"""

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

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""

        statement = """UPDATE player
                       SET player_name=%s, player_team=%s, player_goals=%s
                       WHERE player_id=%s"""
        try:
            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(statement, (self.name, new_team, self.goals, self.id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


