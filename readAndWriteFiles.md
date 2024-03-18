# Interacting with Files
[home](readme.md)
[Function documentation](https://docs.python.org/3/library/functions.html)

* **open:** Open file and return a corresponding file object.
* **write:** to a file
* **writelines:** write an sequence of elements to a file
* **close:** close the file (this will ensure that all the writes happened)
    * Will auto-close if you access within a with statement

## Write to a file
```python
    #write to a file
    my_file = open('xmen.txt', 'w+') #this file doesn't need to exist yet, write+read
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n', 
        'Nightcrawler\n'
    ])
    my_file.close()
```

## Read from a file
```python
    #if you call with "with", it auto-closes the file
    with open('xmen.txt', 'r') as my_file: 
        my_file = open('xmen.txt', 'r') #read only
        print(my_file.read())
        print("I'm reading again")
        print(my_file.read())   #only reads once, cursor was already at the end
        print("Moved cursor back to beginning\n")
        my_file.seek(0) #go back to the beginning
        print(my_file.read())
```