## Understand Program Flow

## Contents

1. [Conditional Statements](#1-conditional-statements)
2. [Loops](#2-loops)
3. [Nested Conditions](#3-nested-conditions)
4. [Control Statements](#4-control-statements)
5. [Problem-Solving Workflows](#5-problem-solving-workflows)

---

## 1. Conditional Statements

Conditional statements are used to make decisions in a program.

Python mainly uses:

* `if`
* `elif`
* `else`

### `if` Statement

The `if` statement executes code when a condition is `True`.

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### `if-else`

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### `if-elif-else`

Used when there are multiple conditions.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

### Example: Positive, Negative, or Zero

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## 2. Loops

Loops are used to execute a block of code repeatedly.

Python has two main loops:

* `for` loop
* `while` loop

### `for` Loop

A `for` loop is commonly used when you know how many times you want to repeat something.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### `range()`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### Loop Through a String

```python
name = "Python"

for letter in name:
    print(letter)
```

### `while` Loop

A `while` loop runs as long as the condition is `True`.

```python
a = 1

while a <= 5:
    print(a)
    a = a + 1
```

Output:

```text
1
2
3
4
5
```

### Example: Print Even Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

Output:

```text
2
4
6
8
10
```

---

## 3. Nested Conditions

A nested condition means placing one `if` statement inside another `if` statement.

### Simple Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")
```

### Example: Login System

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")
```

### Nested Conditions with Marks

```python
marks = 75

if marks >= 40:
    if marks >= 60:
        print("Pass with good marks")
    else:
        print("Pass")
else:
    print("Fail")
```

> Avoid unnecessary nesting when a simpler condition can solve the problem.

---

## 4. Control Statements

Control statements change the normal flow of loops.

The main control statements are:

* `break`
* `continue`
* `pass`

---

### `break`

`break` stops the loop completely.

```python
for i in range(1, 11):
    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, the loop stops.

---

### `continue`

`continue` skips the current iteration and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Here, `3` is skipped.

---

### `pass`

`pass` does nothing.

It is used when you need a statement syntactically but don't want to write the code yet.

```python
age = 20

if age >= 18:
    pass
else:
    print("Not eligible")
```

Another example:

```python
def login():
    pass
```

The function can be completed later.

---

### `break` vs `continue` vs `pass`

| Statement  | Purpose                 |
| ---------- | ----------------------- |
| `break`    | Stops the loop          |
| `continue` | Skips current iteration |
| `pass`     | Does nothing            |

---

## 5. Problem-Solving Workflows

Problem-solving workflow means following a logical process to solve a programming problem.

### Basic Workflow

```text
Understand the Problem
        ↓
Identify Inputs
        ↓
Identify Outputs
        ↓
Break Problem into Steps
        ↓
Write Logic
        ↓
Write Code
        ↓
Test the Code
        ↓
Debug Errors
        ↓
Final Solution
```

### Example Problem

**Problem:** Check whether a person is eligible to vote.

### Step 1: Understand the Problem

A person can vote if their age is `18` or above.

### Step 2: Identify Input

```text
Age
```

### Step 3: Identify Output

```text
Eligible
or
Not eligible
```

### Step 4: Write the Logic

```text
If age >= 18
    Print "Eligible"
Otherwise
    Print "Not eligible"
```

### Step 5: Write the Code

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### Step 6: Test

Input:

```text
20
```

Output:

```text
Eligible to vote
```

Input:

```text
15
```

Output:

```text
Not eligible to vote
```

---

# Practice Programs

## Program 1: Find the Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)
```

---

## Program 2: Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Program 3: Sum of Numbers from 1 to 10

```python
total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)
```

Output:

```text
Sum = 55
```

---

## Program 4: Stop When Number is 5

```python
for i in range(1, 11):
    if i == 5:
        break

    print(i)
```

---

## Program 5: Skip Number 5

```python
for i in range(1, 11):
    if i == 5:
        continue

    print(i)
```

---

## Program 6: Simple Login

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
```

---

# Key Points

* **Conditional statements** are used for decision-making.
* **`if`** checks a condition.
* **`elif`** checks another condition.
* **`else`** executes when previous conditions are false.
* **Loops** repeat code.
* **`for`** is commonly used for iterating over sequences or a known range.
* **`while`** repeats while a condition is true.
* **Nested conditions** put one condition inside another.
* **`break`** stops a loop.
* **`continue`** skips one iteration.
* **`pass`** does nothing and acts as a placeholder.
* **Problem-solving workflow** helps you solve programming problems step by step.

