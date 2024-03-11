# Literals, Variables, and Comments
[home](../readme.md)

## Comments
Comments in Python are done with a `#`. 
```python
    #!/usr/bin/env python

    #This is a full line comment
    print("Hello World") #This is a trailing comment

    """
    This is not a block comment.
    This is a multiline string.
    The file will still run, HelloWorld will still print,
    but the compiler will not ignore this,
    it will instantiate it and it will take space in memory.
    Comments are free, they are disregarded by the interpreter and
    have no impact on the execution of your code. 
    Python has no block comments.
    """
```
## Literals
Python has three types of literals
* [strings](./strings.md)
* [booleans](./bools.md)
* [numbers](./numbers.md), numbers com in the flavors
    * Integers
    * Floats
    * Complex

## Variables
Variables are containers for storing data values. Unlike other programming languages, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type and can even change type after they have been set.
```python
    #assigning a string to a variable
    myStr = "Yo, sup!"  
    print(myStr)    # Yo, sup!

    #reassigning the variable
    myStr = "Yo, sup again!"    
    print(myStr)    # Yo, sup again!

    #augmented assignment 
    myStr += " Boom!"   #a += b is the same as a = a + b
    print(myStr)    # Yo, sup again! Boom!

    #assigning a number to a variable
    myNum = 5
    print(myNum)    # 5
```