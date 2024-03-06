#!/usr/bin/env python

name = input("What is your name? ")
print("Hi " + name + "!", end = " ")

if name[0] in "aeiou":
    print("Your name begins with a vowel, interesting...", end = " ")
else:
    pass    #do nothing

if len(name) < 5:
    print("Your name is too short")
elif len(name) > 10:
    print("Your name is too long")
else:
    print("Your name is a reasonable length")