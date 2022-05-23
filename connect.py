## Test the postgres connector
# use the config file to connect to database

import psycopg2
from configparser import ConfigParser

DATABASE_ATTRS = {"host":"localhost", "database":"bankruptcies", "user":"db", "password":"admin", "port":"5433"}

def connect():
    """ Connect to PostgresSQL docker container"""
    conn = None
    try:
        #read connection parameters
        params = DATABASE_ATTRS

        #connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        #create a cursoe
        cur = conn.cursor()

        #exexute a statement
        print('PostgresSQL database version:')
        cur.execute('SELECT version()')

        #display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()
                print('Database connection closed.')

#use the copy_from function from pycopg2 to add csv the db
if __name__ == '__main__':
        connect()
