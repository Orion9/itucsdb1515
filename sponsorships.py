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
            statement = """SELECT sponsorship.sponsorship_id, sponsorship.sponsorship_name, sponsorship.sponsorship_start_date,
                            sponsorship.sponsorship_league, sponsorship.sponsorship_team, sponsorship.sponsorship_person,
                            person.person_name FROM sponsorship
                            LEFT OUTER JOIN league ON league.league_id = sponsorship.sponsorship_league
                            LEFT OUTER JOIN team ON team.team_id = sponsorship.sponsorship_team
                            LEFT OUTER JOIN person ON person.person_id = sponsorship.sponsorship_person
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
            statement = """SELECT sponsorship.sponsorship_id, sponsorship.sponsorship_name,
                            sponsorship.sponsorship_start_date, sponsorship.sponsorship_league,
                            sponsorship.sponsorship_team, sponsorship.sponsorship_person,
                            league.league_id, league.league_name,
                            team.team_id, team.team_name,
                            person.person_id, person.person_name FROM sponsorship
                            LEFT OUTER JOIN league ON league.league_id = sponsorship.sponsorship_league
                            LEFT OUTER JOIN team ON team.team_id = sponsorship.sponsorship_team
                            LEFT OUTER JOIN person ON person.person_id = sponsorship.sponsorship_person"""
            try:
                cursor.execute(statement, (get_id,))
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
                        'league': sponsorship[7],
                        'team': sponsorship[9],
                        'person': sponsorship[11]
                    }
                )
            cursor.close()
            connection.close()
            return sponsorship_array

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        new_league = None
        new_team = None
        new_person = None

        select_league = """SELECT league_id FROM league WHERE league_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_person = """SELECT person_id FROM person WHERE person_name = %s"""

        statement = """INSERT INTO sponsorship (sponsorship_name, sponsorship_start_date,
                        sponsorship_league, sponsorship_team, sponsorship_person )
                        VALUES (%s, %s, %s, %s, %s)"""
        try:
            cursor.execute(select_league, (self.league,))
            connection.commit()
            new_league = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_person, (self.person,))
            connection.commit()
            new_person = cursor.fetchone()

            cursor.execute(statement, (self.name, self.start_date, new_league, new_team, new_person))
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

    def update_db(self):
        connection = db_connect()
        cursor = connection.cursor()
        status = False

        new_league = None
        new_team = None
        new_person = None

        select_league = """SELECT league_id FROM league WHERE league_name = %s"""
        select_team = """SELECT team_id FROM team WHERE team_name = %s"""
        select_person = """SELECT person_id FROM person WHERE person_name = %s"""

        statement = """UPDATE sponsorship
                       SET sponsorship_name=%s, sponsorship_start_date=%s, sponsorship_league=%s,
                       sponsorship_team=%s, sponsorship_person=%s
                       WHERE sponsorship_id=%s"""

        try:
            cursor.execute(select_league, (self.league,))
            connection.commit()
            new_league = cursor.fetchone()

            cursor.execute(select_team, (self.team,))
            connection.commit()
            new_team = cursor.fetchone()

            cursor.execute(select_person, (self.person,))
            connection.commit()
            new_person = cursor.fetchone()

            cursor.execute(statement, (self.name, self.start_date, new_league, new_team, new_person, self.id))
            connection.commit()
            status = True
        except connection.Error:
            connection.rollback()
            status = False

        cursor.close()
        connection.close()
        return status

