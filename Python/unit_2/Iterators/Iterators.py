"""
You are given a string.

Write a function to create a iterater to iterate through the string. And the return the characters in a list.
Make use of iterator methods __next__ and __iter__.

You will be doing the following:
1. Create Iterator class, and define the respective methods __init__, __iter__ and __next__.
2. Create object of Iterator class with the input string.
3. Return the characters in a list.

If the given string is empty, return -1.

For example: For string "abc", the output should be ['a', 'b', 'c']
"""
def string_iterator(string):
  pass

"""
You are given a number `n`.

Write a function to create an iterator that returns numbers in a list, starting with 1 to the given number n.
Make use of iterator methods __next__ and __iter__.

You will be doing the following:
1. Create MyNumbers class, and define the respective methods __init__, __iter__ and __next__.
2. Create object of MyNumbers class with the input number n.
3. Return the numbers in a list, starting with 1 to the given number n.

If the given number is less than 1, return -1.

For example: For number 4, the output should be [1, 2, 3, 4]
"""
def number_iterator(n):
  pass

"""
You are given a number `n`.

Write a function to create an iterator that returns the odd numbers in a list, starting with 1 to the given number n.
Make use of iterator methods __next__ and __iter__.

You will be doing the following:
1. Create OddNumbers class, and define the respective methods __init__, __iter__ and __next__.
2. Create object of OddNumbers class with the input number n.
3. Return the odd numbers in a list, starting with 1 to the given number n.

If the given number is less than 1, return -1.

For example: For number 4, the output should be [1, 3]
"""
def odd_number_iterator(n):
  pass

"""
You are given a number `n`.

Write a function to create an iterator that returns the even numbers in a list, starting with 1 to the given number n.
Make use of iterator methods __next__ and __iter__.

You will be doing the following:
1. Create EvenNumbers class, and define the respective methods __init__, __iter__ and __next__.
2. Create object of EvenNumbers class with the input number n.
3. Return the even numbers in a list, starting with 1 to the given number n.

If the given number is less than 1, return -1.

For example: For number 4, the output should be [2, 4]
"""
def even_number_iterator(n):
  pass

"""
You are given a string.

Write a function to create a generator to reverse a string.
Make use of generator yield.

You will be doing the following:
1. Create a function rev_str, and generate the reversed string using yield and for loop.
2. Call the function rev_str and return teh reversed string.

If the given string is empty, return -1.

For example: For string "abc", the output should be "cba".
"""
def reverse_string_generator(string):
  pass
    

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # string_iterator function        
        self.assertEqual(string_iterator('abc'), ['a', 'b', 'c'], msg="For the input string 'abc', it should return ['a', 'b', 'c'] i.e characters of the string in a list.") 
        self.assertEqual(string_iterator('Demonstration'), ['D', 'e', 'm', 'o', 'n', 's', 't', 'r', 'a', 't', 'i', 'o', 'n'] , msg="For the input string 'Demonstration', it should return ['D', 'e', 'm', 'o', 'n', 's', 't', 'r', 'a', 't', 'i', 'o', 'n'] i.e characters of the string in a list.") 
        self.assertEqual(string_iterator(''), -1 , msg="This should return -1 as the input string is empty.")

        # number_iterator function        
        self.assertEqual(number_iterator(4), [1, 2, 3, 4], msg="For the input number 4, it should return [1, 2, 3, 4] i.e sequence of number from 1 to 4.") 
        self.assertEqual(number_iterator(6), [1, 2, 3, 4, 5, 6] , msg="For the input number 6, it should return [1, 2, 3, 4, 5, 6] i.e sequence of number from 1 to 6.") 
        self.assertEqual(number_iterator(0), -1 , msg="This should return -1 as the input number is 0 i.e less than 1.") 
        self.assertEqual(number_iterator(-2), -1 , msg="This should return -1 as the input number is -2 i.e less than 1.") 

        # odd_number_iterator function
        self.assertEqual(odd_number_iterator(4), [1, 3], msg="For the input number 4, it should return [1, 3] i.e sequence of odd numbers from 1 to 4.") 
        self.assertEqual(odd_number_iterator(6), [1, 3, 5] , msg="For the input number 6, it should return [1, 3, 5] i.e sequence of odd numbers from 1 to 6.") 
        self.assertEqual(odd_number_iterator(0), -1 , msg="This should return -1 as the input number is 0 i.e less than 1.") 
        self.assertEqual(odd_number_iterator(-2), -1 , msg="This should return -1 as the input number is -2 i.e less than 1.") 

        # even_number_iterator function
        self.assertEqual(even_number_iterator(4), [2, 4], msg="For the input number 4, it should return [2, 4] i.e sequence of even numbers from 1 to 4.") 
        self.assertEqual(even_number_iterator(6), [2, 4, 6] , msg="For the input number 6, it should return [2, 4, 6] i.e sequence of even numbers from 1 to 6.") 
        self.assertEqual(even_number_iterator(0), -1 , msg="This should return -1 as the input number is 0 i.e less than 1.") 
        self.assertEqual(even_number_iterator(-2), -1 , msg="This should return -1 as the input number is -2 i.e less than 1.") 

        # reverse_string_generator function        
        self.assertEqual(reverse_string_generator('abc'), 'cba', msg="For the input string 'abc', it should return 'cba' i.e reversed string.") 
        self.assertEqual(reverse_string_generator('Demonstration'), 'noitartsnomeD' , msg="For the input string 'Demonstration', it should return 'noitartsnomeD' i.e reversed string.") 
        self.assertEqual(reverse_string_generator(''), -1 , msg="This should return -1 as the input string is empty.")

unittest.main()
