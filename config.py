import psycopg2

"""DBConnect Class is the main class for database connection.
    In order to avoid writing down the db information over and over again,
    a main class has been used. Every time a DBConnect object is created,
    a database connection can be achieved. And queries can be send through that object.
    It is also good way to avoid global variables.

    Usage: After created an DBConnect object call db_connect method.
            db_conn_obj = DBConnect()
            connection = db_conn_obj.db_connect()"""


class DBConnect(object):
    user_name = "postgres"
    password = "password"
    db_name = "itucsdb1515"
    host = "localhost"
    port = "5432"

    def db_connect(self):
        try:
            db_connection = psycopg2.connect(database=self.db_name, user=self.user_name,
                                             password=self.password, host=self.host, port=self.port)
        except psycopg2.Error as error:
            pass

        return db_connection
