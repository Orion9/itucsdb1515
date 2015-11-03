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
    def __init__(self, sponsorship_name=None, sponsorship_start_date=None, sponsorship_league=None,
                 sponsorship_team=None, sponsorship_person=None, sponsorship_id=None):
        self.id = sponsorship_id
        self.name = sponsorship_name
        self.start_date = sponsorship_start_date
        self.league = sponsorship_league
        self.team = sponsorship_team
        self.person = sponsorship_person

    def get_sponsorship_by_id(self, get_id=None):
        connection = db_connect()
        cursor = connection.cursor()

        if get_id is not None:
            statement = """SELECT * FROM sponsorship
                            WHERE sponsorship_id = %s"""
            try:
                cursor.execute(statement, (get_id,))
                connection.commit()
            except connection.Error:
                connection.rollback()

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.start_date = data[2]
                self.league = data[3]
                self.team = data[4]
                self.person = data[5]
                cursor.close()
                connection.close()
                return self
            else:
                cursor.close()
                connection.close()
                return None

        else:
            statement = """SELECT * FROM sponsorship"""
            try:
                cursor.execute(statement)
                connection.commit()
            except connection.Error:
                connection.rollback()

            sponsorship_array = []
            data = cursor.fetchall()
            for sponsorship in data:
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
            #print(sponsorship_array)
            cursor.close()
            connection.close()
            return sponsorship_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        statement = """INSERT INTO sponsorship (sponsorship_name, sponsorship_start_date,
                        sponsorship_league, sponsorship_team, sponsorship_person )
                        VALUES (%s, %s, %s, %s, %s)"""
        try:
            cursor.execute(statement, (self.name, self.start_date, self.league, self.team, self.person))
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


