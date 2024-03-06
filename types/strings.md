# Strings
[home](../readme.md)
* [Creating Strings](#creating-strings)
* [Immutability](#immutability)
* [Accessing Characters](#accessing-characters)
* [Slicing Strings](#slicing-strings)
* [String Concatenation](#string-concatenation)
* [String Methods](#string-methods)
* [White Space](#white-space)
* [Escaping Characters](#escaping-characters)


## Creating Strings
You can create strings using single quotes, double quotes, or triple quotes for multi-line strings. Strings are iterable. Strings in Python are immutable, meaning once they are created, their contents cannot be changed. 
 
```python
    my_string = 'this is a string'

    my_string = "this is also a string"

    my_string = '''
    this is a 
    multiline string
    '''

    my_string = """
    this is also a 
    multiline string
    """
```

## Immutability
There will not be more that one explicit string literal in memory. 
```python
    my_str1 = "literal"
    my_str2 = "literal"
    print(id("literal") == id(my_str1) == id(my_str2))  # Output: True
```

## Accessing Characters
Individual characters in a string can be accessed using indexing. Indexing starts from 0 for the first character and negative indexing starts from -1 for the last character.
```python
    my_string = "Hello"
    print(my_string[0])  # Output: H
    print(my_string[-1])  # Output: o
    #don't try to go out of bounds, it will error
    #   my_string[15]
    #   my_string[-15]
```

## Slicing Strings
You can extract a substring from a string using slicing. Slicing syntax is `string[start:end:step]`.
```python
    my_string = "Hello, World!"
    print(my_string[0:5])   # Output: Hello
    print(my_string[7:])    # Output: World!
    print(my_string[0:])    # Output: Hello, World!
    print(my_string[0:500]) # Output: Hello, World!
    print(my_string[0:-1])  # Output: Hello, World
    print(my_string[1::2])  # Output: el,Wrd
    #reverse string
    print(my_string[::-1])  # Output: !dlroW ,olleH
```

# String Concatenation
You can concatenate strings using the `+` operator. You can also use `+=`, `*`, and `*=` on strings
```python
    my_string1 = "Hello"
    my_string2 = "World"
    concatenated_str = my_string1 + ", " + my_string2
    print(concatenated_str)  # Output: Hello, World

    my_string = "Hello"
    my_string += " World!"
    print(my_string)  # Output: Hello World!

    print("Ho" * 2)   # Output: HoHo
    print(2 * "Ho")   # Output: HoHo
    
    my_string = "Ho"
    my_string *= 3
    print(my_string)  # Output: HoHoHo
```
## String Methods
* **ord(char):** returns unicode code point of character
* **chr(uni_cp):** returns char for unicode code point
* **len(string):** number of characters in string
* **split(sep):** split string by separator, returns list
* **join(list):** join elements of list with string as separator
* **format(str\*):** format a templated string
* **upper():** to upper case
* **lower():** to lower case
* **title():** capitalize first letter of words within string
* **capitalize():** capitalize first letter of sentence
* **replace(char, r_char):** replaces all occurrences of `char` with `r_char`
* **find(subStr):** return the first occurrence of this substring
* **count(subStr):** return the count of occurrences of this substring
* **strip(str):** remove any of characters from `str` encountered in string, treat `str` like a set of characters. Null `str` value removes whitespace from either end.

```python
    #ord, chr
    print(ord("A"), ord("Z"), ord("a"), ord("z")) # Output: 65 90 97 122
    print(ord("\u03C0"), ord("π"), int(0x3c0), "\u03C0")    # Output: 960 960 960 π
    print(chr(97), chr(0x61), chr(960), chr(0x3c0)) # Output: a a π π
    
    #split, join
    print(len("my_string"))  # Output: 9
    print("hello, world".split(", "))    # Output: ['hello', 'world']
    print(", ".join(["hello", "world"]))    # Output: hello, world

    #format version 1
    template = "My name is {} and I love {}!"
    print(template.format("Shiva", "tuna")) # Output: My name is Shiva and I love tuna!
    print(template.format("Shiva", "tuna", "extra"))    # Output: ditto to above
    #don't try to go out of bounds, it will error
    #   template.format("Shiva")
    template = "My name is {0} and I love {1}! -{0} out"
    print(template.format("Shiva", "tuna")) # Output: My name is Shiva and I love tuna! -Shiva out
    
    #format version 2
    name = "Shiva"
    thing_i_love = "tuna"
    print(f"My name is {name} and I love {thing_i_love}!")

    #upper, lower, title, capitalization
    print("hello world!".upper())  # Output: HELLO WORLD!
    print("Hello World!".lower())  # Output: hello world!
    print("hello world!".title())  # Output: Hello World!
    print("hello world!".capitalize())  # Output: Hello world!

    #replace, find count, strip
    print("HHello world!".replace("H", "j"))    # Output: jjello, World!
    print("hello world!".find("l"))    # Output: 2
    print("hello world!".count("l"))    # Output: 3
    print("lllll".count("ll"))  # Output: 2
    print("hello world!".strip("d!he"))    # Output: llo worl
    print("\n\t  hello world!  \t\n".strip())    # Output: hello world!

    #isxxxx
    print("hello world!"[0:5].isascii())    # Output: True
    print("hello world!"[0:5].isalpha(), " ".isalpha(), "".isalpha())    # Output: True False * 2
    print("123abc".isalnum(), "123 abc".isalnum())  # Output: True False
    print("2\u03C0r".isprintable(), "2\u03C0r\n".isprintable())   # Output: True False
    print("1str".isidentifier(), "str1".isidentifier()) # Output: False True
    print("1.0".isdigit(), "1.0".isdecimal(), "1.0".isnumeric()) # Output: False * 3
    print("10".isdigit(), "10".isdecimal(), "10".isnumeric()) # Output: True * 3
    print("hello world!".islower())    # Output: True
    print("Hello World!".isupper())    # Output: False
    print("hello world!"[5].isspace())    # Output: True

    #startswith, endswith
    print("hello world!".startswith("h"))    # Output: True
    print("hello world!".endswith("!"))    # Output: True 
    
```

## White Space
You can use escaping characters in Python to represent special whitespace characters such as newline (\n), tab (\t), carriage return (\r).
```python
    my_string = "    Hello, World!    "
    print(my_string)  # Output:     Hello, World!
    print(my_string.strip())  # Output: Hello, World!
    my_string = "\n\t Hello, World! \n\t"
    print(my_string)    # Output:
                        # 
                        #            Hello, World!
                        #
    print(my_string.strip())  # Output: Hello, World!
```

## Escaping Characters
In Python, escaping characters involves using a backslash () before certain characters to indicate that they should be treated as literal characters rather than having their special meaning in strings or regular expressions.
```python
    #quotes within a string
    my_string = "Hello, \"World!\""
    print(my_string)  # Output: Hello, "World!"
    my_string = "Hello, \'World!\'"
    print(my_string)  # Output: Hello, 'World!'

    #backslashes within a string
    my_string = "Hello, \\World!"
    print(my_string)  # Output: Hello, \World!

    #special characters within a string
    my_string = "Hello, \nWorld!"
    print(my_string)  # Output: Hello,
                    #         World!
    my_string = "Hello, \tWorld!"
    print(my_string)  # Output: Hello,    World!

    #backspace
    my_string = "Hello, \bWorld!"
    print(my_string)  # Output: Hello,World!

    #carriage return
    my_string = "Hello, \rWorld!"
    print(my_string)  # Output: World!
```