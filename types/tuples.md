# Tuples
[home](../readme.md)
* [Creating Tuples](#creating-tuples)
* [Mutability](#mutability)
* [Accessing Elements](#accessing-elements)
* [Tuple Operations](#tuple-operations)
* [Tuple or List?](#tuple-or-list)
* [Nesting Tuples and Lists](#nesting-tuples-and-lists)

## Creating Tuples
What is a tuple? Tuples are similar to lists, but they are immutable. You create tuples with `()`.
```python
    point_2d = (-3.14/2, -1)
    print(point_2d) # Output: (-1.57, -1)
```

## Mutability
Tuples are immutable. You can't modify a tuple. 
```python
    point_2d = (-3.14/2, -1)
    print(point_2d) # Output: (-1.57, -1)
    point_2d_id = id(point_2d)
    point_2d += (0, )
    print(point_2d) # Output: (-1.57, -1, 0)

    #For a list, this would be True
    print(point_2d_id == id(point_2d))  # Output: False
```

## Accessing Elements
```python
    point_3d = (-3.14/2, -1, 0)
    print(point_3d[0])  # Output: -1.57
    x, y, z = point_3d
    print(x, y, z)  # Output: -1.57 -1 0
```

## Tuple Operations
```python
    point_2d = (-3.14/2, -1)
    point_3d = point_2d + (0, ) #must add a tuple
    print(point_3d) # Output: (-1.57, -1, 0)
```

## Tuple or List?
* Don't know the size that the container will need to be? Use list
* I want to model something with specific fields and a specific number of fields: use tuples
* I need to return multiple pieces of information from one function: use tuples for unpacking

## Nesting Tuples and Lists
You can nest a list in a tuple and mutate the list in the tuple, even if the tuple itself is immutable. 
```python
    my_inner_list = [1, 2, 3, "a list"]
    my_tuple = (my_inner_list, "in a tuple")
    my_outer_list = [my_tuple, "in anther list" ]
    print(my_outer_list)    # Output: [([1, 2, 3, 'a list'], 'in a tuple'), 'in anther list']

    #modify a list in a tuple
    my_tuple[0].append("I changed")
    print(my_outer_list)    # Output: [([1, 2, 3, 'a list', 'I changed'], 'in a tuple'), 'in anther list']

    #careful
    my_tuple += ("I CHANGED TOO",)    
    print(my_tuple) # Output: ([1, 2, 3, 'a list', 'I changed'], 'in a tuple', 'I CHANGED TOO')
    print(my_outer_list)    # Output: [([1, 2, 3, 'a list', 'I changed'], 'in a tuple'), 'in anther list']
```