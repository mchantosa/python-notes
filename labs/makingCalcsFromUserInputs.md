# Making Calculations From User Inputs
[home](../readme.md)

Create an executable file that prompts the user for a temperature in fahrenheit and prints a conversion "[fahrenheit] F is [celsius] C," where celsius is rounded to 2 digits. 

```shell
    touch to-celsius.py
    chmod u+x ./to-celsius.py
```

Remember, this class uses python 3.7, use python locally.

```python
    #!/usr/bin/env python3.7

    fahrenheit = float(input("What temperature in fahrenheit would you like converted to celsius?"))
    celsius = (fahrenheit -32)*5/9
    print(fahrenheit,"F is", round(celsius, 2), "C")
```
Execute test cases.
```shell
    #test case 1
    ./to-celsius.py
    32  # Outputs: 0

    #test case 2
    ./to-celsius.py
    41  # Outputs: 5
```
