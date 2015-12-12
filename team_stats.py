###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Team_stat(object):
    def __init__(self, team_stat_name=None, team_stat_team=None, team_stat_location=None,
                 team_stat_capacity=None, team_stat_id=None):
        self.id = team_stat_id
        self.name = team_stat_name
        self.team = team_stat_team
        self.location = team_stat_location
        self.capacity = team_stat_capacity

    def get_team_stat_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT team_stat.team_stat_id, team_stat.team_stat_name, team_stat.team_stat_team,
                            team_stat.team_stat_location, team_stat.team_stat_capacity,
                            team.team_id, team.team_name,
                            city.city_id, city.city_name
                            FROM team_stat
                            LEFT OUTER JOIN team ON team.team_id = team_stat.team_stat_team
                            LEFT OUTER JOIN city ON city.city_id = team_stat.team_stat_location
                            WHERE team_stat_id = %s"""
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
                self.location = data[3]
                self.capacity = data[4]

                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT team_stat.team_stat_id, team_stat.team_stat_name, team_stat.team_stat_team,
                            team_stat.team_stat_location, team_stat.team_stat_capacity,
                            team.team_id, team.team_name,
                            city.city_id, city.city_name
                            FROM team_stat
                            LEFT OUTER JOIN team ON team.team_id = team_stat.team_stat_team
                            LEFT OUTER JOIN city ON city.city_id = team_stat.team_stat_location"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            team_stat_array = []
            data = cursor.fetchall()
            for team_stat in data:
                team_stat_array.append(
                    {
                        'id': team_stat[0],
                        'name': team_stat[1],
                        'team': team_stat[6],
                        'location': team_stat[8],
                        'capacity': team_stat[4]
                    }
                )
            print(team_stat_array)
            cursor.close()
            connection.close()
            return team_stat_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_team = None
        new_location = None

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_location = """SELECT city_id FROM city WHERE city_name = %s"""

        statement = """INSERT INTO team_stat (team_stat_name, team_stat_team,
                        team_stat_location, team_stat_capacity )
                        VALUES (%s, %s, %s, %s)"""
        try:
            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_location, (self.location,))
            connection.commit()
            new_location = cursor.fetchone()

            cursor.execute(statement, (self.name, new_team, new_location, self.capacity))
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

        statement = """DELETE FROM team_stat WHERE team_stat_id = %s"""

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
        select_location = """SELECT city_id FROM city WHERE city_name = %s"""

        statement = """UPDATE team_stat
                       SET team_stat_name=%s, team_stat_team=%s, team_stat_location=%s, team_stat_capacity=%s
                       WHERE team_stat_id=%s"""
        try:
            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_location, (self.location,))
            connection.commit()
            new_location = cursor.fetchone()

            cursor.execute(statement, (self.name, new_team, new_location, self.capacity, self.id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status
