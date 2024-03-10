# Using Python Generators
[home](../readme.md)

[using-generators.py](./code/using-generators.py)
## Learning Objectives
* Create the char_range Generator
* Include the Stop Character in the Results
* Support the Start Code Point Being More Than the Stop Code Point

### Objective: 
You have a file `using-generators.py`. If you open it, you will see itemized instructions, each item has an assert. Work your way through the list until all the asserts pass. An unmodified version of this file is located [here](./code/using-generators.py) for practice. 

## Steps

1. Open `using-generators.py` and run it
    ```shell
        python3.7 ./using-generators.py
    ```s
1. Pass assert 1
    ```python
        # 1) Create the char_range Generator
        def generate_range(stop, start = 1, step = 1):
            num = start
            while num <= stop:
                yield num   #this makes it a generator
                num += step

    ```
1. Pass assert 2
    ```python
        #...
        # 2) Include the Stop Character in the Results
        
    ```
1. Pass assert 3
    ```python
        #...
        # 3) Support the Start Code Point Being More Than the Stop Code Point
        
    ```

1. End Product
    ```python
        
    ```