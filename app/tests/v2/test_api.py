import unittest 
from flask import json
from app import create_app
from manage import DatabaseSetup

class TestApi(unittest.TestCase):

    def setUp(self):
        setup = DatabaseSetup
        self.app = create_app(config_name = 'testing')
        self.client = self.app.test_client
        # setup.create_tables()

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

        self.login_attendant = {
            "username" : "kelraf",
            "password" : "kelraf" 
        }

        self.login_admin_invalid = {
            "username" : "admin1234",
            "password" : "admin12" 
        }

        self.delete_att = {
            "username" : "kelvle"
        }

        self.product_info = {
            "name" : "Dell",
            "category" : "Dell",
            "buying_price" : 70000,
            "selling_price" : 80000,
            "description" : "A blue dell"
        }

        self.product_info_ivalid = {
            "name" : "",
            "category" : "Dell",
            "buying_price" : 70000,
            "selling_price" : 80000,
            "description" : " "
        }

        self.sales = {
            "product_id" : 5
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
        data = response23.json
        token = data['access_token']

        response21 = self.client().post("/api/v2/register", data = json.dumps(self.user_info),
         headers = {'Authorization' : 'Bearer'" "+ token} ,
         content_type ="application/json" 
        )

        data = json.loads(response21.get_data().decode())

        self.assertEqual(response21.status_code, 201)

    def test_admin_cannot_create_more_thanone_attendant_with_similar_datails(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        data = response.json
        token = data['access_token']

        response1 = self.client().post("/api/v2/register", data = json.dumps(self.user_infor), content_type = "application/json",
        headers = {"Authorization" : "Bearer" " " + token})

        response2 = self.client().post("/api/v2/register", data = json.dumps(self.user_infor), content_type = "application/json",
        headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response2.status_code, 409)

    def test_admin_can_view_all_attendant(self):

        #These Log in the admin
        response44 = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response44.status_code, 202)

        data = response44.json
        token = data['access_token']

        # data = json.loads(response44.get_data().decode())
        response41 = self.client().get("/api/v2/register", headers = {"Authorization" : "Bearer" " " + token})
        self.assertEqual(response41.status_code, 200)

    def test_admin_can_delete_an_attendant(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response.status_code, 202)

        data = response.json
        token = data['access_token']

        response21 = self.client().delete("/api/v2/register", data = json.dumps(self.delete_att), content_type = "application/json", 
        headers = {"Authorization" : "Bearer" " " + token}  )

        self.assertEqual(response21.status_code, 200)


    def test_admin_cant_delete_an_attendant_that_does_not_exist(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response.status_code, 202)

        data = response.json
        token = data['access_token']

        response21 = self.client().delete("/api/v2/register", data = json.dumps(self.delete_att), content_type = "application/json", 
        headers = {"Authorization" : "Bearer" " " + token}  )

        self.assertEqual(response21.status_code, 404)


    def test_admin_can_get_a_user_by_id(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response.status_code, 202)

        data = response.json
        token = data['access_token']

        response21 = self.client().get("/api/v2/register/112",  headers = {"Authorization" : "Bearer" " " + token}  )

        self.assertEqual(response21.status_code, 200)



    
    def test_admin_cant_get_a_user_by_id_that_does_not_exist(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        self.assertEqual(response.status_code, 202)

        data = response.json
        token = data['access_token']

        response21 = self.client().get("/api/v2/register/1",  headers = {"Authorization" : "Bearer" " " + token}  )

        self.assertEqual(response21.status_code, 404)



    def test_admin_can_create_products(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        data = response.json
        token = data['access_token']

        response2 = self.client().post("/api/v2/products", data = json.dumps(self.product_info), content_type = "application/json",
        headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response2.status_code, 201)



    def test_create_endpoint_returns_an_error_message_on_invalid_product_infor(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        data = response.json
        token = data['access_token']

        response1 = self.client().post("/api/v2/products", data = json.dumps(self.product_info_ivalid), content_type = "application/json",
        headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 409)




    def test_admin_get_all_products(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_admin), content_type = "application/json")
        data = response.json
        token = data['access_token']

        response1 = self.client().get("/api/v2/products",
        headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 200)


    def test_attendant_can_make_sale(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_attendant), content_type = "application/json")
        data = response.json
        token = data['access_token']
        self.assertEqual(response.status_code, 202)

        response1 = self.client().post("/api/v2/sales", data = json.dumps(self.sales), content_type = "application/json", 
        headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 201)



    def test_attendant_can_get_sale_made(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_attendant), content_type = "application/json")
        data = response.json
        token = data['access_token']
        self.assertEqual(response.status_code, 202)

        response1 = self.client().get("/api/v2/sales", headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 200)



    def test_attendant_can_get_sale_made_by_id(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_attendant), content_type = "application/json")
        data = response.json
        token = data['access_token']
        self.assertEqual(response.status_code, 202)

        response1 = self.client().get("/api/v2/sales/2", headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 200)



    def test_attendant_cant_get_sale_made_by_id_that_does_not_exist(self):
        response = self.client().post("/api/v2/login", data = json.dumps(self.login_attendant), content_type = "application/json")
        data = response.json
        token = data['access_token']
        self.assertEqual(response.status_code, 202)

        response1 = self.client().get("/api/v2/sales/57", headers = {"Authorization" : "Bearer" " " + token})

        self.assertEqual(response1.status_code, 404)