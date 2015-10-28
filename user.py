###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

import server
from config import db_connect
from passlib.hash import bcrypt


class User(object):
    def __init__(self, user_alias, user_email, user_pass, is_admin=False):
        self.alias = user_alias
        self.email = user_email
        self.password_hash = bcrypt.encrypt(user_pass)
        self.user_type = is_admin


def get_user(email):
        conn = db_connect()
        cursor = conn.cursor()

        query = """SELECT * FROM users WHERE user_email=%s;"""
        try:
            cursor.execute(query, (email,))
            conn.commit()
        except conn.Error as error:
            print(error)

        try:
            user = cursor.fetchone()
        except conn.Error as error:
            user = None
            print(error)

        cursor.close()
        conn.close()

        return user



