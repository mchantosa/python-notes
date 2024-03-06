# Numbers
[home](../readme.md)

Number types in python are int, float, and complex
```python
    #Integers
    my_int = 2

    #Floats
    my_float = 2.0
    my_float = 4.5e9

    #Complex
    my_complex = 2 + 3j
```

## Operators
```python
    #Addition
    print(2 + 2)    # Output: 4
    print(2.0 + 2.0)    # Output: 4.0
    print(2 + 2.0)    # Output: 4.0

    #Subtraction
    print(2 - 2.0)    # Output: 0.0

    #Multiplication
    print(3 * 9)    # Output: 27 

    #Division
    print(5 / 3)    # Output: 1.66666...7 (old deprecated python2 returned an int)
    print(9 / 3)    # Output: 3.0 (will always return float)

    #Floor Division
    print(5 // 3)   # Output: 1 (int return rounded down)

    #Modulo
    print(5 % 3)    # Output: 2

    #Exponents
    print(2 ** 3)   # Output: 8
    print(27 ** (1/3))   # Output: 3.0
```

## Number systems
```python
    #Decimal(0-9)
    my_num = 10

    #Binary(0-1)
    my_bim = 0b1010

    #bitwise not, or twos compliment
    #   Twos compliment for int n = -(n+1)
    #   a + ~a = -1 => ~a = -1-a = -(a + 1)
    #   let a = 10, ~a = -(10+1) = -(0b1010+1) = -0b1011 = -11
    #   let a = 5, ~a = -(5+1) = -(0b101+1) = -0b110 = -6
    my_twosComp = ~10 #-11

    #Octal(0-7)
    my_oct = 0o12

    #Hexadecimal(0-9 and A-F)
    my_hex = 0xA

    #convert from 
    print(hex(10))      # Output: 0xa
    print(oct(10))      # Output: 0o12
    print(bin(10))      # Output: 0b1010
    print(int(0xa))     # Output: 10
    print(int(0o12))    # Output: 10
    print(int(0b1010))  # Output: 10

    print(0xa == 0b1010)    # Output: True
```

