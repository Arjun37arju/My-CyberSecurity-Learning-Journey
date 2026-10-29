# Understanding Exception Handling

## Contents

1. [Error Handling](#1-error-handling)
2. [Try-Except Blocks](#2-try-except-blocks)
3. [Debugging](#3-debugging)
4. [Logging Errors](#4-logging-errors)
5. [Building Reliable Scripts](#5-building-reliable-scripts)

---

# 1. Error Handling

**Error handling** is the way a program deals with problems safely. It prevents a small problem, such as invalid input or a missing file, from unexpectedly stopping the whole program.

## Types of Errors

### Syntax Error

A syntax error happens when Python cannot understand the code because its rules are not followed.

```python
print("Hello"
```

The closing `)` is missing.

### Runtime Error

A runtime error happens while correctly written code is running.

```python
result = 10 / 0
```

Output:

```text
ZeroDivisionError: division by zero
```

### Logical Error

A logical error does not crash the program, but it gives the wrong result.

```python
price = 500
discount = 10  # 10 percent

final_price = price - discount
print(final_price)
```

The output is `490`, but a 10% discount should give `450`.

```python
price = 500
discount = 10

discount_amount = price * discount / 100
final_price = price - discount_amount

print(final_price)
```

Output:

```text
450.0
```

An **exception** is an error Python raises while a program runs. Some common exceptions are:

```python
int("hello")          # ValueError
10 / 0                 # ZeroDivisionError
open("missing.txt")   # FileNotFoundError
```

---

# 2. Try-Except Blocks

A `try`-`except` block handles an expected exception so that the program can give a useful response instead of crashing.

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a valid whole number.")
```

If the user types `twenty`, `int()` cannot convert that text to a number. Python raises `ValueError`, and the `except` block runs.

## Handle Specific Errors

Catch the exact error you expect.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Avoid a bare `except:` because it can hide unexpected programming mistakes.

```python
# Avoid this
except:
    print("Something went wrong.")
```

## `else` and `finally`

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid number.")
else:
    print("Valid number:", number)
finally:
    print("Program finished.")
```

- `else` runs only when no exception occurs.
- `finally` always runs, whether an exception occurs or not.

---

# 3. Debugging

**Debugging** means finding the cause of a bug and correcting it.

When Python shows an error, read the error type and the line number. Then check the values being used on that line.

```python
items = ["pen", "book", "bag"]
print(items[3])
```

Output:

```text
IndexError: list index out of range
```

The valid indexes are `0`, `1`, and `2`. There is no item at index `3`.

```python
items = ["pen", "book", "bag"]
print(items[2])
```

## Inspecting Values

Use `print()` while learning or testing to inspect values and their types.

```python
price = 100
quantity = "2"

print(price)
print(quantity)
print(type(quantity))
```

Output:

```text
100
2
<class 'str'>
```

`quantity` is text (`str`), not a number (`int`). Debugging helps reveal mistakes like this.

---

# 4. Logging Errors

**Logging** records information about a program. Logs are useful because they can be saved to a file and checked later.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("File is nearly empty")
logging.error("Could not save data")
```

This creates an `app.log` file.

## Log Levels

- `DEBUG` — detailed information used while developing.
- `INFO` — normal events, such as a program starting.
- `WARNING` — something unusual happened, but the program can continue.
- `ERROR` — an action failed.
- `CRITICAL` — a serious failure.

## Logging an Exception

```python
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)

try:
    number = int("hello")
except ValueError:
    logging.exception("Could not convert input to a number")
    print("Invalid input. Please enter a number.")
```

`logging.exception()` records the full traceback, making the problem easier to investigate. Do not log passwords, API keys, or other private information.

---

# 5. Building Reliable Scripts

A **reliable script** handles expected problems, gives clear messages, and avoids damaging data.

## Validate Input

```python
age = input("Enter age: ")

if not age.isdigit():
    print("Age must be a whole number.")
else:
    age = int(age)
    print("Valid age:", age)
```

`isdigit()` checks whether the user entered only digits. Validation catches bad input before the program tries to use it.

## Handle Missing Files

```python
try:
    with open("data.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
```

The `with` statement closes the file automatically, even if something goes wrong.

## Use Small Functions

```python
def divide_numbers(a, b):
    if b == 0:
        return None
    return a / b
```

Small functions are easier to understand, reuse, test, and debug.

## Write Files Safely

```python
with open("report.txt", "w") as file:
    file.write("Completed successfully.")
```

`"w"` creates a file or replaces its existing contents. Use `"a"` when you want to add new text without replacing existing content.

## Complete Example: Safe Division with Logging

```python
import logging

logging.basicConfig(
    filename="newp.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Please enter valid whole numbers.")
    logging.exception("User entered an invalid number.")

except ZeroDivisionError:
    print("The second number cannot be zero.")
    logging.exception("User tried to divide by zero.")
```

This script:

1. Gets two numbers from the user.
2. Converts the input into integers.
3. Divides the first number by the second number.
4. Handles invalid number input.
5. Handles division by zero.
6. Saves technical error details in `newp.log`.

---

# Key Points

- Errors can be syntax errors, runtime errors, or logical errors.
- Exceptions are runtime problems that Python reports.
- Use `try` and `except` to handle expected exceptions.
- Catch specific exceptions such as `ValueError` and `ZeroDivisionError`.
- Debug by reading the error message, checking the line, and inspecting values.
- Use logging to save useful error details.
- Validate input, use small functions, and test bad cases to make scripts reliable.
