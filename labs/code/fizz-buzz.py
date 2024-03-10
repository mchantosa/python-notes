#!/usr/bin/env python
value = int(input("How many values should we process?: "))

for val in range(1, value + 1):
    if val%3 == 0 and val%5 == 0:
            print("FizzBuzz")
    elif val%3 == 0:
        print("Fizz")
    elif val%5 == 0:
        print("Buzz")
    else:
        print(val)