# Operators and Bindings (order of precedence)
[home](../readme.md)

*   **type():** returns the exact type of an object.
*   **isinstance():** checks if an object is an instance of a specified class or any of its subclasses.

```python
    #ints
    my_num = int(1.6)
    print(my_num) # Output: 1
    print(type(my_num)) # Output: int class
    print(isinstance(my_num, int))    # Output: True
    print(isinstance(my_num, float))    # Output: False
    #this will error
    #   my_num = int("1.6")

    #floats
    my_num = float(1)
    print(my_num)   # Output: 1.0
    print(type(my_num)) # Output: float class
    print(isinstance(my_num, float))    # Output: True
    my_num = float("1.6")

    #strings
    my_str1 = str(1.0)
    my_str2 = str(True)
    print(isinstance(my_str1, str), isinstance(my_str2, str))    # Output: True True

    #bools
    #   everything in python can be turned into a bool
    print(bool(1))  # Output: True
    print(bool('boom')) # Output: True
    print(bool([0]))    # Output: True
    #   0s, None, and iterables of length 0
    print(bool(0))  # Output: False
    print(bool(0.0))    # Output: False
    print(None)    # Output: False
    print(bool('')) # Output: False
    print(bool([])) # Output: False
```