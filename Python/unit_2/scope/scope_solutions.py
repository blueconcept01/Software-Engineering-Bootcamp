"""
User will input 2 integers; p1 and p2.

Concept: Variable Scope. If there are two variable with same name, then its scope is defined by the block. 
If its inside a function, then its scope is within the function. 

You will perform the following:
1. Define a variable a with value p1.
2. Create a function name `check` and inside the function define a varibale a with value p2. 
And add a return statement to return the variable a.
3. print the varibale a, and then call the function check.

You will notice that function check will return the value of a as p2, not as p1.
"""
def variable_scope(p1, p2):
  a = p1
  def check():
    a = p2
    return a
  return a, check()


import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # variable_scope function        
        self.assertEqual(variable_scope(2, 3), (2, 3) , msg=f"For the input values 2 and 3, the output should be (2, 3). The first item i.e 2 is the value of outer variable a, and second item i.e 3 is the value of function check()") 
        self.assertEqual(variable_scope(4, 1), (4, 1) , msg=f"For the input values 4 and 1, the output should be (4, 1). The first item i.e 4 is the value of outer variable a, and second item i.e 1 is the value of function check()") 
        self.assertEqual(variable_scope(8, 7), (8, 7) , msg=f"For the input values 8 and 7, the output should be (8, 7). The first item i.e 8 is the value of outer variable a, and second item i.e 7 is the value of function check()") 


unittest.main()
