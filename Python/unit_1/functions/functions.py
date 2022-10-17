"""
n is an int

Return True if n is odd
False if n is even
"""
def is_odd(n):
    pass

"""
n is an int
Return True if n is positive
False if its negative
"""
def is_positive(n):
    pass

"""
n is an int/float

return the 3 times the value of n
"""
def triple(n):
    pass

"""
Implement a function that adds a copy of the first item in the list to end of the list 
"""
def add_first_item(lst):
    pass

"""

Return the final price for a customer given their total_price and if they have a coupon or not

If the total price is $100 or more they get a discount of $20.
If they have a coupon they also get a discount of $10.

Return the final price given the discount if any.

"""
def get_discounted_price(total_price, has_coupon):
    pass

"""
Implement a function called add_to_list that takes in 2 parameters
1 parameter is a list of int/floats
the next parameter is a int/float that will be added to every element in the list
"""
add_to_list = None

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):
        self.assertTrue(is_odd(1), msg="is_odd is not returning true when given a positive number")
        self.assertFalse(is_odd(2), msg="is_odd is not returning false when given a positive number")
        
        self.assertTrue(is_positive(2), msg="is_positive i not returning true when given a positive number")
        self.assertFalse(is_positive(-2), msg="is_positive is not returning false when given a negative number")

        self.assertEqual(triple(3), msg="your triple function is not returning 3 times the input value for n")

        lst = [1,2,3]
        add_first_item(lst)
        self.assertEqual(lst, [1,2,3,1], msg="Your add_first_item function is not adding the first element of the list into the last")

        self.assertEqual(get_discounted_price(100, True), 70, msg="Your get_discount_price is not discounting with both more then 100 and the coupon")
        self.assertEqual(get_discounted_price(80, True), 70, msg="Your get_discount_price function is not discounting the coupon for $10 right")
        self.assertEqual(get_discounted_price(120, False), 100, msg="Your get_discount_price function is not discounting the $100 or more sale discount right")
        
        self.assertNotEqual(add_to_list, None, msg="add_to_list is not implemented right now")
        self.assertEqual(add_to_list([1,2,3], 2), [3,4,5])

unittest.main()