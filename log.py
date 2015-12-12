###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################
from config import db_connect


class Log (object):
    def __init__(self, log_description=None, log_author=None, log_time=None, log_id=None):
        self.id = log_id
        self.description = log_description
        self.author = log_author
        self.time = log_time

    def get_log_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM log
                            JOIN users ON log.log_author = users.user_id
                            WHERE log_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()

                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.description = data[1]
                    self.time = data[3]
                    self.author = data[5]
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
            query = """SELECT * FROM log
                            JOIN users ON log.log_author = users.user_id"""
            try:
                cursor.execute(query)
                connection.commit()

                array = []
                data = cursor.fetchall()
                for log in data:
                    array.append(
                        {
                            'id': log[0],
                            'description': log[1],
                            'time': log[3].strftime('%d/%m/%Y'),
                            'author': log[5]
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

        # query to get referenced user by its id
        query_user = """SELECT user_id FROM users
                                WHERE user_name = %s"""

        # query to add given log tuple to database
        query = """INSERT INTO log (log_description, log_author, log_time)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query_user, (self.author,))
            connection.commit()
            user_id = cursor.fetchone()

            cursor.execute(query, (self.description, user_id, self.time,))
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

        query = """DELETE FROM log WHERE log_id = %s"""

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

