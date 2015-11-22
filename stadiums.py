###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Stadium(object):
    def __init__(self, stadium_name=None, stadium_team=None, stadium_location=None,
                 stadium_capacity=None, stadium_id=None):
        self.id = stadium_id
        self.name = stadium_name
        self.team = stadium_team
        self.location = stadium_location
        self.capacity = stadium_capacity

    def get_stadium_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT s.stadium_id, s.stadium_name, s.stadium_team,
                            s.stadium_location, s.stadium_capacity,
                            team.team_id, team.team_name,
                            city.league_id, city.city_name,
                            FROM stadium AS s
                            LEFT OUTER JOIN team ON team.team_id = stadium.stadium_team
                            LEFT OUTER JOIN city ON city.city_id = stadium.stadium_location
                            WHERE stadium_id = %s"""
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
            statement = """SELECT s.stadium_id, s.stadium_name, s.stadium_team,
                            s.stadium_location, s.stadium_capacity,
                            team.team_id, team.team_name,
                            city.city_id, city.city_name,
                            FROM stadium AS s
                            LEFT OUTER JOIN team ON team.team_id = stadium.stadium_team
                            LEFT OUTER JOIN city ON city.city_id = stadium.stadium_location"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            stadium_array = []
            data = cursor.fetchall()
            for stadium in data:
                stadium_array.append(
                    {
                        'id': stadium[0],
                        'name': stadium[1],
                        'team': stadium[6],
                        'location': stadium[8],
                        'capacity': stadium[4]
                    }
                )
            print(stadium_array)
            cursor.close()
            connection.close()
            return stadium_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_team = None
        new_location = None

        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_location = """SELECT city_id FROM city WHERE city_name = %s"""

        statement = """INSERT INTO stadium (stadium_name, stadium_team,
                        stadium_location, stadium_capacity )
                        VALUES (%s, %s, %s, %s, %s)"""
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

        statement = """DELETE FROM stadium WHERE stadium_id = %s"""

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


