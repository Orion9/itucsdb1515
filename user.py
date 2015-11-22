###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################


from config import db_connect
from passlib.hash import bcrypt


class User(object):
    def __init__(self, user_alias=None, user_email=None, user_pass=None, is_admin=False, user_id=None):
        self.id = user_id
        self.alias = user_alias
        self.email = user_email

        if user_pass is not None:
            self.password_hash = bcrypt.encrypt(user_pass)
        else:
            self.password_hash = user_pass

        self.user_type = is_admin

    def get_user(self, email=None):
            conn = db_connect()
            cursor = conn.cursor()

            if email is not None:
                query = """SELECT * FROM users WHERE user_email=%s;"""
                try:
                    cursor.execute(query, (email,))
                    conn.commit()
                except conn.Error as error:
                    print(error)
                    conn.rollback()

                user_data = cursor.fetchone()
                if user_data is not None:
                    self.id = user_data[0]
                    self.alias = user_data[1]
                    self.email = user_data[3]
                    self.password_hash = user_data[2]
                    self.user_type = user_data[4]

                cursor.close()
                conn.close()

                return self

            else:
                query = """SELECT * FROM users"""
                try:
                    cursor.execute(query)
                    conn.commit()
                except conn.Error as error:
                    print(error)
                    conn.rollback()

                user_data = cursor.fetchall()

                cursor.close()
                conn.close()

                return user_data

    def add_user_to_db(self):
                conn = db_connect()
                cursor = conn.cursor()

                try:
                    cursor.execute(
                        """INSERT INTO users (user_name, password_hash, user_email, is_admin)
                           VALUES (%s, %s, %s, %s);""",
                        (self.alias, self.password_hash, self.email, self.user_type)
                    )
                    conn.commit()

                    status = 'success'

                except conn.Error as error:
                    print(error)
                    status = 'user already there'

                cursor.close()
                conn.close()

                return status
