# Dictionaries
[home](../readme.md)
* [Creating Strings](#creating-dictionaries-hashes-key-value-pairs)
* [Mutability and Access](#mutability-and-access)
* [Dictionary Methods](#dictionary-methods)

## Creating Dictionaries (Hashes, Key-Value Pairs)
Dictionaries in Python are like objects in JavaScript. Create a dictionary using `{}`, or using `dict`. As of Python 3.7 the key order is maintained. Keys must be immutable and unique, but don't have to be strings.
```python
    ages = {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38}
    print(ages) # Output: {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38}

    weights = dict(Jane = 160, John = 220, Sally = 120, Sam = 200)
    print(ages) # Output: {'Jane': 160, 'John': 220, 'Sally': 120, 'Sam': 200}

    colors = dict([("Jane", "green"),("John", "blue"),("Sally", "purple"),("Sam", "red")])
    print(colors)   # Output: {'Jane': 'green', 'John': 'blue', 'Sally': 'purple', 'Sam': 'red'}
```
## Mutability and Access
Dictionaries are mutable.
```python
    ages = {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38}

    #access
    print(ages["Jane"]) # Output: 30
    #don't try to access a non-existent key, it will error
    #   my_list['Billy']

    #mutable
    ages["Billy"] = 7
    print(ages) # Output: {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38, 'Billy': 7}
    ages["Billy"] += 1
    print(ages) # Output: {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38, 'Billy': 8}

    del ages["Billy"]
    print(ages) # Output: {'Jane': 30, 'John': 25, 'Sally': 36, 'Sam': 38}
```
## Dictionary Methods
* **keys():** returns a view object containing the keys of the dictionary, as a list
* **values():** returns view object containing the values of the dictionary, as a list
* **items():** returns view object containing key-value tuples, as a list
* **in:** checks if dictionary contains key
* **not in:** checks if dictionary does not contain key
* **len(dictionary):** returns number of key-value pairs
```python
    #keys
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.keys()
    y = list(x)

    #   x references keys, y does not
    car["color"] = "white"
    print(x)    # Output: dict_keys(['brand', 'model', 'year', 'color'])
    print(y)  #Output: ['brand', 'model', 'year']

    #values
    print(car.values()) # Output: dict_values(['Ford', 'Mustang', 1964, 'white'])

    #items
    print(car.items())  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

    #in and not in
    print("electric" in car)  # Output: False
    print("color" in car)   # Output: True
    print("electric" not in car)  # Output: True
    print("color" not in car)   # Output: False

    #length
    print(len(car)) # Output: 3
```