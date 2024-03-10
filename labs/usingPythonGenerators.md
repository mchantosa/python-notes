# Using Python Generators
[home](../readme.md)

[using-generators.py](./code/using-generators.py)
## Learning Objectives
* Create the char_range Generator
* Include the Stop Character in the Results
* Support the Start Code Point Being More Than the Stop Code Point

### Objective: 
You have a file `using-generators.py`. If you open it, you will see a place to create your generator as well as a set of asserts that your generator must pass. Work your way through the asserts until they all pass. An unmodified version of this file is located [here](./code/using-generators.py) for practice. 

## Steps

1. Open `using-generators.py` and run it
    ```shell
        python3.7 ./using-generators.py
    ```

1. End Product
    ```python
        # Define the `char_range` generator here
        def char_range(start, stop, step = 1):
            stop_modifier = 1
            start_code = ord(start)
            stop_code = ord(stop)
            if start_code > stop_code:
                step*=-1
                stop_modifier*=-1
            for value in range(start_code, stop_code + stop_modifier, step):
                yield chr(value)

        # Tests to verify the implementation of char_range
        # *Do not modify
        ##################################################

        # Ensure that `char_range` is a generator function
        from inspect import isgeneratorfunction

        assert isgeneratorfunction(
            char_range
        ), f"Expected char_range to be a generator function but was not."

        # Ensure that the result *does* includes the stop character
        assert list(char_range("a", "e")) == [
            "a",
            "b",
            "c",
            "d",
            "e",
        ], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"

        # Iterate backwards if the start code point is higher than the stop code point

        assert list(char_range("e", "a")) == [
            "e",
            "d",
            "c",
            "b",
            "a",
        ], f"Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"

        # Properly step if a step value is provided

        assert list(char_range("a", "e", 2)) == [
            "a",
            "c",
            "e",
        ], f"Expected ['a', 'c', 'e'] but got {repr(list(char_range('a', 'e', 2)))}"

        # Step properly if the start code point is higher than the stop code point

        assert list(char_range("e", "a", 2)) == [
            "e",
            "c",
            "a",
        ], f"Expected ['e', 'c', 'a'] but got {repr(list(char_range('e', 'a', 2)))}"
    ```