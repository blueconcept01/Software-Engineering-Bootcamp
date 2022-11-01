from typing import Dict, List, Tuple

"""
n is an int
check if n is negative, return -1
Else, Return the numbers from 0 till n(including n)
"""
def list_numbers(n: int) -> List[int]:    
    if n < 0:
        return -1

    res = []
    i = 0

    # loop till i is less or equal to n
    while i <= n :
      res.append(i)
      i = i+1

    return res

"""
n is a positive integer
Return a list of integers from 1 to n(including n) that are even.
"""
def even_numbers(n: int) -> List[int]:
    res = []
    i = 1

    # loop till i is less or equal to n
    while i <= n:
      if i%2 == 0:
        res.append(i)
      i = i+1

    return res

"""
n is a positive integer
Return a list of integers from 1 to n(including n) that are odd.
"""
def odd_numbers(n: int) -> List[int]:
    res = []
    i = 1

    # loop till i is less or equal to n
    while i <= n:
      if i%2 != 0:
        res.append(i)
      i = i+1

    return res

"""
Implement a function that will take a string and return the list with its individual characters. If the string is empty, then return -1
For example: if string is "hello", then answer should be ['h', 'e', 'l', 'l', 'o']
"""
def individual_characters(string: str) -> Tuple[int, List[str]]:
    if string == '':
        return -1

    res = []
    
    # loop till length of string
    i = 0
    while i < len(string):
      res.append(string[i])
      i = i+1
    
    return res

"""
Implement a function that will take a string and return the list with its unique characters. If the string is empty, then return -1.
For example: if string is "hello", then answer should be ['h', 'e', 'l', 'o']
Make use of continue statement.
"""
def individual_unique_characters(string: str) -> Tuple[int, List[str]]:
    if string == '':
        return -1

    res = []

    # loop till length of string
    i = 0
    while i < len(string):
      if string[i] in res:
        i = i+1
        continue
      res.append(string[i])
      i = i+1
    
    return res    

