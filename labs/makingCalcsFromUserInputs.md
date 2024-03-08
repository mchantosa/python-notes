# Making Calculations From User Inputs
[home](../readme.md)

[to-celsius.py](./code/to-celsius.py)

## Learning Objectives
1. Create the ~/to-celsius.py Script and Make It Executable with python3.7
1. Prompt and Store Fahrenheit Value from User
1. Calculating the Celsius Value
1. Print the Calculated Value to the Screen

### Objective: 
Create an executable file that prompts the user for a temperature in fahrenheit and prints a conversion "[fahrenheit] F is [celsius] C," where celsius is rounded to 2 digits. 

## Steps
1. Create an executable file
    ```shell
        touch to-celsius.py
        chmod u+x ./to-celsius.py
    ```
    Remember, this class uses python 3.7, use python locally.
    ```python
        #!/usr/bin/env python3.7
    ```
1. Prompt and Store Fahrenheit Value from User
    ```python
        #...
        fahrenheit = float(input("What temperature in fahrenheit would you like converted to celsius?"))
    ```
1. Calculate the Celsius Value
    ```python
        #...
        celsius = (fahrenheit -32)*5/9
    ```
1. Print the Calculated Value to the Screen
    ```python
        #...
        print(fahrenheit,"F is", round(celsius, 2), "C")
    ```
1. End Product
    ```python
        #!/usr/bin/env python3.7

        fahrenheit = float(input("What temperature in fahrenheit would you like converted to celsius?"))
        celsius = (fahrenheit -32)*5/9
        print(fahrenheit,"F is", round(celsius, 2), "C")
    ```
1. Execute test cases.
    ```shell
        #test case 1
        ./to-celsius.py
        32  # Outputs: 0

        #test case 2
        ./to-celsius.py
        41  # Outputs: 5
    ```
