# Conditionals and Looping
[home](./readme.md)
* [If, Elif, Else](#if-elif-else)
* [Pass](#conditionals-and-looping)
* [While](#while)
* [For](#for)
* [Continue and Break](#continue-and-break)
* [For Else, While Else](#for-else-while-else)
* [Ranges](#ranges)
* [List Comprehensions](#list-comprehensions)
## If, Elif, Else
```python
    a = 0
    b = 0
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a equals b")
    # Output: a equals b
```
## pass
Using `pass` let's you define a code block that doesn't do anything, can be useful for structural logic. 
```python
    name = input("What is your name? ")
    print("Hi " + name + "!", end = " ")

    if name[0] in "aeiou":
        print("Your name begins with a vowel, interesting...", end = " ")
    else:
        pass    #do nothing
```
## While
```python
    count = 0
    while count < 3:
        print("count: ", count)
        count += 1
```
## For
```python
    colors = ["blue","green","red","orange"]
    for color in colors:
        print(color)

    numbers = (1, 2, 3, 4)
    for number in numbers:
        print(number)
        
    pets = {"Shive": "Sphinx", "Ashley": "Boston", "Blue": "Parakeet"}
    for key in pets:
        print(key, pets[key])
    for key, value in pets.items():
        print(key, value)

    for letter in "hello world":
        print(letter.upper())
``` 
## Continue and Break
```python
    count = 0
    while True:
        count += 1
        if count % 2 == 0:
            continue
        else:
            print(count, end=' ')
        if count > 6:
            print("")
            break
    # Output: 1 3 5 7 
```
## For Else, While Else
Else executes after for or while. More significantly, else doesn't execute if loop is broken.
```python
    #search_color = "orange"
    search_color = "green"
    colors = ["red", "orange", "yellow", "blue", "purple"]
    for color in colors:
        if color == search_color:
            print("yay, we have {}".format(search_color))
            break
    else: 
        print("we don't have {}".format(search_color))
    # Output: yay, we have orange
    #     or: we don't have green
```
## Ranges
```python
    print(list(range(10)))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(range(5, 10)))   # Output: [5, 6, 7, 8, 9]
    print(list(range(0, 11, 2)))    # Output: [0, 2, 4, 6, 8, 10]

    for i in range(3):
        print(i, end = "")
        # Output: 012
    else:
        print("")
```
## List Comprehensions
```python
    colors = ["red", "orange", "yellow", "blue", "purple"]

    upper_colors = [color.upper() for color in colors]
    warm_colors = [color for color in colors if color in ["red", "orange", "yellow"]]
    
    print(upper_colors) # Output: ['RED', 'ORANGE', 'YELLOW', 'BLUE', 'PURPLE']
    print(warm_colors)  # Output: ['red', 'orange', 'yellow']
```