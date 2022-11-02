
"""
User will input two parameters.

Concept:  If we try to add a string to a integer, then it should raise TypeError.
'100' + 5
# TypeError: can only concatenate str (not “int”) to str

Write a function that will take two parameter. Use try and except. 
If the parameters are not of same type, then return 'Type Error'
If parameters are of same type, perform + operation.

Example: If the parameters are 1 and 2, then output should be 3.
         If the parameters are 1 and 'abc', then it should return TypeError.

"""
def TypeError(para1, para2):
  pass

"""
User will input one parameter(integer).

Concept:  If we try to perform a opration on a variable that is not defined, then it should raise NameError.
x = 5
y = x * z
# NameError: name ‘z’ is not defined

Write a function that will take one parameter. Use try and except. Try to add the given input to a variable.
If the variable exists it should return the sum of two variables, else it should return 'Name Error'

Example: If the parameter is 1, and if it try to add it to a variable z, but z dosn't exist then it should return 'Name Error'.

"""
def NameError(n):
  pass

"""
User will input two parameters(integers).

Concept:  If we try to divide a number by 0, then it should raise ZeroDivisionError.
c = 10/0
# ZeroDivisionError: division by zero

Write a function that will take two parameter. Use try and except. 
If the second parameter is 0, then return 'ZeroDivisionError'
If the second parameter is not 0, return their sum.

Example: If the parameters are 10 and 2, then output should be 5.0.
         If the parameters are 10 and 0, then it should return 'ZeroDivisionError'

"""
def ZeroDivisionError(para1, para2):
  pass

"""
User will input three parameters(integers) - amount, year and rate.

Concept:  If the rate is greater than 100, then it should raise ValueError.

Write a function will throw an exception if interest rate is greater than 100 else return simple interest.

Example: If the parameters are 800, 6, and 8, then output should be 384.0.
         If the parameters are 800, 6, and 800, then it should return 'ValueError'

"""

def simple_interest(amount, year, rate):
  pass

"""
User will input three parameters(integers) - a1, a2, and a3

Make Use of else and finally with try and except.

Concept:  If a3 is 0, then go to finally block and return the multiplication of first two numbers.
          If a3 is not 0, return (a1*a2)/a3 using else block.

Write a function to perform the mentioned.

Example: If the parameters are 5, 4, and 2, then output should be 10.0
         If the parameters are 2, 3 and 0, then output should be 6.

"""

def nums_ops(a1, a2, a3):
  pass

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # TypeError function
        self.assertEqual(TypeError(1, 2), 3, msg="The parameters are 1 and 2. It should returns 3 as the type of both parameters are same.") 
        self.assertEqual(TypeError('ab', 'av'), 'abav', msg="The parameters are 'ab' and 'av'. It should returns 'abav' as the type of both parameters are same.") 
        self.assertEqual(TypeError(1, 'abc'), 'Type Error', msg="The parameters are 1 and 'abc'. It should returns 'Type Error' as the type of both parameters are different.") 

        # NameError function
        self.assertEqual(NameError(1), 'Name Error', msg="The parameter is 1. It should returns 'Name Error' as the function is try to add it to variable z which is undefined.") 

        # ZeroDivisionError function
        self.assertEqual(ZeroDivisionError(10, 2), 5.0, msg="The parameters are 10 and 2. It should returns 5.0 as the second parameter is 2.") 
        self.assertEqual(ZeroDivisionError(10, 0), 'ZeroDivisionError', msg="The parameters are 10 and 0. It should returns 'ZeroDivisionError' as the second parameter is 0.") 

        # simple_interest function
        self.assertEqual(simple_interest(800, 6, 8), 384.0, msg="The parameters are 800, 6, and 8. It should returns 384.0 as the rate is 8 i.e less than 100.") 
        self.assertEqual(simple_interest(800, 6, 800), 'ValueError', msg="The parameters are 800, 6, and 800. It should returns 'ValueError' as the rate is 800 i.e greater than 100.") 

        # nums_ops function
        self.assertEqual(nums_ops(5, 4, 2), 10.0, msg="The parameters are 5, 4, and 2. It should returns 10.0 as if will fall into else block.") 
        self.assertEqual(nums_ops(2, 3, 0), 6, msg="The parameters are 2, 3, and 0. It should returns 6 as the last parameter is 0 and it should fall in finally block.") 


unittest.main()
