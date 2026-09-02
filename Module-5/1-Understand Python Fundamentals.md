## Understand Python Fundamentals

## Contents

1. [Variables and Data Types](#1-variables-and-data-types)
2. [Operators](#2-operators)
3. [Input and Output](#3-input-and-output)
4. [Type Conversion](#4-type-conversion)
5. [Python Coding Practices](#5-python-coding-practices)

---

## 1. Variables and Data Types

### What is a Variable?

A variable is a name used to store a value.

```python
name = "Arjun"
age = 22
```

Here:

* `name` stores `"Arjun"`
* `age` stores `22`

### Common Data Types

| Data Type | Example             |
| --------- | ------------------- |
| `int`     | `10`                |
| `float`   | `10.5`              |
| `str`     | `"Hello"`           |
| `bool`    | `True` / `False`    |
| `list`    | `[10, 20, 30]`      |
| `tuple`   | `(10, 20, 30)`      |
| `set`     | `{10, 20, 30}`      |
| `dict`    | `{"name": "Arjun"}` |

### Example

```python
name = "Arjun"
age = 22
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

### Checking Data Type

Use `type()` to check the type of a variable.

```python
age = 22

print(type(age))
```

Output:

```text
<class 'int'>
```

---

## 2. Operators

Operators are symbols used to perform operations on values.

### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a ** b)  # Power
print(a // b)  # Floor division
```

### Comparison Operators

Comparison operators return `True` or `False`.

```python
a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
```

### Assignment Operators

```python
a = 10

a += 5
print(a)

a -= 2
print(a)

a *= 2
print(a)
```

### Logical Operators

Python has three main logical operators:

* `and`
* `or`
* `not`

```python
age = 22

print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not(age > 18))
```

### Membership Operators

Used to check whether a value exists in a sequence.

```python
name = "Arjun"

print("A" in name)
print("z" not in name)
```

### Identity Operators

Used to check whether two variables refer to the same object.

```python
a = [1, 2, 3]
b = a

print(a is b)
```

---

## 3. Input and Output

### Taking Input

Use `input()` to take input from the user.

```python
name = input("Enter your name: ")

print("Hello", name)
```

Example:

```text
Enter your name: Arjun
Hello Arjun
```

> **Note:** `input()` always returns data as a string.

### Taking Number Input

```python
age = int(input("Enter your age: "))

print("Your age is", age)
```

### Using `print()`

The `print()` function displays output.

```python
name = "Arjun"
age = 22

print("Name:", name)
print("Age:", age)
```

### Using f-strings

f-strings are an easy way to insert variables into text.

```python
name = "Arjun"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

---

## 4. Type Conversion

Type conversion means changing one data type into another.

### String to Integer

```python
num = "10"

num = int(num)

print(num)
print(type(num))
```

### Integer to Float

```python
num = 10

num = float(num)

print(num)
```

### Integer to String

```python
num = 100

num = str(num)

print(num)
print(type(num))
```

### String to Float

```python
price = "99.5"

price = float(price)

print(price)
```

### Boolean Conversion

```python
a = 1
b = 0

print(bool(a))
print(bool(b))
```

Output:

```text
True
False
```

### Simple User Input Example

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)
```

---

## 5. Python Coding Practices

Good coding practices make programs easier to read, understand, debug, and maintain.

### 1. Use Meaningful Variable Names

Bad:

```python
x = 20
```

Good:

```python
age = 20
```

### 2. Use Proper Indentation

Python uses indentation to define blocks of code.

```python
age = 22

if age >= 18:
    print("Adult")
```

### 3. Use Comments

Comments explain the purpose of code.

```python
# Store the user's age
age = 22

print(age)
```

### 4. Keep Code Simple

Instead of writing unnecessary code:

```python
a = 10
b = 20
c = a + b

print(c)
```

Keep the code clear and simple.

### 5. Use Consistent Naming

Use `snake_case` for variable and function names.

```python
first_name = "Arjun"
student_age = 22
total_marks = 450
```

### 6. Avoid Unnecessary Code

Avoid repeating the same code unnecessarily.

```python
# Good
name = "Arjun"
print(name)
```

### 7. Test Your Code

Run your program with different inputs and check whether the output is correct.

Example:

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Test with:

```text
10
-5
0
```

---

# Practice Programs

## Program 1: Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

## Program 2: Check Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Program 3: Calculate Area of a Rectangle

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)
```

## Program 4: Swap Two Variables

```python
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)
```

## Program 5: Display Personal Information

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

---

## Key Points

* **Variables** store values.
* **Data types** define the type of value.
* **Operators** perform operations.
* **`input()`** takes user input.
* **`print()`** displays output.
* **Type conversion** changes one data type into another.
* **Good coding practices** make code readable and maintainable.
* Python uses **indentation** to define code blocks.

