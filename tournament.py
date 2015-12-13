###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################
from config import db_connect


class Tournament (object):
    def __init__(self, tournament_name=None, tournament_matches=None,
                 tournament_start_date=None, tournament_end_date=None,
                 tournament_country=None, tournament_prize=None, tournament_id=None):
        self.id = tournament_id
        self.name = tournament_name
        self.matches = tournament_matches
        self.start_date = tournament_start_date
        self.end_date = tournament_end_date
        self.country = tournament_country
        self.prize = tournament_prize

    def get_tournament_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            query = """SELECT * FROM tournament
                                JOIN country ON country.country_id = tournament.tournament_country
                                WHERE tournament_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                connection.commit()
                data = cursor.fetchone()
                if data is not None:
                    self.id = data[0]
                    self.name = data[1]
                    self.matches = data[2]
                    self.start_date = data[3]
                    self.end_date = data[4]
                    self.country = data[8]
                    self.prize = data[6]

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
            query = """SELECT * FROM tournament
                                JOIN country ON country.country_id = tournament.tournament_country"""
            try:
                cursor.execute(query)
                connection.commit()
            except connection.Error as error:
                print(error)
                connection.rollback()

            array = []
            data = cursor.fetchall()
            for tournament in data:
                array.append(
                    {
                        'id': tournament[0],
                        'name': tournament[1],
                        'matches': tournament[2],
                        'start_date': tournament[3].strftime('%d/%m/%Y'),
                        'end_date': tournament[4].strftime('%d/%m/%Y'),
                        'country': tournament[8],
                        'prize': tournament[6]
                    }
                )



            cursor.close()
            connection.close()

            return array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # query to get referenced country by its id
        query_country = """SELECT country_id FROM country
                                WHERE country_name = %s"""

        # query to add given tournament tuple to database
        query = """INSERT INTO tournament (tournament_name, tournament_matches, tournament_start_date, tournament_end_date,
                                       tournament_country, tournament_prize)
                        VALUES (%s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(query_country, (self.country,))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.matches, self.start_date, self.end_date, country_id, self.prize))
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

        query = """DELETE FROM tournament WHERE tournament_id = %s"""

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
        query = """UPDATE tournament
                   SET tournament_name=%s, tournament_matches=%s, tournament_start_date=%s, tournament_end_date=%s, tournament_country=%s, tournament_prize=%s
                   WHERE tournament_id=%s"""

        try:
            cursor.execute(query_country, (self.country, ))
            connection.commit()
            country_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.matches, self.start_date, self.end_date, country_id, self.prize, self.id,))
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
