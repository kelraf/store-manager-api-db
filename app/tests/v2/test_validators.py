from app.api import Tools
from app.api.v2.models.users import UserDetails
import unittest

class TestValidators(unittest.TestCase):

    def setUp(self):
        self.tools = Tools()
        self.users = UserDetails()

    def test_validation_successful(self):
        response = self.tools.validate_user_info("kelraf", "rafwa@gmail.com", "0718089771", "kelraf", "kelraf")
        self.assertEqual(response, True)

    def test_validation_with_invalid_username(self):
        response1 = self.tools.validate_user_info("kel$f", "rafwa@gmail.com", "0718089771", "kelraf", "kelraf")
        self.assertEqual(response1, "Username can only contain alphanumeric characters")

    def test_validation_with_invalid_email(self):
        response2 = self.tools.validate_user_info("kelraf", "rafwagmail.com", "0718089771", "kelraf", "kelraf")
        self.assertEqual(response2, "Invalid Email")

    def test_validation_with_username_less_than_six_characters(self):
        response3 = self.tools.validate_user_info("keraf", "rafwa@gmail.com", "0718089771", "kelraf", "kelraf")
        self.assertEqual(response3, "Username should be atleast six characters long")

    def test_validation_with_password_with_less_than_six_characters(self):
        response4 = self.tools.validate_user_info("kelraf", "rafwa@gmail.com", "0718089771", "kelr", "kelraf")
        self.assertEqual(response4, "Password should be atleast six characters long")

    def test_validation_with_unmatching_passwords(self):
        response5 = self.tools.validate_user_info("kelraf", "rafwa@gmail.com", "0718089771", "kelref", "kelraf")
        self.assertEqual(response5, "Your Passwords Should match")


    """ Testing Registration of users """

    def test_successful_user_registration(self):
        response6 = self.users.register("kelraf", "kel@gmail.com", "0700234912", "kelraf", "kelraf")
        self.assertEqual(response6, True)

    def test_user_registration_with_invalid_info(self):
        response7 = self.users.register("kelrtf", "kelgmail.com", "0703234912", "kelraf", "kelraf")

        self.assertEqual(response7, "Invalid Email")

    def test_user_cant_be_created_twice(self):
        response8 = self.users.register("kelraf", "kel@gmail.com", "0700234912", "kelraf", "kelraf")

        self.assertEqual(response8, "User already Exists")

    def test_successfull_login(self):
        response9 = self.users.login("admin1234")
        self.assertTrue(response9)

    def test_login_with_invalid_info(self):
        response10 = self.users.login("admin12")
        self.assertEqual(response10, "User admin12, does not exist")

    def test_getting_all_users(self):
        response11 = self.users.get_all_users()

        self.assertTrue(response11)

    def test_get_user_by_id_unsuccessfull(self):
        response12 = self.users.get_user_id(162)
        self.assertFalse(response12)

    def test_successfull_deletion_of_user(self):
        response13 = self.users.delete_user("kelraf")
        self.assertEqual(response13, True)

    def test_unsuccessfull_deletion_of_user(self):
        response13 = self.users.delete_user("kelraf")
        self.assertTrue(response13)

    def test_get_user_by_username(self):
        response14 = self.users.get_user_by_email("admin1234")

        self.assertEqual(response14, True)
