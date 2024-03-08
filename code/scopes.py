#!/usr/bin/env python

# Accessing outer scope variables in a function
print("\nEXAMPLE 1: Accessing global variables in a function")
a = "global"
def function1():
    b = "local to function1"
    def function2():
        print("a in function2 is: ", a) #access global a
        print("b in function2 is: ", b) #access outer b, make global to edit
    function2()
    print("a in function1 is: ", a) #access global a
    print("b in function1 is: ", b) #access local b
function1()
print("a in outer scope is: ", a) #access global a
 

# Masking a variable in a function 
print("\nEXAMPLE 2: Masking variables in a function")
x = 1
def function1():
    x = 2   #create a local variable, will not affect x in outer scope
    def function2():
        x = 3   #create a local variable, will not affect x in outer scope
        print("local variable x in function2 is: ", x)
    function2()
    print("local variable x in function1 is: ", x)
function1()
print("global variable x is: ", x)


# Create and modify a global variable in a function
print("\nEXAMPLE 3: Creating and modifying global variables in a function")
def function1():
    def function2():
        global y    #create a global variable
        y = 0
        print("global y in function2 is initialized to: ", y)
    function2()
    global y    #modify a global variable
    y = 1
    print("global y in function1 is modified to: ", y)
function1()
print("global y in outer scope is accessed: ", y) 


# Parameters in nested scopes
print("\nEXAMPLE 4: Parameters in nested scopes")
i = 1
print(f"the global value of i is: {i}") 
def function1(i):
    print(f"the parameter value of i is: {i}") 
    x = i   #set x to an i
    print(f"x initialized to y: {x}")   #it's the parameter i
function1(5)