###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect

class Team (object):
    def __init__(self, team_name=None, team_id=None, couch_id=None):
        self.id = team_id
        self.name = team_name
        self.couch = couch_id

    def get_team_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_team_by_id is not None:
            query = """SELECT * FROM team
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
            query = """SELECT * FROM team"""
            try:
                cursor.execute(query)
                connection.commit()

                array = []
                data = cursor.fetchall()
                for team in data:
                    array.append(
                        {
                            'id': team[0],
                            'name': team[1],
                            'couch_id': team[2]
                        }
                        )

                cursor.close()
                connection.close()

                return array

            except connection.Error as error:
                print(error)
                connection.rollback()

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # query to add given country tuple to database
        query = """INSERT INTO team (team_id, team_name, couch_id)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query,(self.id, self.name, self.couch))
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

