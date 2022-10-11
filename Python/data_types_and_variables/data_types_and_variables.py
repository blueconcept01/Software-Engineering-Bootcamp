# Set the variable int_var to some whole number for the int data type
int_var = None

# Set the variable float_var to some decimal number for the float data type
float_var = None

# Set the variable bool_var to some value for boolean
bool_var = None

# Set the str_var to any value for a string
str_var = None

# --- Do Edit Code Below this ---

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_var(self):
        self.assertNotEqual(int_var, None, msg="int_var is still None you have not set int_var yet")
        self.assertEqual(type(int_var), int, msg="int_var is not an int you need to change int_var to an int")

        self.assertNotEqual(float_var, None, msg="float_var is still None you have not set float_var yet")
        self.assertEqual(type(float_var), float, msg="float_var is not an float you need to change float_var to a float")

        self.assertNotEqual(bool_var, None, msg="bool_var is still None you have not set bool_var yet")
        self.assertEqual(type(bool_var), bool, msg="bool_var is not an float you need to change bool_var to a bool")

        self.assertNotEqual(str_var, None, msg="str_var is still None you have not set str_var yet")
        self.assertEqual(type(str_var), str, msg="str_var is not an str you need to change str_var to a str")

unittest.main()