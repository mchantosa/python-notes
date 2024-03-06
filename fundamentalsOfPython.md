# Fundamentals of Python
[home](./readme.md)

## About Python
Python is considered to be an interpreted language, not a compiled language, though it is nuanced because the interpreter compiles to an intermediate form. This is unlike Java which is both a compiled and an interpreted language. Java source code compiles bytecode which is then interpreted by a JVM or further compiled into native machine code using a just-in-time (JIT) compiler for improved performance. 

## Compilers and Interpreters
A compiler converts source code (something you write) into intermediate code (something that runs), though

1. Lexical analysis (Lexing)
1. Syntax analysis (Parsing)
1. Semantic analysis
1. Optimization
1. Code Generation

An Interpreter takes the source code and runs it

1. Will either parse code and execute it directly or
1. (Python) Or compile to an intermediate form (bytecode) and then execute

## Lexing
The process of breaking up source code into identified tokens.

```sh
    #Consider the following
    f = (c * 9 / 5) + 32

    #The Lexing process breaks this into 
    (ID) f, (EQUALS) =, (RPAREN) (, (ID) c, (TIMES) *, (NUM) 9, (DIV) /, (NUM) 5, (LPAREN) ), (PLUS) +, (NUM) 32
```
## Syntactical Analysis (Parsing)
Construct a parsing tree using tokens from the lexing process.
```sh
    #Parsing tree, informs in what order code should run

                    (Equals) = 
                /               \
            (ID) f              (PLUS) +
                                /       \
                            (DIV) /     (NUM) 32
                            /   \
                    (TIMES) *   (NUM) 5
                    /   \
                (ID) c  (NUM) 9
```
## Semantic Analysis
Layer of extra rules that don't apply to parsing
* Is there a type mismatch
* Is there an undeclared variable
* Is there a parameter mismatch
* ...

## Bytecode Instructions
Python is an interpreted language, but the source code is compiled to bytecode before being run. It is this bytecode that is run by the Python Virtual Machine (PVM).

## Using the REPL (Read Evaluate Print Loop)
Open terminal and type `python`, as a result, you should have a terminal with a prompt `>>>`. This is your Python REPL. In the REPL, you can enter lines or blocks of Python code, and the PVM will interpret and execute them. After executing the code, the REPL will display the output (if any), and then return you to the prompt, allowing you to enter more code or command.

Exit Python REPL with `exit()`

## Creating a Python File
1.  Create `code/hello.py`
    ```python
        print("Hello World")
    ```
1.  In terminal enter `python code/hello.py`. Boom! You should have a "Hello World" greeting.
1.  Let's make it executable
    ```python
        #!/usr/bin/env python

        print("Hello World")
    ```
1.  Identify the file as executable
    ```shell
        chmod u+x code/hello.py
    ```
1. From terminal enter `./code/hello.py`. Boom again! You should have a "Hello World" greeting.

## Python Keywords
These are predefined in Python, don't use these
|       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: |
|False|await|else|import|pass|
|None|break|except|in|raise|
|True|class|finally|is|return|
|and|continue|for|lambda|try|
|as|def|from|nonlocal|while|
|assert|del|global|not|with|
|async|elif|if|or|yield|