###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Penalty(object):
    def __init__(self, given_person=None, given_date=None, penalty_type=None, penalty_id=None):
        self.id = penalty_id
        self.person = given_person
        self.given_date = given_date
        self.type = penalty_type

    def get_penalty_by_id(self, get_id=None):
        conn = db_connect()
        cursor = conn.cursor()

        if get_id is not None:
            query = """SELECT * FROM penalty
                                JOIN person ON penalty_given_person = person.person_id
                                JOIN penalty_type ON penalty_type = penalty_type.id
                                WHERE penalty_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data = cursor.fetchone()
            print(data)
            if data is not None:
                self.id = data[0]
                self.person = data[5]
                self.given_date = data[3]
                self.type = data[10]

                cursor.close()
                conn.close()

                return self

            else:
                cursor.close()
                conn.close()

                return None

        else:
            query = """SELECT * FROM penalty
                                JOIN person ON penalty_given_person = person.person_id
                                JOIN penalty_type ON penalty_type.id = penalty.penalty_type"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data_array = []
            data = cursor.fetchall()
            print(data)
            for penalty in data:
                data_array.append(
                    {
                        'id': penalty[0],
                        'person': penalty[5],
                        'given_date': penalty[3].strftime("%d/%m/%Y"),
                        'type':  penalty[10]
                    }
                )

            print(data_array)
            cursor.close()
            conn.close()

            return data_array

    def add_to_db(self):
        conn = db_connect()
        cursor = conn.cursor()

        query_type = """SELECT id FROM penalty_type WHERE penalty_type_name = %s"""
        query = """INSERT INTO penalty(penalty_type, penalty_given_person, penalty_given_date)
                            VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query_type, (self.type,))
            conn.commit()
            type_id = cursor.fetchone()

            print(self.person, type_id, self.given_date)
            cursor.execute(query, (type_id, self.person, self.given_date))
            conn.commit()
            status = True

        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False

        cursor.close()
        conn.close()
        return status

    def delete_from_db(self):
        conn = db_connect()
        cursor = conn.cursor()

        query = """DELETE FROM penalty WHERE penalty_id = %s"""

        try:
            cursor.execute(query, (self.id, ))
            conn.commit()
            status = True

        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False

        cursor.close()
        conn.close()
        return status

    def update_db(self):
        conn = db_connect()
        cursor = conn.cursor()
        status = False

        query_type = """SELECT id FROM penalty_type WHERE penalty_type_name=%s"""
        query = """UPDATE penalty
                   SET penalty_given_date=%s, penalty_given_person=%s, penalty_type=%s
                   WHERE penalty_id=%s"""

        try:
            cursor.execute(query_type, (self.type, ))
            conn.commit()
            type_id = cursor.fetchone()

            cursor.execute(query, (self.given_date, self.person, type_id, self.id))
            conn.commit()
            print(cursor.mogrify(query, (self.given_date, self.person, type_id, self.id)))
            status = True
        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False
        finally:
            cursor.close()
            conn.close()
            return status


class PenaltyType(object):
    def __init__(self, type_name=None, type_id=None):
        self.id = type_id
        self.type = type_name

    def get_penalty_type(self, type_id=None):
        conn = db_connect()
        cursor = conn.cursor()
        types = None

        if type_id is None:
            query_type = """SELECT penalty_type.penalty_type_name FROM penalty_type"""

            try:
                cursor.execute(query_type)
                conn.commit()
                types = cursor.fetchall()

            except conn.Error as error:
                print(error)
                conn.rollback()

                cursor.close()
                conn.close()

            return types

        else:
            query_type = """SELECT penalty_type.penalty_type_name FROM penalty_type WHERE id=%s"""

            try:
                cursor.execute(query_type, (type_id, ))
                conn.commit()
                types = cursor.fetchone()

                if types is not None:
                    self.id = type_id
                    self.type = types[0]

            except conn.Error as error:
                print(error)
                conn.rollback()

                cursor.close()
                conn.close()

            return self

    def add_to_db(self):
        conn = db_connect()
        cursor = conn.cursor()
        status = False

        query = """INSERT INTO penalty_type(penalty_type_name) VALUES (%s)"""

        try:
            cursor.execute(query, (self.type, ))
            conn.commit()
            status = True
        except conn.Error as error:
            print(error)
            conn.rollback()
            status = False
        finally:
            cursor.close()
            conn.close()
            return status
