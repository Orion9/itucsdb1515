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
    def __init__(self, league_name=None, league_country=None, league_start_date=None, 
                league_id=None):
        self.id = league_id
        self.name = league_name
        self.start_date = league_start_date
        self.country = league_country
       
    def get_league_by_id(self, get_id=None):
        pass

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()
        
        # query to get referenced country by its id
        query_country = """SELECT id FROM country
                                WHERE country_name = %s"""
                             
        # query to add given league tuple to database                     
        query = """INSERT INTO league (league_name, league_start_date, league_country, league_team_number)
                        VALUES (%s, %s, %s, %s)""" 

        try:
            cursor.execute(query_country, (self.country))
            connection.commit()
            country_id = cursor.fetchone()
            
            cursor.execute(query,(self.name, self.start_date, country_id, self.team_count))
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
