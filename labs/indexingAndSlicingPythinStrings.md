# Indexing and Slicing Python Strings
[home](../readme.md)

[string-info.py](./code/string-info.py)
## Learning Objectives
* Create the `string-info.py` Script and Take User Input
* Print the First, Last, and Middle Characters from the User's Input
* Print the Even Index Characters and Odd Index Characters
* Print the String in Reverse

### Objective: 
Create an executable file `string-info.py` that prompts the user for a message and prints out to the user string manipulations from that message

## Steps

1. Create an executable file
    ```shell
        touch string-info.py
        chmod u+x ./string-info.py
    ```
    Remember, this class uses python 3.7, use python locally.
    ```python
        #!/usr/bin/env python3.7
    ```
1. Prompt and Store message from User
    ```python
        #...
        message = input("Enter a message: ")
    ```
1. Print the First, Last, and Middle Characters from the User's Input
    ```python
        #...
        print("First character: ", message[0])
        print("Last character: ", message[-1])
        print("Middle character: ", message[int(len(message)/2)])
    ```
1. Print the Even Index Characters and Odd Index Characters
    ```python
        #...
        print("Even index characters: ", message[0::2])
        print("Odd index characters: ", message[1::2])
    ```
1. Print the String in Reverse
    ```python
        #...
        print("Reversed message:", message[::-1])
    ```
1. End Product
   ```python
        #!/usr/bin/env python

        message = input("Enter a message: ")
        print("First character: ", message[0])
        print("Last character: ", message[-1])
        print("Middle character: ", message[int(len(message)/2)])
        print("Even index characters: ", message[0::2])
        print("Odd index characters: ", message[1::2])
        print("Reversed message:", message[::-1])
    ```
1. Execute test cases.
    ```shell
        #test case 1
        ./string-info.py
        abc  
        #Output:
        #   Enter a message: abc
        #   First character:  a
        #   Last character:  c
        #   Middle character:  b
        #   Even index characters:  ac
        #   Odd index characters:  b
        #   Reversed message: cba

        #test case 2
        ./string-info.py
        abcd 
        #Output:
        #   Enter a message: abcd
        #   First character:  a
        #   Last character:  d
        #   Middle character:  c
        #   Even index characters:  ac
        #   Odd index characters:  bd
        #   Reversed message: dcba

        #test case 3
        ./string-info.py
        test message
        #Output: 
        #   Enter a message: test message
        #   First character:  t
        #   Last character:  e
        #   Middle character:  e
        #   Even index characters:  ts esg
        #   Odd index characters:  etmsae
        #   Reversed message: egassem tset
    ```
