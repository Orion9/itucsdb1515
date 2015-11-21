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
    def __init__(self, country_name=None, country_population=None, country_id=None):
        self.id = country_id
        self.name = country_name
        self.population = country_population
        
    def get_country_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM country
                            WHERE country_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.population = data[2]
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
            query = """SELECT * FROM country"""
            try:
                cursor.execute(query)
                connection.commit()
                
                array = []
                data = cursor.fetchall()
                for country in data:
                    array.append(
                        {
                            'id': country[0],
                            'name': country[1],
                            'population': country[2]
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
        query = """INSERT INTO country (country_name, country_population)
                        VALUES (%s, %s)""" 

        try:
            cursor.execute(query,(self.name, self.population,))
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

        query = """DELETE FROM country WHERE country_id = %s"""

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
        
        query = """UPDATE country
                   SET country_name=%s, country_population=%s
                   WHERE country_id=%s"""

        try:
            cursor.execute(query, (self.name, self.population, self.id,))
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
