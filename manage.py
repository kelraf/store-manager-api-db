import psycopg2
from psycopg2.extras import RealDictCursor
import os
import sys

db_url = os.getenv('DATABASE_URL')


class DatabaseSetup():

    #Database connection setup
    def __init__(self):
        self.connect = psycopg2.connect(
            database='store-manager', host='localhost', password='kelraf', user='postgres', port='5432'
        )
        self.cursor = self.connect.cursor(cursor_factory = RealDictCursor)
        self.cursor2 = self.connect.cursor()
      
    def create_tables(self):
        queries = self.tables()

        for query in queries:
            try:
                self.cursor.execute(query)
            except psycopg2.ProgrammingError as exc:
                print(exc)
                self.connect.rollback()
            except psycopg2.IntegrityError as exc:
                print(exc)
                self.connect = psycopg2.connect(db_url)
                self.cursor = self.connect.cursor()

        self.connect.commit()
        self.cursor.close()
        self.connect.close()



    #A method to define tables
    def tables(self):

        t1 = """ CREATE TABLE IF NOT EXISTS users (
                    id serial PRIMARY KEY NOT NULL,
                    username VARCHAR (50) NOT NULL,
                    email VARCHAR (100) NOT NULL,
                    phone_number VARCHAR (15) NOT NULL,
                    password VARCHAR (300) NOT NULL,
                    confirm_password VARCHAR (300) NOT NULL )
            """

        t2 = """ CREATE TABLE IF NOT EXISTS products(
                    id serial PRIMARY KEY NOT NULL,
                    product_name VARCHAR (100) NOT NULL,
                    product_category VARCHAR (60) NOT NULL,
                    buying_price double precision NOT NULL,
                    selling_price double precision NOT NULL,
                    description VARCHAR (200) NOT NULL
                )

            """

        t3 = """ CREATE TABLE IF NOT EXISTS sales(
                    id serial PRIMARY KEY NOT NULL,
                    product_name VARCHAR (100) NOT NULL,
                    product_category VARCHAR (60) NOT NULL,
                    product_id double precision NOT NULL,
                    selling_price double precision NOT NULL,
                    description VARCHAR(200) NOT NULL
                )
            """

        queries = [t1, t2, t3]
        return queries
