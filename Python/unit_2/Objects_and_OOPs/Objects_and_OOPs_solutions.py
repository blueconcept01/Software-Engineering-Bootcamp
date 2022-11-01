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
1. Create a Vehicle class with max_speed and mileage instance attributes. 
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
Input will be a list.

You will be doing the following -

1. Create class vehicle with the attributes name, mileage and capacity.
2. Create method `fare` in class vehicle that calulates the fare as 'capacity*100'
3. Create object of class Vehicle with the input list.
4. Return the fare for the given capacity.

"""
def get_fare_vehicle(list1: List):    

  # create class
  class Vehicle:
      def __init__(self, name, mileage, capacity):
          self.name = name
          self.mileage = mileage
          self.capacity = capacity

      # create fare method
      def fare(self):
          return self.capacity * 100

  # create object
  vehicle1 = Vehicle(list1[0], list1[1], list1[2])

  # return the fare of the vehicle
  return vehicle1.fare()

"""
This is based on Class Inheritence.

Input will be a list.

You will be doing the following -

1. Create class Vehicle with the attributes name, max_speed and mileage.
2. Create class Bus that will inherit class vehicle.
3. Create object of class Bus with the input list and return the name attribute of the Bus object.

"""
def create_bus_inherit_class(list1: List):    

  # create class vehicle
  class Vehicle:
      def __init__(self, name, max_speed, mileage):
          self.name = name
          self.max_speed = max_speed
          self.mileage = mileage

  # create class Bus that inherit class Vechicle
  class Bus(Vehicle):
      pass

  # create object of class Bus
  School_bus = Bus(list1[0], list1[1], list1[2])

  # return the attribute name
  return School_bus.name

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

  # create class Vehicle
  class Vehicle:
      def __init__(self, name, mileage, capacity):
          self.name = name
          self.mileage = mileage
          self.capacity = capacity

      def fare(self):
          return self.capacity * 100

  # creae class Bus
  class Bus(Vehicle):
      def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

  # crete object of class Bus
  School_bus = Bus(list1[0], list1[1], list1[2])

  # return fare of the object
  return School_bus.fare()

import unittest

class TestDataTypesAndVariables(unittest.TestCase):
    def test_functions(self):

        # create_dog_class function
        self.assertEqual(create_dog_class(["Husky", "Gray", 5, "Fido"]), "Husky", msg="It should return the breed attribute i.e 'Husky' for the given object.") 
        self.assertEqual(create_dog_class(["Labra", "Doodle", 8, "Dong"]), "Labra", msg="It should return the breed attribute i.e 'Labra' for the given object.") 
 
        # create_vehicle_class function
        self.assertEqual(create_vehicle_class([240, 18]), 18, msg="It should return the mileage attribute i.e 18 for the given object.") 
        self.assertEqual(create_vehicle_class([230, 98]), 98, msg="It should return the mileage attribute i.e 98 for the given object.") 

        # get_fare_vehicle function
        self.assertEqual(get_fare_vehicle(["SUV", 12, 6]), 600, msg="It should return the fare of the Vehicle i.e 600 for the given object.") 
        self.assertEqual(get_fare_vehicle(["DOD", 10, 35]), 3500, msg="It should return the fare of the Vehicle i.e 3500 for the given object.") 

        # create_bus_inherit_class function
        self.assertEqual(create_bus_inherit_class(["School Volvo", 180, 12]), "School Volvo", msg="It should return the name attribute i.e 'School Volvo' for the given object.") 
        self.assertEqual(create_bus_inherit_class(["Wagon R", 200, 60]), "Wagon R", msg="It should return the name attribute i.e 'Wagon R' for the given object.") 
 
        # get_bus_fare function
        self.assertEqual(get_bus_fare(["School Volvo", 12, 50]), 5500.0, msg="It should return the fare of the Bus i.e 5500.0 for the given object.") 
        self.assertEqual(get_bus_fare(["Wagon R", 10, 55]), 6050.0, msg="It should return the fare of the Bus i.e 6050.0 for the given object.") 

unittest.main()
