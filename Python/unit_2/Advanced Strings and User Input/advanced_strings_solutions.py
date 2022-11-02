
"""

You are given a string. Write a function to count the number of characters (character frequency) in a string.
If string is empty, return -1

Example: if string is "hello", then output should be a dict with {'h':1, 'e':1, 'l':2, 'o':1}.

"""
def char_frequency(string):
  
  if len(string) == 0:
    return -1
  

  dict = {}
  for n in string:
    keys = dict.keys()
    if n in keys:
      dict[n] += 1
    else:
      dict[n] = 1

  return dict

"""

You are given a string. Write a function to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return empty string.

If string is empty, return -1

Example: if string is "hello", then output should be a 'helo'

"""
def string_both_ends(string):
  
  if len(string) == 0:
    return -1
  
  if len(string) < 2:
    return ''

  return string[0:2] + string[-2:]

"""
You are given a string. Write a function to call a input method and get the input from the user. If the input is same as the 
input of the function return 'Matched' else return 'Not Matched'.

For Example: If the function input is 'hello' and input from the user is 'hello', then return 'Matched'.

Input string cannot be empty.
"""
def check_input(string):

  input_user = input("Enter the string: ")

  if input_user == string:
    return 'Matched'
  else:
    return 'Not Matched'


"""
You are given two string. Write a function to get a single string from two given 
strings, separated by a space and swap the first two characters of each string.

If any of the strings have length less than 2, then return -1.

Example: if given strings are "abc" and "xyz", then output should be a 'xyc abz'.

"""
def chars_mix_up(string1, string2):
  
  if len(string1) < 2 or len(string2) < 2:
    return -1

  new_a = string2[:2] + string1[2:]
  new_b = string1[:2] + string2[2:]

  return new_a + ' ' + new_b

"""

You are given a string. Write a function to sort a string lexicographically.

If the string is empty, return -1.

Example: if string is 'quickbrown', then output should be a ['b', 'c', 'i', 'k', 'n', 'o', 'q', 'r', 'u', 'w'] 

"""
def lexicographi_sort(string):

  if len(string) == 0:
    return -1

  return sorted(sorted(string), key=str.upper)

"""

You are given a list of words. Write a function to get the unique words in sorted form.

If the list is empty, return -1.

Example: if the inputted list is ['red', 'black', 'pink', 'green', 'pink'], the the output should be ['black', 'green', 'pink', 'red']

"""
def get_unique_words_sorted(list1):

  if len(list1) == 0:
    return -1

  return sorted(list(set(list1)))

"""

You are given a string of words. Write a function to reverse words in a string.

If the list is empty, return -1.

Example: if the string is 'hi i am', the the output should be 'am i hi'

"""
def reverse_string_words(text):

  if len(text) == 0:
    return -1

  for line in text.split('\n'):
    return(' '.join(line.split()[::-1]))


import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # char_frequency function
        self.assertEqual(char_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1}, msg="It should return the character frequency of string 'hello'. Answer should be {'h': 1, 'e': 1, 'l': 2, 'o': 1}") 
        self.assertEqual(char_frequency("google.com"), {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}, msg="It should return the character frequency of string 'google.com'. Answer should be {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}") 
        self.assertEqual(char_frequency(""), -1, msg="It should return -1 as the string is empty") 

        # string_both_ends function
        self.assertEqual(string_both_ends("hello"), 'helo', msg="It should return the concatenation of first 2 and last 2 letters of the string. For string 'hello', answer should be 'helo'.") 
        self.assertEqual(string_both_ends('a'), '', msg="It should return a empty string as the length of given string is less than 2.") 
        self.assertEqual(string_both_ends(""), -1, msg="It should return -1 as the string is empty.") 

        # check_input function
        self.assertEqual(check_input('hello'), 'Matched', msg="It should return 'Matched', assuming user also inputted 'hello'.") 
        self.assertEqual(check_input("okay"), 'Not Matched', msg="It should return 'Not Matched', assuming user did not inputted 'okay'.") 

        # string_both_ends function
        self.assertEqual(chars_mix_up("abc", "xyz"), 'xyc abz', msg="For strings 'abc' and 'xyz', answer should be 'xyc abz'.") 
        self.assertEqual(chars_mix_up('a', 'xyz'), -1, msg="For strings 'a' and 'xyz', it should return -1 as 'a' has length less than 2.") 
        self.assertEqual(chars_mix_up("abc", "x"), -1, msg="For strings 'abc' and 'x', it should return -1 as 'x' has length less than 2.") 
        self.assertEqual(chars_mix_up("a", "x"), -1, msg="For strings 'a' and 'x', it should return -1 as both strings has length less than 2.") 

        # lexicographi_sort function
        self.assertEqual(lexicographi_sort('quickbrown'), ['b', 'c', 'i', 'k', 'n', 'o', 'q', 'r', 'u', 'w'] , msg="It should sort the given string lexicographically. For string 'hello', answer should be ['b', 'c', 'i', 'k', 'n', 'o', 'q', 'r', 'u', 'w'] .") 
        self.assertEqual(lexicographi_sort('hello'), ['e', 'h', 'l', 'l', 'o'], msg="It should sort the given string lexicographically. For string 'hello', answer should be") 
        self.assertEqual(lexicographi_sort(""), -1, msg="It should return -1 as the string is empty.") 

        # get_unique_words_sorted function
        self.assertEqual(get_unique_words_sorted(['red', 'black', 'pink', 'green', 'pink']), ['black', 'green', 'pink', 'red'] , msg="It should get the unique words from the list and sort them. For the given list ['red', 'black', 'pink', 'green', 'pink'], answer should be ['black', 'green', 'pink', 'red'].") 
        self.assertEqual(get_unique_words_sorted(['red', 'black', 'pink', 'green']), ['black', 'green', 'pink', 'red'], msg="It should get the unique words from the list and sort them. For the given list ['red', 'black', 'pink', 'green'], answer should be ['black', 'green', 'pink', 'red'].") 
        self.assertEqual(get_unique_words_sorted([]), -1, msg="It should return -1 as the given list is empty.") 

        # reverse_string_words function
        self.assertEqual(reverse_string_words('hi i am'), 'am i hi' , msg="It should reverse the words in the string. For the string 'hi i am', answer should be 'am i hi'.") 
        self.assertEqual(reverse_string_words(''), -1, msg="It should return -1 as the given string is empty.") 

unittest.main()
