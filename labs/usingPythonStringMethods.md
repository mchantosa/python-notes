# Indexing and Slicing Python Strings
[home](../readme.md)

[variations.py](./code/variations.py)
## Learning Objectives
* Create the `variations.py` Script, Make It Executable with python3.7, and Accept User Input
* Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input
* Separate the String and Present the Individual Words as a List
* Print the Alphabetic First and Last Words from the User's Input

### Objective: 
Create an executable file `variations.py` that prompts the user for a message and prints out to the user string manipulations from that message

## Steps

1. Create an executable file
    ```shell
        touch variations.py
        chmod u+x ./variations.py
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
1. Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input
    ```python
        #...
        print("Lowercase:", message.lower())
        print("Uppercase:", message.upper())
        print("Capitalized:", message.capitalize())
        print("Title Case:", message.title())
    ```
1. Separate the String and Present the Individual Words as a List
    ```python
        #...
        print("Words:", words)
    ```
1. Print the Alphabetic First and Last Words from the User's Input
    ```python
        #...
        print("Alphabetic First Word:", sorted_words[0])
        print("Alphabetic Last Word:", sorted_words[-1])
    ```
1. End Product
   ```python
        #!/usr/bin/env python

        message = input("Enter a message: ")
        print("Lowercase:", message.lower())
        print("Uppercase:", message.upper())
        print("Capitalized:", message.capitalize())
        print("Title Case:", message.title())

        words = message.split()
        print("Words:", words)

        sorted_words = sorted(words)
        print("Alphabetic First Word:", sorted_words[0])
        print("Alphabetic Last Word:", sorted_words[-1])
    ```
1. Execute test cases.
    ```shell
        #test case 
        ./variations.py
        'This is a test case'
        #Output:
        #   Enter a message: This is a test case
        #   Lowercase: this is a test case
        #   Uppercase: THIS IS A TEST CASE
        #   Capitalized: This is a test case
        #   Title Case: This Is A Test Case
        #   Words: ['This', 'is', 'a', 'test', 'case']
        #   Alphabetic First Word: This
        #   Alphabetic Last Word: test
    ```
