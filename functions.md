# Functions
[home](./readme.md)

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

## Recursion
```python

```