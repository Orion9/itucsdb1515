__author__ = "ITUCSDB1515"

import psycopg2

"""DBConnect method is the main method for database connection.
    In order to avoid writing down the db information over and over again,
    a main method has been used. Every time a DBConnect method is called,
    a main method has been used. Every time a DBConnect method is called,
    a database connection can be achieved. And queries can be send through that object.
    It is also good way to avoid global variables.

    Usage: After created an DBConnect object call db_connect method.
            connection = config.db_connect()"""


def db_connect():
    user_name = "postgres"
    password = "password"
    db_name = "itucsdb1515"
    host = "localhost"
    port = "5432"

    try:
        db_connection = psycopg2.connect(database=db_name, user=user_name,
                                         password=password, host=host, port=port)
    except psycopg2.Error as error:
        pass

    return db_connection
