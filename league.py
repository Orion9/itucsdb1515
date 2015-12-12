###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################
from config import db_connect


class League (object):
    def __init__(self, league_name=None, league_country=None,
                 league_start_date=None, league_id=None):
        self.id = league_id
        self.name = league_name
        self.start_date = league_start_date
        self.country = league_country
       
    def get_league_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM league
                                JOIN country ON country.country_id = league.league_country
                                WHERE league_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.start_date = data[3]
                    self.country = data[5]

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
            query = """SELECT * FROM league
                                JOIN country ON country.country_id = league.league_country"""
            try:
                cursor.execute(query)
                connection.commit()
            except connection.Error as error:
                print(error)
                connection.rollback()

            array = []
            data = cursor.fetchall()
            for league in data:
                array.append(
                    {
                        'id': league[0],
                        'name': league[1],
                        'start_date': league[3].strftime('%d/%m/%Y'),
                        'country': league[5]
                    }
                )
            print(array)

            cursor.close()
            connection.close()

            return array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()
        
        # query to get referenced country by its id
        query_country = """SELECT country_id FROM country
                                WHERE country_name = %s"""
                             
        # query to add given league tuple to database                     
        query = """INSERT INTO league (league_name, league_country, league_start_date)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query_country, (self.country,))
            connection.commit()
            country_id = cursor.fetchone()
            
            cursor.execute(query, (self.name, country_id, self.start_date,))
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

        query = """DELETE FROM league WHERE league_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
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

        query_country = """SELECT country_id FROM country WHERE country_name=%s"""
        query = """UPDATE league
                   SET league_name=%s, league_country=%s, league_start_date=%s
                   WHERE league_id=%s"""

        try:
            cursor.execute(query_country, (self.country, ))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (self.name, country_id, self.start_date, self.id,))
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

