# Operators
[home](./readme.md)
* [Bitwise Operators {~, |, &, ^, >>, <<}](#bitwise-operators)
* [Boolean Operators {not, or, and}](#boolean-operators-on-bools)
* [Boolean Operators on Truthy/Falsy {not, or, and}](#boolean-operators-on-truthyfalsy)
* [Comparison Operators {>, >=, <, <=, ==, !=, is, is not}](#comparison-operators)
* [Order of Operations Table](#order-of-operations)

An operator is a symbol that denotes or performs a mathematical or logical operation. A unary operators are operators with only one operand. 

## Bitwise Operators
Bitwise operators do comparisons along a set of binary values. 
```python
    #Twos compliment, bitwise unary operator, for a an int, ~ a = -(a + 1)
    print(~10)  # Output: +0b1010 -> -0b[0101]1, -0b1011 = -11

    a = 0b1001
    b = 0b1100

    #bitwise or
    print(bin(a | b))    # Output: 0b1101, TTFT bitwise comparison
    print(a | b)    # Output: int(0b1101) -> 13

    #bitwise and
    print(bin(a & b))    # Output: 0b1000, TFFF bitwise comparison
    print(a & b)    # Output: int(0b1000) -> 8

    #bitwise xor, exclusive or
    print(bin(a ^ b))    # Output: 0b0101, FTFT bitwise comparison
    print(a ^ b)    # Output: int(0b0101) -> 5

    #shift right
    print(0b11111 >> 2) # Output: 7 (0b111, the two shifted values are truncated)  

    #shift left
    print(0b111 << 2) # Output: 28 (0b11100, padded with 0s)   
```

## Boolean Operators on Bools
```python
    #not, a unary operator
    print(not True) # Output: False
    print(not False)    # Output: True

    #or
    print(True or False) # Output: True
    print(False or False) # Output: False

    #and
    print(True and True) # Output: True
    print(False and True) # Output: False
```
## Boolean Operators on Truthy/Falsy
```python
    #not
    #   returns True or False, the negation of the falsy value
    print(not [])   # Output: True
    print(not "a")  # Output: False

    #or
    #   returns the first truthy value or the last falsy value
    print(0 or "a" or "b")  # Output: "a"
    print([] or None or '')  # Output: ''

    #and
    #   returns the first falsy or the last truthy
    print("a" and "b")  # Output: "b"
    print([] and "b")  # Output: []
```

## Comparison Operators
```python
    #greater than
    print(1 > 1)    # Output: False
    print(1 >= 1.0)    # Output: True
    print('a' > 'b')    # Output: False
    print('b' > 'a')    # Output: True
    print('bbb' > 'bbc')    # Output: False
    #   print('a' > 1), type error

    #less than
    print(1 < 1)    # Output: False
    print(1 <= 1.0)    # Output: True
    print('a' < 'b')    # Output: True
    print('B' < 'a')    # Output: True
    print('B'.lower() < 'a')    # Output: False

    #equivalence
    print(1 == 1)   # Output: True
    print(1 == 1.0)   # Output: True
    print('a' == 1)   # Output: False

    #not equivalent
    print(1 != 1.0)     # Output: False
    print(1 != 2)     # Output: True

    #identity is, (same place in memory)
    print(id(1))    # Output: 1's place in memory
    print(1 is 1)   # Output: True, id(1) == id(1) is true
    print(1 is 0b1) # Output: True, id(1) == id(0b1) is true
    print(1 is 1.0) # Output: False, id(1) == id(1.0) is false

    #is not (different place in memory)
    print('a' is not 'b')   # Output: True, id('a') != id('b') is true
```

## Order of Operations
|Operator|Description|
|:--|:--|
|(expressions...), [expressions...], {key: value...}, {expressions...}|Binding or parenthesized expression, list display, dictionary display, set display|
|x[index], x[index:index], x(arguments...), x.attribute|Subscription, slicing, call, attribute reference|
|await x|Await expression|
|**|Exponentiation|
|+x, -x, ~x|Positive, negative, bitwise NOT|
|*, @, /, //, %|Multiplication, matrix multiplication, division, floor division, remainder|
|+, -|Addition and subtraction|
|<<, >>|Shifts|
|&|Bitwise AND|
|^|Bitwise XOR|
|\||Bitwise OR|
|in, not in, is, is not, <, <=, >, >=, !=, ==|Comparisons, including membership tests and identity tests|
|not x|Boolean NOT|
|and|Boolean AND|
|or|Boolean OR|
|if – else|Conditional expression|
|lambda|Lambda expression|
|:=|Assignment expression|
```python
    #Example
    #   14 & 2* 3 + 4 
    #   -> 14 & 6 + 4
    #   -> 14 & 10 
    #   -> 0b1110 & 0b1010
    #   -> 0b1010
    #   -> 10
    print(14 & 3 * 2 + 4)   # Output: 6
```