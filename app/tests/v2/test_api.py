import unittest 
from flask import json
from app import create_app

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name = 'testing')
        self.client = self.app.test_client

    user_info = {
        "username" : "kelvole",
        "email" : "kelvole@gmail.com",
        "phone_number" : "0723657456",
        "password" : "kelvol",
        "confirm_password" : "kelvol"
    }

    user_infor = {
        "username" : "kelvolu",
        "email" : "kelvolu@gmail.com",
        "phone_number" : "0723657453",
        "password" : "kelvolu",
        "confirm_password" : "kelvolu"
    }

    user_login = {
        "username" : "kelvolu",
        "password" : "kelvolu"
    }

    product_info = {
        "name" : "Dell",
        "category" : "Dell",
        "buying_price" : 70000,
        "selling_price" : 80000,
        "description" : "A blue dell"
    }

    def test_user_registration(self):
        response = self.client().post("/api/v2/register", data = json.dumps(self.user_info), content_type = "application/json")

        self.assertEqual(response.status_code, 201)

    def test_cant_create_user_twice(self):
        response1 = self.client().post("/api/v2/login", data = json.dumps(self.user_login), content_type = "application/json")
        data = response1.json

        self.assertEqual(data['message'], "Successfully Logged in as kelvole")

    def test_product_creating(self):

        response4 = self.client().post("/api/v2/register", data = json.dumps(self.user_infor), content_type = "application/json")

        response2 = self.client().post("/api/v2/login", data = json.dumps(self.user_login), content_type = "application/json")
        data = response2.json

        token = data["access_token"]

        response3 = self.client().post("/api/v2/products", data = json.dumps(self.product_info),
        content_type = "application/json",
        headers={'Authorization': 'Bearer ' + token})

        self.assertEqual(response3.status_code, 201)