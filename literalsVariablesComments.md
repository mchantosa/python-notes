# Literals, Variables, and Comments
[home](./readme.md)

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

## Types
### Strings
Strings can be enclosed in single or double quotes. 
```python
    #single and double quotes
    str = 'this is a string'
    print(str)    # this is a string

    str = "this is also a string"
    print(str)    # this is also a string

    #multiline strings
    str = '''
    this is a 
    multiline string
    '''
    print(str)    #/nthis is a /n multiline string/n

    str = """
    this is also a 
    multiline string
    """
    print(str)    #/nthis is also a/nmultiline string/n
```
### Booleans
### Numbers