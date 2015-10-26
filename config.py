###############################
# Author: ITUCSDB1515         #
# Oguz Kerem Tural 150130125  #
# Umut Can Ozyar 150130022    #
# Mert Seker 150130119        #
# Furkan Akgun 150130106      #
# Emine Oyku Bozkir 150120017 #
###############################

import os
import re
import json

from psycopg2 import *


def get_elephantsql_dsn(vcap_services):

    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


##########################################################################################
#  DBConnect method is the main method for database connection.                          #
#  In order to avoid writing down the db information over and over again,                #
#  a main method has been used. Every time a DBConnect method is called,                 #
#  a main method has been used. Every time a DBConnect method is called,                 #
#  a database connection can be achieved. And queries can be send through that object.   #
#  It is also good way to avoid global variables.                                        #
#                                                                                        #
#  Usage: After created an DBConnect object call db_connect method.                      #
#           connection = config.db_connect()                                             #
##########################################################################################
def db_connect():
    # Connecting db by checking VCAP credentials. By courtesy of Turgut Hoca. #
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        dsn = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        # Change this line according to your local db credentials #
        dsn = """user='postgres' password='password'
                               host='localhost' port=5432 dbname='itucsdb1515'"""

    try:
        db_connection = connect(dsn)
        return db_connection
    except Error as error:
        print(error)
        return None
