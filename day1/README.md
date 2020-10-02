# Python

## Basics

### Environment

  - Install Python
  - Python REPL
  - A Text Editor (VS Code or similar)

### Introduction

  - Numbers
    - Arithmetic ops
  - Strings
    - concatenation
    - single/double quotes
    - raw strings `r'string'`
    - multiline strings
  - Lists
    - append()
    - len()

### Programming
  - Looping
    - while
    - if
    - for
    - range()
    - break, continue, else
    - pass

### Functions

  - positional arguments
  - default and keyword arguments

### Data Structures

  - More Lists
    - insert
    - count
    - sort
    - reverse
    - list comprehensions
  - Tuples
  - Sets
  - Dictionaries
    - looping using items()

### Modules

  - file with funcs and vals
  - standard modules
    - sys
    - os

### Input and Output

  - print()
    - f strings
  - files
    - with 
    - read()
    - readline()
    - write()

### Errors and Exceptions

  - Errors
  - Exceptions
    - try except
      ```py
      while True:
          try:
              x = int(input("Please enter a number: "))
              break
          except ValueError:
              print("Oops!  That was no valid number.  Try again...")
      ```
    - raise
      ```py
      import sys

      try:
          f = open('myfile.txt')
          s = f.readline()
          i = int(s.strip())
      except OSError as err:
          print("OS error: {0}".format(err))
      except ValueError:
          print("Could not convert data to an integer.")
      except:
          print("Unexpected error:", sys.exc_info()[0])
          raise
      ```

### Classes

```py
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

#### Objects

```py
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

#### init method

```py
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
```

#### Instance Objects

```py
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

#### Method Objects

### Inheritance

#### Multiple Inheritance

## Iterators

## Generators

## Standard Library

### Command Line Arguments

### RegEx

## Virutal Environments and Packages




### Decorators

## Resources

  - [Official Tutorial](https://docs.python.org/3/tutorial/)
  - Coding Style [PEP8](https://www.python.org/dev/peps/pep-0008)
  - [Python Setup and Usage](https://docs.python.org/3/using/index.html)


