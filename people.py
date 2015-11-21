###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect


class Person(object):
    def __init__(self, name=None, birth_date=None, birth_place=None, user_type=None, user_id=None):
        self.id = user_id
        self.name = name
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.type = user_type

    def get_person_by_id(self, get_id=None):
        conn = db_connect()
        cursor = conn.cursor()

        if get_id is not None:
            query = """SELECT * FROM person
                                JOIN city ON city.city_id = person.person_birth_location
                                JOIN person_types ON person_types.id = person.person_type
                                WHERE person_id = %s"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.birth_date = data[2]
                self.birth_place = data[6]
                self.type = data[10]

                cursor.close()
                conn.close()

                return self

            else:
                cursor.close()
                conn.close()

                return None

        else:
            query = """SELECT * FROM person
                                JOIN city ON city.city_id = person.person_birth_location
                                JOIN person_types ON person_types.id = person.person_type"""
            try:
                cursor.execute(query, (get_id,))
                conn.commit()
            except conn.Error as error:
                print(error)
                conn.rollback()

            data_array = []
            data = cursor.fetchall()
            for person in data:
                data_array.append(
                    {
                        'id': person[0],
                        'name': person[1],
                        'birth_date': person[2].strftime('%d/%m/%Y'),
                        'birth_place': person[6],
                        'type':  person[10]
                    }
                )

            # print(data_array)
            cursor.close()
            conn.close()

            return data_array

    def add_to_db(self):
        conn = db_connect()
        cursor = conn.cursor()

        query_type = """SELECT id FROM person_types WHERE person_type_name = %s"""
        query_city = """SELECT city_id FROM city WHERE city_name = %s"""
        query = """INSERT INTO person(person_name, person_birth_date, person_birth_location, person_type)
                            VALUES (%s, %s, %s, %s)"""

        try:
            cursor.execute(query_type, (self.type,))
            conn.commit()
            type_id = cursor.fetchone()

            cursor.execute(query_city, (self.birth_place,))
            conn.commit()
            city_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.birth_date, city_id, type_id))
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

        query = """DELETE FROM person WHERE person_id = %s"""

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

        query_city = """SELECT city_id FROM city WHERE city_name=%s"""
        query_type = """SELECT id FROM person_types WHERE person_type_name=%s"""
        query = """UPDATE person
                   SET person_name=%s, person_birth_date=%s, person_birth_location=%s, person_type=%s
                   WHERE person_id=%s"""

        try:
            cursor.execute(query_city, (self.birth_place, ))
            conn.commit()
            city_id = cursor.fetchone()

            cursor.execute(query_type, (self.type, ))
            conn.commit()
            type_id = cursor.fetchone()

            cursor.execute(query, (self.name, self.birth_date, city_id, type_id, self.id))
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


class PersonType(object):
    def __init__(self, type_name=None, type_id=None):
        self.id = type_id
        self.type = type_name

    def get_person_type(self, type_id=None):
        conn = db_connect()
        cursor = conn.cursor()
        types = None

        if type_id is None:
            query_type = """SELECT person_type_name FROM person_types"""

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
            query_type = """SELECT person_type_name FROM person_types WHERE id=%s"""

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

        query = """INSERT INTO person_types(person_type_name) VALUES (%s)"""

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
