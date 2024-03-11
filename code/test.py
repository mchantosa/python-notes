#!/usr/bin/env python
def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
      return print('FizzBuzz')
    elif num % 3 == 0:
      return 'Fizz'
    elif num % 5 == 0:
      return 'Buzz'
    else:
      return num

fizz(15)