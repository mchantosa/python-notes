#!/usr/bin/env python

fahrenheit = float(input("What temperature in fahrenheit would you like converted to celsius?"))
celsius = (fahrenheit -32)*5/9
print(fahrenheit,"F is", round(celsius, 2), "C")