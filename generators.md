# Generators
[home](./readme.md)
* [Creating Generators](#creating-generators)
* [Using Generators](#using-generators)
* [Converting to Lists](#converting-to-lists)

## Creating Generators
Generators are functions that behave like iterators. 
```python
    def generate_range(stop, start = 1, step = 1):
        num = start
        while num <= stop:
            yield num   #this makes it a generator
            num += step
```
## Using Generators
```python
    #next
    gen = generate_range(3)
    print(next(gen))    # Output: 1
    print(next(gen))    # Output: 2
    print(next(gen))    # Output: 3
    #another call will result in error

    #in a loop
    gen = generate_range(3)
    for num in gen:
        print(num)  # Output: 1 2 3
```
## Converting to Lists
```python
    gen = generate_range(3)
    print(gen)
    print(list(gen))

    #but what if your generator is infinite?
    def gen_fib():
        a, b = 0, 1
        while True:
            a, b = b, a + b
            yield a

    def fib(n):
        fib = gen_fib()
        return [next(fib) for _ in generate_range(n)][-1]
```