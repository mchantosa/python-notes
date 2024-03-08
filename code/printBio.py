#!/usr/bin/env python

#get user inputs
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))
favorite_color = input("What if your favorite color? ")

#print with end
print("Greetings " + first_name + " " + last_name, end = ", ")# default end = "\n"
print("you are " + str(age) + " years old", end = ", ")# default end = "\n"
print("and your favorite color is " + favorite_color + ".")

#print with sep
print("Greetings " + first_name + " " + last_name, 
      "you are " + str(age) + " years old",  
      "and your favorite color is " + favorite_color + ".", 
      sep = ", ")# default sep = " "