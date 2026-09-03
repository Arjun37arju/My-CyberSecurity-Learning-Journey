##Understand Functions

## Contents

1. [Function Creation](#1-function-creation)
2. [Parameters](#2-parameters)
3. [Return Values](#3-return-values)
4. [Scope](#4-scope)
5. [Reusable Code](#5-reusable-code)

---

# 1. Function Creation

A **function** is a block of code that performs a specific task.

Instead of writing the same code again and again, we can put it inside a function and call it whenever needed.

### Creating a Function

A function is created using the `def` keyword.

```python
def greet():
    print("Hello!")
```

### Calling a Function

Creating a function does not execute it.

We need to **call** the function.

```python
def greet():
    print("Hello!")

greet()
```

Output:

```text
Hello!
```

### Function with Multiple Statements

```python
def introduce():
    print("My name is Arjun")
    print("I am learning Python")
    print("I like programming")

introduce()
```

### Basic Function Structure

```text
def function_name():
    # code
```

Example:

```python
def welcome():
    print("Welcome to Python")

welcome()
```

---

# 2. Parameters

A **parameter** is a variable inside the function definition that receives a value.

Parameters allow us to give data to a function.

### Function Without Parameter

```python
def greet():
    print("Hello Arjun")

greet()
```

This function always prints the same name.

### Function With a Parameter

```python
def greet(name):
    print("Hello", name)

greet("Arjun")
```

Output:

```text
Hello Arjun
```

Here:

* `name` → parameter
* `"Arjun"` → argument

### Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

Here:

```text
a = 10
b = 20
```

### Another Example

```python
def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce("Arjun", 22)
```

### Default Parameter

A parameter can have a default value.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Arjun")
```

Output:

```text
Hello User
Hello Arjun
```

---

# 3. Return Values

A function can **return a value** using the `return` statement.

### Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The function calculates:

```text
10 + 20 = 30
```

and sends `30` back to the caller.

### `print()` vs `return`

#### Using `print()`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

The function displays the result.

#### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The function sends the result back so we can store or use it.

### Return Multiple Values

Python can return multiple values.

```python
def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference

result1, result2 = calculate(20, 10)

print(result1)
print(result2)
```

Output:

```text
30
10
```

### Return Boolean Value

```python
def is_even(number):
    return number % 2 == 0

result = is_even(10)

print(result)
```

Output:

```text
True
```

---

# 4. Scope

**Scope** means where a variable can be accessed in a program.

The two important types of scope for beginners are:

* Local scope
* Global scope

---

## Local Scope

A variable created inside a function is a **local variable**.

It can normally be used only inside that function.

```python
def show_number():
    number = 10
    print(number)

show_number()
```

Here, `number` belongs to the function.

Trying to use it outside:

```python
def show_number():
    number = 10

show_number()

print(number)
```

This causes an error because `number` is local to the function.

---

## Global Scope

A variable created outside a function is a **global variable**.

```python
name = "Arjun"

def greet():
    print(name)

greet()
```

The function can access the global variable `name`.

### Local and Global with the Same Name

```python
name = "Arjun"

def show_name():
    name = "Rahul"
    print(name)

show_name()

print(name)
```

Output:

```text
Rahul
Arjun
```

The local variable does not change the global variable.

---

# 5. Reusable Code

One of the biggest advantages of functions is **code reuse**.

Instead of repeating the same code, create a function once and call it whenever needed.

### Without a Function

```python
print("Hello Arjun")
print("Hello Rahul")
print("Hello Vivek")
```

The same structure is repeated.

### With a Function

```python
def greet(name):
    print("Hello", name)

greet("Arjun")
greet("Rahul")
greet("Vivek")
```

Output:

```text
Hello Arjun
Hello Rahul
Hello Vivek
```

The function is written once but used multiple times.

---

# Practical Examples

## Example 1: Add Two Numbers

```python
def add(a, b):
    return a + b

result = add(10, 20)

print("Sum =", result)
```

Output:

```text
Sum = 30
```

---

## Example 2: Check Even or Odd

```python
def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_number(15)

print(result)
```

Output:

```text
Odd
```

---

## Example 3: Find Largest Number

```python
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

result = find_largest(25, 40)

print("Largest =", result)
```

Output:

```text
Largest = 40
```

---

## Example 4: Calculate Area

```python
def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)

print("Area =", area)
```

Output:

```text
Area = 50
```

---

## Example 5: User Input with Function

```python
def add_numbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)

print("Sum =", result)
```

---

# Function Flow

A simple function workflow looks like this:

```text
Create Function
      ↓
Define Parameters
      ↓
Write Function Logic
      ↓
Return Result
      ↓
Call Function
      ↓
Use Result
```

Example:

```python
def multiply(a, b):       # Create + parameters
    return a * b          # Logic + return

result = multiply(5, 4)   # Call function

print(result)             # Use result
```

Output:

```text
20
```

---

# Function vs Normal Code

### Repeated Code

```python
a = 10
b = 20
print(a + b)

a = 30
b = 40
print(a + b)
```

### Reusable Function

```python
def add(a, b):
    return a + b

print(add(10, 20))
print(add(30, 40))
```

The second approach is easier to reuse and maintain.

---

# Key Points

* `def` is used to create a function.
* A function runs when it is **called**.
* **Parameters** allow functions to receive data.
* **Arguments** are the actual values passed to parameters.
* `return` sends a value back from a function.
* **Local variables** belong to a function.
* **Global variables** are created outside functions.
* Functions help create **reusable code**.
* A good function should generally perform one clear task.

