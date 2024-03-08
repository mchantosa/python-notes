# Using Python Lists
[home](../readme.md)

[using-lists.py](./code/using-lists.py)
## Learning Objectives
* Create a users List and Add Initial Items
* Remove bob and Create rev_users List
* Insert melody to users and Concatenate Lists
* Slice`users to Return 3rd and 4th Elements

### Objective: 
You have a file `using-lists.py`. If you open it, you will see itemized instructions, each item has an assert. Work your way through the list until all the asserts pass. An unmodified version of this file is located [here](./code/using-lists.py) for practice. 

## Steps

1. Open `using-lists.py` and run it
    ```shell
        python3.7 ./using-lists.py
    ```
1. Pass assert 1
    ```python
        # 1) Set the users variable to be an empty list
        users = []
        assert users == [], f"Expected `users` to be [] but got: {repr(users)}"
    ```
1. Pass assert 2
    ```python
        #...
        # 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
        users.append('kevin')
        users.append('bob')
        users.append('alice')
        assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"
    ```
1. Pass assert 3
    ```python
        #...
        # 3) Remove 'bob' from the users list without reassigning the variable.
        del users[1]
        assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"
    ```
1. Pass assert 4
    ```python
        #...
        # 4) Reverse the users list and assign the result to `rev_users`
        rev_users = list(reversed(users))
        assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"
    ```
1. Pass assert 5
    ```python
        #...
        # 5) Add the user 'melody' to users where 'bob' used to be.
        users.insert(1, "melody")
        assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"
    ```
1. Pass assert 6
    ```python
        #...
        # 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command
        users += ["andy", "wanda", "jim"]
        assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"
    ```
1. Pass assert 7
    ```python
        #...
        # 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
        center_users = users[2:4]
        assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"
    ```
1. End Product
    ```python
        # 1) Set the users variable to be an empty list
        users = []
        assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

        # 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
        users.append('kevin')
        users.append('bob')
        users.append('alice')
        assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

        # 3) Remove 'bob' from the users list without reassigning the variable.
        del users[1]
        assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

        # 4) Reverse the users list and assign the result to `rev_users`
        rev_users = list(reversed(users))
        assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"

        # 5) Add the user 'melody' to users where 'bob' used to be.
        users.insert(1, "melody")
        assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

        # 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command
        users += ["andy", "wanda", "jim"]
        assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

        # 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
        center_users = users[2:4]
        assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"
    ```