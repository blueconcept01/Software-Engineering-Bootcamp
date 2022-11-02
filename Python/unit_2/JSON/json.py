import json
"""
User will input json data in string.
Make use of json module

Write a function to convert JSON data to Python object. and return the values.

For example: for the JSON - '{ "Name":"David", "Class":"I", "Age":6 }', it should return ['David', 'I', 6] 
"""
def json_to_object(json_data):
  pass

"""
User will input a dictionary.
Make use of json module

Write a function to convert Python dictionary object (sort by key) to JSON data. 
Return the object with indent level 4.

For example: for the input data - {'4': 5, '6': 7, '1': 3, '2': 4}, the ouput should be -
{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}
"""
def dict_to_json(dictionary):
  pass

"""
User will input json data in string.
Make use of json module

Write a function to check whether following json is valid or invalid.
If valid returns 'Valid', else 'InValid'

For example: for the JSON - '{ "Name":"David", "Class":"I", "Age":6 }', it should return 'Valid'
             for the JSON - '{{}', it should return 'InValid'
"""
def check_json_validity(json_data):
  pass

"""
User will input 2 parameters 1st is json data in string abd 2nd is the key.
Make use of json module

Write a function that parse the following JSON to get all the values of a given key within an array.

For example: for the input json data - [ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]

The  output for the key `name' are - ['name1', 'name2']
"""
def get_all_key_data(jsondata, key):
  pass

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # json_to_object function
        s = '{ "Name":"David", "Class":"I", "Age":6 }'
        self.assertEqual(json_to_object(s), ['David', 'I', 6] , msg=f"For the input json {s}, it should return the values after using the json module i.e ['David', 'I', 6]") 
        s = '{ "Fruit": "Mangoes", "Count": 5 }'
        self.assertEqual(json_to_object(s), ['Mangoes', 5] , msg=f"For the input json {s}, it should return the values after using the json module i.e ['Mangoes', 5]") 

        # dict_to_json function
        s = {'4': 5, '6': 7, '1': 3, '2': 4}
        res = '''{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}'''
        self.assertEqual(dict_to_json(s), res , msg=f"For the input json {s}, it should return the values after using the json module and perform the ident of level 4 i.e {res}") 
        s = { "Fruit": "Mangoes", "Count": 5 }
        res = '''{
    "Count": 5,
    "Fruit": "Mangoes"
}'''
        self.assertEqual(dict_to_json(s), res , msg=f"For the input json {s}, it should return the values after using the json module and perform the ident of level 4 i.e {res}") 

        # check_json_validity function
        s = '{ "Name":"David", "Class":"I", "Age":6 }'
        self.assertEqual(check_json_validity(s), 'Valid' , msg=f"For the input json {s}, it should return 'Valid' as the given json is Valid") 

        s = '{{}'
        self.assertEqual(check_json_validity(s), 'InValid' , msg=f"For the input json {s}, it should return 'InValid' as the given json is invalid")

        # get_all_key_data function
        jsondata = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""
        res = ['name1', 'name2']
        self.assertEqual(get_all_key_data(jsondata, 'name'), res , msg=f"For the input json {jsondata}, it should return the values for key name i.e {res}") 

        res = [1, 2]
        self.assertEqual(get_all_key_data(jsondata, 'id'), res , msg=f"For the input json {jsondata}, it should return the values for key id i.e {res}") 

        res = [['red', 'green'], ['pink', 'yellow']]
        self.assertEqual(get_all_key_data(jsondata, 'color'), res , msg=f"For the input json {jsondata}, it should return the values for key color i.e {res}") 


unittest.main()
