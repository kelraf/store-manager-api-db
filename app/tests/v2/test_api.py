import unittest 
from flask import json
from app import create_app
from manage import DatabaseSetup as setup

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name = 'testing')
        self.client = self.app.test_client
        # setup.create_tables(self)

        self.user_info = {
            "username" : "kelvle",
            "email" : "kelvole@gmail.com",
            "phone_number" : "0723657456",
            "password" : "kelvol",
            "confirm_password" : "kelvol"
        }

        self.user_infor = {
            "username" : "kelvolu",
            "email" : "kelvolu@gmail.com",
            "phone_number" : "0723657453",
            "password" : "kelvolu",
            "confirm_password" : "kelvolu"
        }

        self.user_login = {
            "username" : "kelvolu",
            "password" : "kelvolu"
        }

        self.login_admin = {
            "username" : "admin1234",
            "password" : "admin1234" 
        }

        self.login_admin_invalid = {
            "username" : "admin1234",
            "password" : "admin12" 
        }

        self.product_info = {
            "name" : "Dell",
            "category" : "Dell",
            "buying_price" : 70000,
            "selling_price" : 80000,
            "description" : "A blue dell"
        }

    

    def test_login_of_admin(self):
        response23 = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertAlmostEqual(response23.status_code, 202)

    def test_login_of_admin_with_invalid_password(self):
        response12 = self.client().post("/api/v2/login", data = json.dumps(self.login_admin_invalid), content_type = "application/json")

        self.assertAlmostEqual(response12.status_code, 404)

    def test_admin_can_create_attendant(self):
        response23 = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response23.status_code, 202)
        
        data = json.loads(response23.get_data().decode("UTF-8"))
        token = data['access_token']

        response21 = self.client().post("/api/v2/register", data = json.dumps(self.user_info),
         headers = {'Authentication' : 'Bearer'+ token} ,
         content_type ="application/json" 
        )

        data = json.loads(response21.get_data().decode())

        self.assertEqual(data, 200)

    # def test_user_registration(self):
    #     response = self.client().post("/api/v2/register", data = json.dumps(self.user_info), content_type = "application/json")

        # self.assertEqual(response.status_code, 201)

    # def test_cant_create_user_twice(self):
    #     response1 = self.client().post("/api/v2/login", data = json.dumps(self.user_login), content_type = "application/json")
    #     data = response1.json

    #     self.assertEqual(data['message'], "Successfully Logged in as kelvole")

    # def test_product_creating(self):

    #     response4 = self.client().post("/api/v2/register", data = json.dumps(self.user_infor), content_type = "application/json")

    #     response2 = self.client().post("/api/v2/login", data = json.dumps(self.user_login), content_type = "application/json")
    #     data = response2.json

    #     token = data["access_token"]

    #     response3 = self.client().post("/api/v2/products", data = json.dumps(self.product_info),
    #     content_type = "application/json",
    #     headers={'Authorization': 'Bearer ' + token})

    #     self.assertEqual(response3.status_code, 201)


    # def tearDown(self):
    #     setup.delete_tables(self)
