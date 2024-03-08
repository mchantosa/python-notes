# Using Python Conditionals
[home](../readme.md)

[fizz-buzz-item.py](./code/fizz-buzz-item.py)
## Learning Objectives
* Create the `fizz-buzz-item.py` Script, Make It Executable with python3.7, and Accept User Input
* Print "FizzBuzz" if the Value Is a Multiple of Three and Five
* Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five

### Objective: 
Create an executable file `fizz-buzz-item.py` that prompts the user for a value and prints "FizzBuzz" if the value is a multiple of 3 and 5, "Fizz" if the value is a multiple of three, and "Buzz" if it's a multiple of five

## Steps

1. Create an executable file
    ```shell
        touch fizz-buzz-item.py
        chmod u+x ./fizz-buzz-item.py
    ```
    Remember, this class uses python 3.7, use python locally.
    ```python
        #!/usr/bin/env python3.7
    ```
1. Prompt and Store message from User
    ```python
        #...
        value = int(input("Enter an integer value: "))
    ```
1. Print "FizzBuzz" if value is a multiple of 3 and 5
    ```python
        #...
        if value%3 == 0 and value%5 ==0:
            print("FizzBuzz")
    ```
1. Otherwise print "Fizz" if value is a multiple of 3
    ```python
        #...
        elif value%3 == 0:
            print("Fizz")
    ```
1. Otherwise print "Buzz" if value is a multiple of 5
    ```python
        #...
        elif value%5 == 0:
            print("Buzz")
    ```
1. Otherwise print the value itself
    ```python
        #...
        else:
            print(value)
    ```
1. End Product
   ```python
        #!/usr/bin/env python

        value = int(input("Enter an integer value: "))

        if value%3 == 0 and value%5 == 0:
            print("FizzBuzz")
        elif value%3 == 0:
            print("Fizz")
        elif value%5 == 0:
            print("Buzz")
        else:
            print(value)
    ```
1. Execute test cases.
    ```shell
        #test case 1
        ./fizz-buzz-item.py
        15
        #Output: FizzBuzz

        #test case 2
        ./fizz-buzz-item.py
        6
        #Output: Fizz

        #test case 3
        ./fizz-buzz-item.py
        10
        #Output: Buzz

        #test case 4
        ./fizz-buzz-item.py
        2
        #Output: 2

        #test case 5
        ./fizz-buzz-item.py
        0
        #Output: FizzBuzz
    ```
