import unittest
import useful_functions


class TestUsefulFunctions(unittest.TestCase):
    def test_contains_numbers(self):
        result = useful_functions.contains_numbers("Contains 1 number")
        self.assertTrue(result, "Input contains an integer")

        result = useful_functions.contains_numbers("Contains no number")
        self.assertFalse(result, "Input contains an integer")

    def test_not_empty(self):
        result = useful_functions.not_empty("Not empty")
        self.assertTrue(result, "String is empty")

        result = useful_functions.not_empty("")
        self.assertFalse(result, "String is not empty")

    def test_is_email(self):
        result = useful_functions.is_email("Luyanda@gmail.com")
        self.assertTrue(result, "Email does not meet requirements")

        result = useful_functions.is_email("LuyandaAtGmailDotCom")
        self.assertFalse(result, "Email does meet the requirements")

    def test_id_valid(self):
        result = useful_functions.id_valid("9903155793082")
        self.assertTrue(result, "Id is invalid")

        result = useful_functions.id_valid("1999031793082")
        self.assertFalse(result, "Id is not invalid")

    def test_generate_random_number(self):
        result = useful_functions.generate_random_number()
        if 1 <= result >= 49:
            self.assertTrue(result, "Something went wrong")
