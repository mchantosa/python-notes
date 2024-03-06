# Functions
[home](./readme.md)
* [Defining a Function](#defining-a-function)
* [Parameters and Arguments](#parameters-and-arguments)
    * [Explicit Verses Position Based Arguments](#explicit-verses-position-based-arguments)
    * [Using Default Arguments](#using-default-arguments)
* [Recursion](#recursion)

## Defining a Function
```python
    def print_something(something):
        print(something)

    def add(a, b):
        return a + b

    print_something("Shiva is mad at me")
    print(add(3, 5))
```

## Parameters and Arguments
### Explicit Verses Position Based Arguments 
```python
    def contact_card(name, age, phone):
        return f"{name}:\n\tage: {age}\n\tphone: {phone}"

    #position based arguments
    print(contact_card("Zoe", 9, "123-456-7890"))
    #explicitly defined arguments
    print(contact_card(age = 9, phone = "123-456-7890", name = "Zoe"))
    #split arguments
    print(contact_card("Zoe", phone = "123-456-7890", age = 9))
    # Output:
    #           Zoe:
    #               age: 9
    #               phone: 123-456-7890 
```
### Using Default Arguments
```python
def can_drive_wa(age, drivers_ed = False, driving_age = 18):
    if drivers_ed:
        driving_age = 16
    return age >= driving_age

print(can_drive_wa(18)) # Output: True
print(can_drive_wa(17)) # Output: False
print(can_drive_wa(17, True))   # Output: True
```
## Recursion

```python

```