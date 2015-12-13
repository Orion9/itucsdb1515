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
    def __init__(self, country_name=None, country_population=None, capital=None, country_id=None):
        self.id = country_id
        self.name = country_name
        self.population = country_population
        self.capital = capital
        
    def get_country_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM country
                            JOIN city ON country.capital=city.city_id
                            WHERE country_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.population = data[2]
                    self.capital = data[5]

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
            query = """SELECT * FROM country
                            JOIN city ON country.capital = city.city_id"""
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
                            'population': country[2],
                            'capital': country[5]
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

        query_capital = """SELECT city_id FROM city
                                    WHERE city_name = %s"""

        query = """INSERT INTO country (country_name, country_population, capital)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query_capital,(self.capital,))
            connection.commit()
            capital_id = cursor.fetchone()

            cursor.execute(query,(self.name, self.population, capital_id))
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

        query_capital = """ SELECT city_id FROM city
                                WHERE city_name = %s"""
        
        query = """UPDATE country
                   SET country_name=%s, country_population=%s, capital=%s
                   WHERE country_id=%s"""

        try:
            cursor.execute(query_capital, (self.capital,))
            connection.commit()
            capital_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.population, capital_id, self.id,))
            connection.commit()
            status = True

        except connection.Error as error:
            print(error)
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status
