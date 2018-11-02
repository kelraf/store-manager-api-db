import psycopg2
from psycopg2.extras import RealDictCursor
import os
import sys
from werkzeug.security import generate_password_hash

# db_url = os.getenv('DATABASE_URL')

db_url = os.environ['DATABASE_URL'],sslmode='required'

class DatabaseSetup():

    #Database connection setup
    def __init__(self):
        self.connect = psycopg2.connect( )
        self.cursor = self.connect.cursor(cursor_factory = RealDictCursor)
      
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
        


    def create_admin(self):
        #A dict to store admin details
        admin_info = {}
        hash_pass1 = generate_password_hash("admin1234", method='pbkdf2:sha256')
        hash_pass2 = generate_password_hash("admin1234", method='pbkdf2:sha256')

        admin_info['username'] = "admin1234"
        admin_info['email'] = "admin@gmail.com"
        admin_info['phone_number'] = "0712345763"
        admin_info['admin'] = True
        admin_info['password'] = hash_pass1
        admin_info['confirm_password'] = hash_pass2

        query = """ INSERT INTO users(username, email, phone_number, admin, password, confirm_password)
                VALUES(%s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(query, (admin_info['username'], admin_info['email'], admin_info['phone_number'],
                     admin_info['admin'], admin_info['password'], admin_info['confirm_password']))
        self.connect.commit()   

    def delete_test_admin(self, username):
        query = """ DELETE FROM users WHERE username = %s """
        self.cursor.execute(query, (username,))
        self.connect.commit()

    def delete_tables(self):
        """Delete tables"""

        table_1 = """DROP TABLE IF EXISTS users CASCADE"""
        table_2 = """DROP TABLE IF EXISTS products CASCADE"""
        table_3 = """DROP TABLE IF EXISTS sales CASCADE"""

        # Add all tables to the queries list
        queries = [table_1, table_2, table_3]

        for query in queries:
            self.cursor.execute(query)
        self.connect.commit()

       
   

    #A method to define tables
    def tables(self):

        t1 = """ CREATE TABLE IF NOT EXISTS users (
                    id serial PRIMARY KEY NOT NULL,
                    username VARCHAR (50) NOT NULL,
                    email VARCHAR (100) NOT NULL,
                    phone_number VARCHAR (15) NOT NULL,
                    admin boolean NOT NULL,
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


