# Defining and Using Python Functions
[home](../readme.md)

[testing-functions.py](./code/testing-functions.py)
## Learning Objectives
* Create the split_names Function to Separate Names
* Create the is_palindrome Function to Determine if a String or Number Is a Palindrome
* Create the build_list Function to Take an Item and a Count and Return a List with item Repeated count Times

### Objective: 
You have a file `testing-functions.py`. If you open it, you will see itemized instructions, each item has an assert. Work your way through the list until all the asserts pass. An unmodified version of this file is located [here](./code/testing-functions.py) for practice. 

## Steps

1. Open `using-dictionaries.py` and run it
    ```shell
        python3.7 ./using-functions.py
    ```
1. Pass asserts 1 and 2
    ```python
        # 1) Create the split_names Function to Separate Names
        # 2) Ensure that `split_name` can handle multi-word last names

        def split_name(name):
            first_name, last_name = name.split(maxsplit=1)
            return {
                'first_name': first_name,
            }
    ```
1. Pass asserts 3 and 4
    ```python
        #...
        # 3) Write an `is_palindrome` function to check if a string is a palindrome 
        # 4) Make `is_palindrome` work with numbers

        def is_palindrome(str_or_num):
            return str(str_or_num)[::-1] == str(str_or_num)
    ```
1. Pass asserts 5
    ```python
        #...
        # 5) Write a `build_list` function that takes an item and a number to include in a list

        def build_list(item, count):
            return_list = []
            for _ in range(count):
                return_list.append(item)
            return return_list
    ```

1. End Product
    ```python
        # 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name
        def split_name(name):
            first_name, last_name = name.split(maxsplit=1)
            return {
                'first_name': first_name,
                'last_name': last_name,
            }
        assert split_name("Kevin Bacon") == {
            "first_name": "Kevin",
            "last_name": "Bacon",
        }, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

        # 2) Ensure that `split_name` can handle multi-word last names

        assert split_name("Victor Von Doom") == {
            "first_name": "Victor",
            "last_name": "Von Doom",
        }, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

        # 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)
        def is_palindrome(str_or_num):
            return str(str_or_num)[::-1] == str(str_or_num)

        assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
        assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

        # 4) Make `is_palindrome` work with numbers

        assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
        assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

        # 5) Write a `build_list` function that takes an item and a number to include in a list
        def build_list(item, count =1):
            return_list = []
            for _ in range(count):
                return_list.append(item)
            return return_list
        assert build_list("Apple", 3) == [
            "Apple",
            "Apple",
            "Apple",
        ], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
        assert build_list("Orange") == [
            "Orange"
        ], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
    ```