"""
Implement a function that will take a list of numbers(integers) and return the sum of numbers. If the list is empty, then return -1.
"""
def sum_list(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    sum_list = 0

    # loop till the length of list
    i = 0
    while i < len(num_list):
        sum_list += num_list[i]
        i = i+1
    
    return sum_list 

"""
Implement a function that will take a list of numbers(integers) and return the maximum number from the list of numbers. 
If the list is empty, then return -1.
"""
def max_list(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    max_list = -1
    # loop till the length of list
    i = 0
    while i < len(num_list):
        if num_list[i] > max_list:
          max_list = num_list[i]
        i = i+1
    
    return max_list 

"""
Implement a function that will take a list of numbers(integers) and return the minimum number from the list of numbers. 
If the list is empty, then return -1.
"""
def min_list(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    min_list = 10**9
    # loop till the length of list
    i = 0
    while i < len(num_list):
        if num_list[i] < min_list:
          min_list = num_list[i]
        i = i+1
    
    return min_list     

"""
Implement a function that will take a list of numbers(integers) and number num and check whether the number exists in the list.
If number exists return "Found", else return "Not Found"
If the list is empty, then return -1.
Make use of break statement
"""
def find_num_in_list(num_list: List[int], num: int) -> Tuple[str, int]:
    if len(num_list) == 0:
        return -1

    found = False

    # loop till the length of list
    i = 0
    while i < len(num_list):
        if num_list[i] == num:
            found = True
            break
        i = i+1
    
    if found:
        return "Found"
    else:
        return "Not Found"

"""
Implement a function that will take a list of numbers(integers) and return the list of positive numbers from the list of numbers. 
If the list is empty, then return -1.
If there are no positive numbers in the list, return -1
Make use of continue statement.
"""
def get_positives(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    pos_list = []
    # loop till the length of list
    i = 0
    while i < len(num_list):
        if num_list[i] > 0:
            pos_list.append(num_list[i])
        i = i+1
    
    if len(pos_list) == 0:
        return -1

    return pos_list  

"""
Implement a function that will take a list of numbers(integers) and return the list of negative numbers from the list of numbers. 
If the list is empty, then return -1.
If there are no negative numbers in the list, return -1
Make use of continue statement.
"""
def get_negative(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    neg_list = []
    # loop till the length of list
    i = 0
    while i < len(num_list):
        if num_list[i] < 0:
            neg_list.append(num_list[i])
        i = i+1
    
    if len(neg_list) == 0:
        return -1

    return neg_list  

"""
Implement a function that will take a list of numbers(integers) and return the average of numbers. 
If the list is empty, then return -1.
"""
def get_average(num_list: List[int]) -> int:
    if len(num_list) == 0:
        return -1

    average_list = 0

    # loop till the length of list
    i = 0
    while i < len(num_list):
        average_list += num_list[i]
        i = i+1
    
    # get the average
    average = average_list/len(num_list)

    return average 

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # list_numbers function
        self.assertEqual(list_numbers(5), [0, 1, 2, 3, 4, 5], msg="It should return the list i.e [0, 1, 2, 3, 4, 5] for the given number 5.") 
        self.assertEqual(list_numbers(-2), -1, msg="It should return -1 as the given number -2 is negative") 
        
        # even_numbers function
        self.assertEqual(even_numbers(5), [2, 4], msg="It should return list of even numbers from 1 till the given number i.e for number 5 it should return [2, 4]")
        self.assertEqual(even_numbers(12), [2, 4, 6, 8, 10, 12], msg="It should return list of even numbers from 1 till the given number i.e for number 12 it should return [2, 4, 6, 8, 10, 12]")
        self.assertEqual(even_numbers(1), [], msg="It should return empty list as the given list is empty []")

        # odd_numbers function
        self.assertEqual(odd_numbers(5), [1, 3, 5], msg="It should return list of odd numbers from 1 till the given number i.e for number 5 it should return [1, 3, 5]")
        self.assertEqual(odd_numbers(12), [1, 3, 5, 7, 9, 11], msg="It should return list of odd numbers from 1 till the given number i.e for number 12 it should return [1, 3, 5, 7, 9, 11]")
        self.assertEqual(odd_numbers(0), [], msg="It should return empty list as the given list is empty []")       

        # individual_characters function
        self.assertEqual(individual_characters("hello"), ['h', 'e', 'l', 'l', 'o'], msg="It should return list of characters in the string i.e for string 'hello' it should return ['h', 'e', 'l', 'l', 'o']")
        self.assertEqual(individual_characters("okay"), ['o', 'k', 'a', 'y'], msg="It should return list of characters in the string i.e for string 'okay' it should return ['o', 'k', 'a', 'y']")
        self.assertEqual(individual_characters(""), -1, msg="It should return -1 as given string is empty")    

        # individual_unique_characters function
        self.assertEqual(individual_unique_characters("hello"), ['h', 'e', 'l', 'o'], msg="It should return list of unique characters in the string i.e for string 'hello' it should return ['h', 'e', 'l', 'o']")
        self.assertEqual(individual_unique_characters("okay"), ['o', 'k', 'a', 'y'], msg="It should return list of unique characters in the string i.e for string 'okay' it should return ['o', 'k', 'a', 'y']")
        self.assertEqual(individual_characters(""), -1, msg="It should return -1 as given string is empty")               

        # sum_list function
        self.assertEqual(sum_list([1, 2, 3, 4]),10, msg="It should return the sum of all the numbers in the list i.e for list [1, 2, 3, 4] it should return 1+2+3+4=10")
        self.assertEqual(sum_list([2, 2, 2]),6, msg="It should return the sum of all the numbers in the list i.e for list [2, 2, 2] it should return 2+2+2=6")
        self.assertEqual(sum_list([]), -1, msg="It should return -1 as given list is empty") 

        # max_list function
        self.assertEqual(max_list([1, 2, 3, 4]),4, msg="It should return the maximum of all the numbers in the list i.e for list [1, 2, 3, 4] it should return 4")
        self.assertEqual(max_list([2, 2, 2]),2, msg="It should return the maximum of all the numbers in the list i.e for list [2, 2, 2] it should return 2")
        self.assertEqual(max_list([]), -1, msg="It should return -1 as given list is empty")

        # min_list function
        self.assertEqual(min_list([1, 2, 3, 4]),1, msg="It should return the minimum of all the numbers in the list i.e for list [1, 2, 3, 4] it should return 1")
        self.assertEqual(min_list([2, 2, 2]),2, msg="It should return the minimum of all the numbers in the list i.e for list [2, 2, 2] it should return 2")
        self.assertEqual(min_list([]), -1, msg="It should return -1 as given list is empty")        

        # find_num_in_list function
        self.assertEqual(find_num_in_list([1, 2, 3, 4], 4),"Found", msg="It should return Found as number exists in the list i.e for list [1, 2, 3, 4] and number 4 it should return 'Found' as 4 is present in the list")
        self.assertEqual(find_num_in_list([2, 2, 2], 3),"Not Found", msg="It should return Not Found as the number not found i.e for list [2, 2, 2] and number 3 it should return 'Not Found' as 3 is not present")
        self.assertEqual(find_num_in_list([], 5), -1, msg="It should return -1 as given list is empty")

        # get_positives function
        self.assertEqual(get_positives([1, -2, 3, -1, -8, 0]),[1, 3], msg="It should return the list of positive numbers that exists in the list i.e for list [1, -2, 3, -1, -8, 0] it should return [1, 3]")
        self.assertEqual(get_positives([-1, -2, -3]),-1, msg="It should return -1 as there are no positive numbers in the list i.e for list [-1, -2, -3] it should return -1 as there are no positive integer.")
        self.assertEqual(get_positives([]), -1, msg="It should return -1 as given list is empty")     

        # get_negative function
        self.assertEqual(get_negative([1, -2, 3, -1, -8, 0]),[-2, -1, -8], msg="It should return the list of negative numbers that exists in the list i.e for list [1, -2, 3, -1, -8, 0] it should return [-2, -1, -8]")
        self.assertEqual(get_negative([1, 2, 3]),-1, msg="It should return -1 as there are no negative numbers in the list i.e for list [1, 2, 3] it should return -1 as there are no negative integer.")
        self.assertEqual(get_negative([]), -1, msg="It should return -1 as given list is empty")    

        # get_average function
        self.assertEqual(get_average([1, 2, 3, 4]),2.5, msg="It should return the average of all the numbers in the list i.e for list [1, 2, 3, 4] it should return 1+2+3+4=10/4=2.5")
        self.assertEqual(get_average([2, 2, 2]),2.0, msg="It should return the average of all the numbers in the list i.e for list [2, 2, 2] it should return 2+2+2=6/3=2.0")
        self.assertEqual(get_average([]), -1, msg="It should return -1 as given list is empty") 

unittest.main()
