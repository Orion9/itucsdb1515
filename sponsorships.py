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

            s_data = cursor.fetchone()
            if s_data is not None:
                self.id = s_data[0]
                self.name = s_data[1]
                self.start_date = s_data[2]
                self.league = s_data[3]
                self.team = s_data[4]
                self.person = s_data[5]
                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT * FROM sponsorship
                            JOIN person ON person.person_id = sponsorship.sponsorship_person"""

            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            sponsorship_array = []
            s_data = cursor.fetchall()
            for sponsorship in s_data:
                sponsorship_array.append(
                    {
                        'id': sponsorship[0],
                        'name': sponsorship[1],
                        'start_date': sponsorship[2].strftime('%d/%m/%Y'),
                        'league': sponsorship[3],
                        'team': sponsorship[4],
                        'person': sponsorship[5]
                    }
                )
            print(sponsorship_array)
            cursor.close()
            connection.close()
            return sponsorship_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """INSERT INTO sponsorship (sponsorship_name, sponsorship_start_date,
                        sponsorship_league, sponsorship_team, sponsorship_person )
                        VALUES (%s, %s, %s, %s, %s)"""
        person_to_add = """SELECT person_id FROM person WHERE person_name = %s"""

        try:
            cursor.execute(person_to_add, (self.person,))
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


