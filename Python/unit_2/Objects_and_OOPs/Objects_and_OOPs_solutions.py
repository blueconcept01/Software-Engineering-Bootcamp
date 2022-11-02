from typing import List

"""
Input is a list of values.

You will be doing the following -
1. Create a class `Dog` with the attributes breed, color, age, and name. 
2. Create the object of the `Dog` class with the input 
3. Return the attribute breed of the object.

Example: if the input is - [“Husky”, "Gray", 5, "Fido"], then output should be "Husky".

"""
def create_dog_class(list1: List):    

  # create class
  class Dog:
      def __init__(self, breed, color, age, name):
          self.breed = breed
          self.color = color
          self.age = age
          self.name = name

  # create object
  dog1 = Dog(list1[0], list1[1], list1[2], list1[3])

  # return the breed attribute
  return dog1.breed 

"""
Input is a list of values.

You will be doing the following -
1. Create a `Vehicle` class with max_speed and mileage instance attributes. 
2. Create the object of the `Vehicle` class with the input 
3. Return the attribute mileage of the object.

Example: if the input is - [240, 18], then output should be 18.
"""
def create_vehicle_class(list1: List):    
  # create class
  class Vehicle:
      def __init__(self, max_speed, mileage):
          self.max_speed = max_speed
          self.mileage = mileage

  # create object
  Vehicle1 = Vehicle(list1[0], list1[1])

  # return the mileage attribute
  return Vehicle1.mileage

"""
Input is a string.

You will be doing the following -
1. Create a `Word` class with attribute word. 
2. Create a method `reverse_words` inside the class that will return the reversed word.
3. Create the object of the `Word` class with the input string.
4. Call the function `reverse_words` on the object.
5. return the reversed string

If the given string is empty, return -1.

Example: if the input is - 'hello', then output should be 'olleh'.
"""
def create_class_word(string):   

    if len(string) == 0:
        return -1

    class Word:
        def __init__(self, word):
            self.word = word
            
        def reverse_words(self):
            s = self.word
            return s[::-1]

    # create object of the class
    word = Word(string)

    # call function
    reversed_word = word.reverse_words()

    return reversed_word

"""
Input is a number.

You will be doing the following -
1. Create a `IntToRoman` class with attribute num. 
2. Create a method `int_to_Roman` inside the class that will return the roman form of the num.
3. Create the object of the `IntToRoman` class with the input.
4. Call the function `int_to_Roman` on the object.
5. return the roman string

If the given number is less than 1, return -1.

Example: if the input is - 'hello', then output should be 'olleh'.
"""
def intToRoman(n):

    if n < 1:
        return -1

    class IntToRoman:
        
        def __init__(self, num):
            self.num = num
            
        def int_to_Roman(self):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
            roman_num = ''
            i = 0
            n = self.num
            while  n > 0:
                for _ in range(n // val[i]):
                    roman_num += syb[i]
                    n -= val[i]
                i += 1
            return roman_num

    # create object of class
    obj1 = IntToRoman(n)
    return obj1.int_to_Roman()

"""
Input is a string.

You will be doing the following -
1. Create a `Paranthesis` class with attribute str1. 
2. Create a method `is_valid_parenthese` inside the class that will the validity. If its valid, returns 'Valid' else returns 'Invalid'.
3. Create the object of the `Paranthesis` class with the input string.
4. Call the function `is_valid_parenthese` on the object.
5. return the output of the function

If the given string is empty, return -1.

Example: if the input is - '(){}[]', then output should be 'Valid'.
"""
def check_paranthesis_validity(string):

    if len(string) == 0:
        return -1

    class Paranthesis:
        def __init__(self, str1):
            self.str1 = string
            
        def is_valid_parenthese(self):
                stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
                for parenthese in self.str1:
                    if parenthese in pchar:
                        stack.append(parenthese)
                    elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                        return 'Invalid'
                if len(stack) == 0:
                    return 'Valid'

    # create object
    obj1 = Paranthesis(string)
    return obj1.is_valid_parenthese()

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # create_dog_class function
        self.assertEqual(create_dog_class(["Husky", "Gray", 5, "Fido"]), "Husky", msg="It should return the breed attribute i.e 'Husky' for the given object.") 
        self.assertEqual(create_dog_class(["Labra", "Doodle", 8, "Dong"]), "Labra", msg="It should return the breed attribute i.e 'Labra' for the given object.") 
 
        # create_vehicle_class function
        self.assertEqual(create_vehicle_class([240, 18]), 18, msg="It should return the mileage attribute i.e 18 for the given object.") 
        self.assertEqual(create_vehicle_class([230, 98]), 98, msg="It should return the mileage attribute i.e 98 for the given object.") 

        # create_class_word function
        self.assertEqual(create_class_word("hello"), 'olleh', msg="It should return the 'olleh' for the given string 'hello'.") 
        self.assertEqual(create_class_word("okay"), 'yako', msg="It should return the 'yako' for the given string 'okay'.")
        self.assertEqual(create_class_word(""), -1, msg="It should return -1 as the given string is empty.")

        # intToRoman function
        self.assertEqual(intToRoman(1), 'I', msg="It should return the 'I' for the given number 1.") 
        self.assertEqual(intToRoman(4087), 'MMMMLXXXVII', msg="It should return the 'MMMMLXXXVII' for the given number 4087.")
        self.assertEqual(intToRoman(0), -1, msg="It should return -1 as the given number is 0 i.e less than 1.") 
        self.assertEqual(intToRoman(-3), -1, msg="It should return -1 as the given number is -3 i.e less than 1.") 

        # check_paranthesis_validity function
        self.assertEqual(check_paranthesis_validity("(){}[]"), 'Valid', msg="It should return the 'Valid' for the given paranthesis string '(){}[]'.")
        self.assertEqual(check_paranthesis_validity("()[{)}"), 'Invalid', msg="It should return the 'Invalid' for the given paranthesis string '()[{)}'.") 
        self.assertEqual(check_paranthesis_validity("()"), 'Valid', msg="It should return the 'Valid' for the given paranthesis string '()'.")
        self.assertEqual(check_paranthesis_validity(""), -1, msg="It should return -1 as the given paranthesis string is empty.")


unittest.main()
