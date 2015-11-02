###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Sponsorship(object):
    def __init__(self, sponsor_name=None, sponsorship_start_date=None, sponsored_league=None,
                 sponsored_team=None, sponsored_person=None, sponsor_id=None):
        self.id = sponsor_id
        self.name = sponsor_name
        self.start_date = sponsorship_start_date
        self.league = sponsored_league
        self.team = sponsored_team
        self.person = sponsored_person

    def get_sponsorship_by_id(self, get_id=None):

        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT * FROM sponsorship
                            JOIN person ON person.person_id = sponsorship.sponsorship_person
                            WHERE sponsorship_id = %s"""

            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            sponsorship = cursor.fetchone()
            if sponsorship is not None:
                for sponsorship_id, sponsorship_name, sponsorship_start_date, \
                    sponsorship_league, sponsorship_team, sponsorship_person in sponsorship:
                    self.id = sponsorship_id
                    self.name = sponsorship_name
                    self.start_date = sponsorship_start_date
                    self.league = sponsorship_league
                    self.team = sponsorship_team
                    self.person = sponsorship_person
            if sponsorship is not None:
                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        if get_id is None:
            statement = """SELECT * FROM sponsorship
                            JOIN person ON person.person_id = sponsorship.sponsorship_person"""

            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

                sponsorship_array = []
                sponsorship = cursor.fetchall()
                for sponsorship_id, sponsorship_name, sponsorship_start_date, \
                        sponsorship_league, sponsorship_team, sponsorship_person in sponsorship:
                    sponsorship_array.append(
                        {
                            'id': sponsorship_id,
                            'name': sponsorship_name,
                            'start_date': sponsorship_start_date,
                            'league': sponsorship_league,
                            'team': sponsorship_team,
                            'person': sponsorship_person
                        }
                    )
                return sponsorship_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """INSERT INTO sponsorship (sponsorship_name, sponsorship_start_date,
                        sponsorship_league, sponsorship_team, sponsorship_person )
                        VALUES (%s, %s, %s, %s, %s)"""
        person = """SELECT person_id FROM person WHERE person_name = %s"""

        try:
            cursor.execute(person, (self.person,))
            connection.commit()
            person_id = cursor.fetchone()

            cursor.execute(statement, (self.name, self.start_date, self.league, self.team, person_id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


    def delete_from_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """DELETE FROM sponsorship WHERE sponsorship_id = %s"""

        try:
            cursor.execute(statement, (self.id,))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status


