# Create code to test if people are as old or older then 21
# replace where None is with a boolean statement that tests people's age

age = 34

if None: # edit this code so that you can test if the person is as old as 34 years old
    output = "This person is old enough to drink"
else:
    output = "This person can't drink"

print(output)

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_if(self):
        self.assertEqual(output, "This person is old enough to drink", msg="You have not implemented line number 6 correctly for age 34 to be true")

unittest.main()