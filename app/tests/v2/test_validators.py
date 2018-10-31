from app.api import Tools
import unittest

class TestValidators(unittest.TestCase):

    def setUp(self):
        self.tools = Tools()

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


    """ Testing Validation of products """

    # def test_success_in_product_validation(self):
    #     response6 = self.tools.validate_products_info("Dell", "Dell", 45555, 5678381)
    #     self.assertEqual(response6, True)
