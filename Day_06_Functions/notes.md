# Python Functions Notes

## Goal

Understand how to define, call, and return values from functions in Python, including handling parameters, default arguments, keyword arguments, and variable scope.

### What is a Function?

A function is a reusable block of code designed to perform a specific task.

### Syntax

```

def function_name(parameters):
\# code block
return value \# optional

```

## Why Use Functions?

- Avoid code repetition.
- Make code modular and readable.
- Test and debug small parts easily.

## Example: Basic Function

```

def greet(name):
print(f"Hello, {name}!")

greet("Thejas")

```

## Parameters and Arguments

- **Parameters**: Variables inside parentheses in a function definition.
- **Arguments**: Actual values passed when calling the function.

## Return Statement

Functions can return values using the `return` statement.

```

def add(a, b):
return a + b

result = add(5, 3)
print(result) \# Output: 8

```

## Default Arguments

Functions can provide default values for parameters.

```

def greet(name="Guest"):
print(f"Welcome, {name}!")

greet() \# Uses default value

```

## Keyword Arguments

Arguments can be specified by parameter names for clarity.

```

def intro(name, age):
print(f"Name: {name}, Age: {age}")

intro(age=23, name="Thejas")

```

## Variable Scope

- **Local Variable**: Defined inside a function and accessible only there.
- **Global Variable**: Defined outside functions and accessible everywhere in the file.

### Example

```

x = 10 \# global variable

def show():
y = 5 \# local variable
print(x + y)

show()
```
