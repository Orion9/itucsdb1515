###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

from config import db_connect
import requests


class City(object):
    def __init__(self, city_name=None, city_population=None, city_coordinates=None, city_id=None):
        self.id = city_id
        self.name = city_name
        self.coordinates = city_coordinates
        self.population = city_population

    def get_city_by_id(self, city_id=None):
        conn = db_connect()
        cursor = conn.cursor()

        if city_id is None:
            query = """SELECT * FROM city"""
            try:
                cursor.execute(query)
                conn.commit()
            except conn.Error as error:
                print(error)

            data_array = []
            data = cursor.fetchall()
            for city in data:
                data_array.append(
                    {
                        'id': city[0],
                        'name': city[1],
                        'coordinates': city[2],
                        'population':  city[3]
                    }
                )
            # print(data)

            cursor.close()
            conn.close()

            return data_array

        else:
            query = """SELECT * FROM city WHERE city_id = %s"""

            try:
                cursor.execute(query, (city_id, ))
                conn.commit()
            except conn.Error as error:
                print(error)

            data = cursor.fetchone()
            if data is not None:
                self.id = data[0]
                self.name = data[1]

            return self

    def add_to_db(self):
        connection = db_connect()
        cursor = connection.cursor()

        # Get geocode using Google Maps API #
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {'sensor': 'false', 'address': self.name, 'key': 'AIzaSyCZGB4LyytNSiSk3hsmIrgM0ikaOO3NMUs'}
        print(params)

        respond = requests.get(url, params=params)

        respond_data = respond.json()
        print(respond_data)

        result_data = respond_data['results']
        location = result_data[0]['geometry']['location']
        self.coordinates = str(location['lat']) + "," + str(location['lng'])

        # query to add given country tuple to database
        query = """INSERT INTO city (city_name, city_population, city_coordinates)
                        VALUES (%s, %s, %s)"""

        try:
            cursor.execute(query, (self.name, self.population, self.coordinates))
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

        query = """DELETE FROM city WHERE city_id = %s"""

        try:
            cursor.execute(query, (self.id,))
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

        # Get geocode using Google Maps API #
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {'sensor': 'false', 'address': self.name, 'key': 'AIzaSyCZGB4LyytNSiSk3hsmIrgM0ikaOO3NMUs'}
        # print(params)

        respond = requests.get(url, params=params)

        respond_data = respond.json()
        # print(respond_data)

        result_data = respond_data['results']
        location = result_data[0]['geometry']['location']
        self.coordinates = str(location['lat']) + "," + str(location['lng'])

        query = """UPDATE city
                   SET city_name=%s, city_population=%s, city_coordinates=%s
                   WHERE city_id=%s"""

        try:
            cursor.execute(query, (self.name, self.population, self.coordinates, self.id))
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
