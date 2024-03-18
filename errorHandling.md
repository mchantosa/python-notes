# Error Handling
[home](readme.md)

[try documentation](https://docs.python.org/3/reference/compound_stmts.html#try)
# Example
Consider this file, if you run it once, it creates `recipes.txt`, if you run it again it errors. It errors because `recipes.txt` already exists. 
```python  
    my_file = open('recipes.txt', 'x')  #x is mode for creation
    my_file.write('meatballs\n')
    my_file.close()
```
Wrap problematic code in a try block. If you run this code again, you get a nice error that says that this file already exists. 
```python
    import sys

    file_name = 'recipes.txt'
    try:
        my_file = open(file_name, 'x')  #x is mode for creation
        my_file.write(b'meatballs\n')   #triggers error 2
        my_file.close()

    except FileExistsError as err:
        print(f"{file_name} already exists")
        sys.exit(1) #non zero exit code means error

    except:
        print(f"Unable to write to the file")
        sys.exit(1)
```
What if you want to use an `else` or a `finally`? You need to remove your `sys.exit` statements to access them.
```python
    import sys

    file_name = 'recipes.txt'
    try:
        my_file = open(file_name, 'x')  #x is mode for creation
        #my_file.write(b'meatballs\n')   #toggle for error 2
        my_file.write('meatballs\n')    
        my_file.close()

    except FileExistsError:
        print(f"{file_name} already exists")

    except:
        print(f"Unable to create {file_name}")

    else:
        print(f"{file_name} was created")

    finally:
        print("Executing completed")
```