from config import db_connect

class City(object):
    def __init__(self, city_name, city_id=None):
        self.id = city_id
        self.name = city_name

    def get_city(self, name=None):
        conn = db_connect()
        cursor = conn.cursor()

        if name is None:
            query = """SELECT city_name FROM city"""
            try:
                cursor.execute(query)
                conn.commit()
            except conn.Error as error:
                print(error)

            data = cursor.fetchall()

            cursor.close()
            conn.close()

            return data

        else:
            query = """SELECT * FROM city WHERE city_name = %s"""

            try:
                cursor.execute(query, (name, ))
                conn.commit()
            except conn.Error as error:
                print(error)

            data = cursor.fetchone()

            self.id = data[0]
            self.name = data[1]

            return self
