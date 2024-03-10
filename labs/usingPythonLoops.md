# Utilizing Python Loops
[home](../readme.md)

[fizz-buzz.py](./code/fizz-buzz.py)
## Learning Objectives
* Create the `fizz-buzz.py` Script, Make It Executable with python3.7, and Accept User Input
* Create a Range from 1 to the User's Provided Number and Loop Through It
* Print "FizzBuzz" if the Value Is a Multiple of Three and Five
* Print "Fizz" if the Value Is a Multiple of Three and "Buzz" if It's a Multiple of Five

### Objective: 
Create an executable file `fizz-buzz.py` that prompts the user for a value and iterates from 1 to that value printing "FizzBuzz" if the value is a multiple of 3 and 5, "Fizz" if the value is a multiple of three, and "Buzz" if it's a multiple of five, or the value if it is divisible by neither 3 nor 5.

## Steps

1. Create an executable file
    ```shell
        touch fizz-buzz.py
        chmod u+x ./fizz-buzz.py
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
1. Create a loop that iterates from 1 to value
    ```python
        #...
        for val in range(1, value):
    ```
1. Insert FizzBuzz algorithm into loop
    ```python
        #... val in loop
        if val%3 == 0 and val%5 == 0:
            print("FizzBuzz")
        elif val%3 == 0:
            print("Fizz")
        elif val%5 == 0:
            print("Buzz")
        else:
            print(val)
    ```
1. End Product
   ```python
        #!/usr/bin/env python3.7
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
    ```
1. Execute test cases.
    ```shell
        #test case 1
        ./fizz-buzz.py
        15
        #Output: 1, 2, Fizz, 4, Buss, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz 
    ```
