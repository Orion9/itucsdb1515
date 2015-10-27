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

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]
                self.birth_date = data[2]
                self.birth_place = data[6]
                self.type = data[9]

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

            data_array = []
            data = cursor.fetchall()
            for person in data:
                data_array.append(
                    {
                        'id': person[0],
                        'name': person[1],
                        'birth_date': person[2].strftime('%d/%m/%Y'),
                        'birth_place': person[6],
                        'type':  person[9]
                    }
                )

            print(data_array)
            cursor.close()
            conn.close()

            return data_array


def add_person(person_obj):
    pass