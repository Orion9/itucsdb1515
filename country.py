###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect

class Country (object):
    def __init__(self, country_name=None, country_id=None):
        self.id = country_id
        self.name = country_name
        
    def get_country_by_id(self, get_id=None):
        pass

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()
                             
        # query to add given country tuple to database                     
        query = """INSERT INTO country (country_name)
                        VALUES (%s)""" 

        try:
            cursor.execute(query,(self.name))
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
        pass

    def update_db(self):
        pass