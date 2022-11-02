from typing import List
"""
You are given two parameters:
1st parameters contains a list with student name, and its marks.
2nd parameters contains the updated marks of the student.

Write a class named Student with two attributes student_name, marks. Modify the marks attribute 
of the said object and return modified values of the class object.

You will be doing the following:
1. Create a class `Student` with attributes `student_name` and `marks`.
2. Create a object of class with the parameter1.
3. Update the `marks` of the student object with the parameter2.
4. Return the latest details.

For example: For the input parameters ['ravi', 20] and 95
Create object of student with ['ravi', 20].
Update the marks of the student object using `setattr`

Get the updated details of object using `getattr`.

The output should be ['ravi', 95]
"""
def create_update_class_student(parameter1, parameter2):
  pass

"""
Input will be a list.

You will be doing the following -

1. Create class vehicle with the attributes name, mileage and capacity.
2. Create method `fare` in class vehicle that calulates the fare as 'capacity*100'
3. Create object of class Vehicle with the input list.
4. Return the fare for the given capacity.

"""
def get_fare_vehicle(list1: List):  
  pass

"""
This is based on Class Inheritence.

Input will be a list.

You will be doing the following -

1. Create class Vehicle with the attributes name, max_speed and mileage.
2. Create class Bus that will inherit class vehicle.
3. Create object of class Bus with the input list and return the name attribute of the Bus object.

"""
def create_bus_inherit_class(list1: List):    
  pass

"""
This is based on Class Inheritence.

Input will be a list.

You will be doing the following -

1. Create class Vehicle with the attributes name, mileage and capacity.
2. Create method `fare` in class Vehicle that calulates the fare as 'capacity*100'
3. Create class Bus that will inherit class Vehicle.
4. Create method `fare` in class Vehicle that will inherit the super class method and add the 10% maintainence charges. So total 
fare for bus instance will become the final amount = total fare + 10% of the total fare.
3. Create object of class Bus with the input list.
4. Return the fare for the given capacity.

"""
def get_bus_fare(list1: List):  
  pass

"""
Input will be 2 integers: length and width of rectangle.

You will be doing the following -

1. Create class Rectangle with the attributes length and width.
2. Create method `rectangle_area` in class Rectangle that calulates the area.
3. Create object of class Rectangle with the input.
4. Return the rectangle_area.

For Example: If the input is 12 and 10, then the output should be 120

"""
def get_rectangle_area(length, width):
  pass

"""
Input will be radius of the circle

You will be doing the following -

1. Create class Circle with the attribute radius.
2. Create two method `area` and `perimeter` in class Circle that calulates the area and perimeter of circle.
3. Create object of class Circle with the input.
4. Return the area and perimeter in a list.

If the input radius is less than 1, it returns -1.

For Example: If the input is 8, then the output should be [200.96, 50.24].

"""

def get_area_perimeter_circle(radius):
  pass

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # create_update_class_student function        
        self.assertEqual(create_update_class_student(['ravi', 20], 40), ['ravi', 40], msg="It should return the updated student details. For the given object ['ravi', 20] and updated marks 40, it should return ['ravi', 40]") 
        self.assertEqual(create_update_class_student(['kamal', 90], 30), ['kamal', 30], msg="It should return the updated student details. For the given object ['kamal', 90] and updated marks 30, it should return ['kamal', 30]") 
        self.assertEqual(create_update_class_student(['Rashi', 100], 99), ['Rashi', 99], msg="It should return the updated student details. For the given object ['Rashi', 100] and updated marks 99, it should return ['Rashi', 99]") 

        # get_fare_vehicle function
        self.assertEqual(get_fare_vehicle(["SUV", 12, 6]), 600, msg="It should return the fare of the Vehicle i.e 600 for the given object.") 
        self.assertEqual(get_fare_vehicle(["DOD", 10, 35]), 3500, msg="It should return the fare of the Vehicle i.e 3500 for the given object.") 

        # create_bus_inherit_class function
        self.assertEqual(create_bus_inherit_class(["School Volvo", 180, 12]), "School Volvo", msg="It should return the name attribute i.e 'School Volvo' for the given object.") 
        self.assertEqual(create_bus_inherit_class(["Wagon R", 200, 60]), "Wagon R", msg="It should return the name attribute i.e 'Wagon R' for the given object.") 
 
        # get_bus_fare function
        self.assertEqual(get_bus_fare(["School Volvo", 12, 50]), 5500.0, msg="It should return the fare of the Bus i.e 5500.0 for the given object.") 
        self.assertEqual(get_bus_fare(["Wagon R", 10, 55]), 6050.0, msg="It should return the fare of the Bus i.e 6050.0 for the given object.") 

        # get_rectangle_area function
        self.assertEqual(get_rectangle_area(10, 12), 120, msg="It should return the 120 for the given number 10 and 12.")
        self.assertEqual(get_rectangle_area(4, 7), 28, msg="It should return 28 as the given number 4 and 7.") 
        self.assertEqual(get_rectangle_area(4, 8), 32, msg="It should return 32 as the given number 4 and 8.") 

        # get_rectangle_area function
        self.assertEqual(get_rectangle_area(10, 12), 120, msg="It should return the 120 for the given number 10 and 12.")
        self.assertEqual(get_rectangle_area(4, 7), 28, msg="It should return 28 as the given number 4 and 7.") 
        self.assertEqual(get_rectangle_area(4, 8), 32, msg="It should return 32 as the given number 4 and 8.") 

        # get_area_perimeter_circle function
        self.assertEqual(get_area_perimeter_circle(10), [314.0, 62.800000000000004], msg="It should return the area and perimeter for radius 10 be - [314.0, 62.800000000000004].")
        self.assertEqual(get_area_perimeter_circle(8), [200.96, 50.24], msg="It should return the area and perimeter for radius 8 be [200.96, 50.24].") 
        self.assertEqual(get_area_perimeter_circle(0), -1, msg="It should return -1 as the given number is 0 i.e less than 1.")
        self.assertEqual(get_area_perimeter_circle(-3), -1, msg="It should return -1 as the given number is -3 i.e less than 1.")

unittest.main()
