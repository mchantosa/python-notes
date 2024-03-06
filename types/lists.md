# Lists
[home](../readme.md)
* [Creating Lists](#creating-lists-arrays)
* [Mutability](#mutability)
* [Accessing Elements](#accessing-elements)
* [Slicing Lists](#slicing-lists)
* [List Concatenation](#list-concatenation)
* [List Methods](#list-methods)

## Creating Lists (Arrays)
Lists in python are like arrays in JavaScript, create them with `[]`.
```python
    my_list = [False, 1, 2.0, 3+4j, "five", []]
    print(my_list) # Output: [False, 1, 2.0, (3+4j), 'five', []]
```
## Mutability
Lists are mutable. You can modify a list. 
```python
    my_list = [0, 1, 2, 3, 4, 5]
    my_other_list = my_list
    my_list_id = id(my_list)
    my_list[0] = "zero"
    print(my_other_list)    # Output: ['zero', 1, 2, 3, 4, 5]
    print(my_list_id == id(my_list)) # Output: True
```
## Accessing Elements
Individual elements in a list can be accessed using indexing. Indexing starts from 0 for the first character and negative indexing starts from -1 for the last character.
```python
    my_list[0, 1, 2, 3, 4, 5]
    print(my_list[0])  # Output: 0
    print(my_list[-1])  # Output: 5
    #don't try to go out of bounds, it will error
    #   my_list[15]
    #   my_list[-15]
```
## Slicing Lists
You can extract a sublist from a list using slicing. Slicing syntax is `list[start:end:step]`.
```python
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(my_list[0:5])   # Output: [0, 1, 2, 3, 4]
    print(my_list[7:])    # Output: [7, 8, 9, 10]
    print(my_list[0:])    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(my_list[0:500]) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(my_list[0:-1])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list[1::2])  # Output: [1, 3, 5, 7, 9]
    #reverse list
    print(my_list[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## List Concatenation, Edit, and Deletion
You can concatenate lists with `+` and `+=`
```python
    my_list = [0, 1, 2, 3, 4, 5]
    my_list = my_list + [6, 7]
    my_list += [8, 9, 10]
    print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #can modify a list via slice
    # 2->2
    my_list[0:2] = ["zero", "one"]
    print(my_list)  # Output: ['zero', 'one', 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 3->2 
    my_list[-2:] = ["nine", "ten", "11"]
    print(my_list)  # Output: ['zero', 'one', 2, 3, 4, 5, 6, 7, 8, 'nine', 'ten', '11']

    # remove elements
    my_list[-3:] = []
    print(my_list)  # Output: ['zero', 'one', 2, 3, 4, 5, 6, 7, 8]

    del my_list[-1] # No return value
    print(my_list)  # Output: ['zero', 'one', 2, 3, 4, 5, 6, 7]
```

## List Methods
* **append(elm):** push
* **insert(index, elm):** shift at specified index
* **index(elm):** return first occurrence 
* **in:** checks if array contains element
* **not in:** checks if array does not contain element
* **len(list):** returns list length
* **sorted(list):** sorts, not in place
* **reversed(list):** returns a reversed list iterator that converts to reversed list
```python
    my_list = [1, 2, 3]

    #push
    my_list.append(5)   #my_list = [1, 2, 3, 5]

    #insert and shift
    my_list.insert(3, "four")    #my_list = [1, 2, 3, "four", 5]
    my_list.insert(0, "zero")    #my_list = ['zero', 1, 2, 3, 'four', 5]

    #find first occurrence of x
    print(my_list.index("zero"))   # Output: 0
    #don't try to go out of bounds, it will error
    #   my_list.index("three")

    #is x in my list?
    print("four" in my_list)   # Output: True
    print("three" in my_list)  # Output: False
    print("four" not in my_list)   # Output: False
    print("three" not in my_list)  # Output: True

    #length
    len([0, 1, 2, 3, 4, 5]) # Output: 6

    #sorting
    print(sorted([1, 3, 5, 4, 2]))  # Output: [1, 2, 3, 4, 5]
    print(sorted(["a", "b", "c", "D", "E"]))    # Output: ['D', 'E', 'a', 'b', 'c']

    #reversed
    print(list(reversed([1, 3, 5, 4, 2]))) # Output: [2, 4, 5, 3, 1]
    print(list(reversed(sorted([1, 3, 5, 4, 2])))) # Output: [5, 4, 3, 2, 1]
```
## Nested Lists and Matrices
* **squares:** 2 x 2 matrix, (exam specific knowledge req)
* **cubes:** n x n matrix, (exam specific knowledge req)
    * 3 x 3: 3 cube
    * 5 x 5: 5 cube
```python
    #create a matrix
    my_matrix = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(my_matrix)    # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #get row count
    print(len(my_matrix))   # Output: 3
    #get column count, sort of, you know
    print(col_count = len(my_matrix[0]))    # Output: 3
    #access matrix[row][col]
    print(my_matrix[0][0], 
        my_matrix[0][2], 
        my_matrix[2][0], 
        my_matrix[2][2]
    )   # Output: 1, 3, 7, 9
```