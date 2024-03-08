# Scopes and Globals
[home](./readme.md)
* Examples
    * [Accessing outer scope variables in a function](#accessing-outer-scope-variables-in-a-function)
    * [Masking a variable in a function ](#masking-a-variable-in-a-function)
    * [Create and modify a global variable in a function](#create-and-modify-a-global-variable-in-a-function)
    * [Parameters in nested scopes](#parameters-in-nested-scopes)

Scope refers to the visibility and accessibility of variables within a program. Python has four levels of scope:

1. **Global Scope:** Variables declared outside of any function or class have global scope. They can be accessed from anywhere within the module. Parameters always win against globals.
1. **Enclosing (Non-local) Scope:** This scope applies to nested functions. If a variable is not found in the local scope of a function but is present in the enclosing scope (e.g., the scope of the outer function), it can be accessed from within the inner function.
1. **Local Scope:** Variables declared within a function have local scope. They are accessible only within the function where they are defined.
1. **Built-in Scope:** Python provides a set of built-in functions and objects that are always available. These are part of the built-in scope.
## Examples
### Accessing outer scope variables in a function
```python
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
```
### Masking a variable in a function 
```python
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
```
### Create and modify a global variable in a function
```python
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
```
### Parameters in nested scopes
```python
    i = 1
    print(f"the global value of i is: {i}") 
    def function1(i):
        print(f"the parameter value of i is: {i}") 
        x = i   #set x to an i 
        print(f"x initialized to y: {x}")   #it's the parameter i
    function1(5)
```