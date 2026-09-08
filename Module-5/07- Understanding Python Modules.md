## Understanding Python Modules

## Contents

1. [Importing Modules](#1-importing-modules)
2. [Creating Modules](#2-creating-modules)
3. [Package Management](#3-package-management)
4. [Virtual Environments](#4-virtual-environments)
5. [Reusable Security Tools](#5-reusable-security-tools)

---

# 1. Importing Modules

A **module** is a Python file that contains useful code, such as functions, variables, or classes.

Python has built-in modules that can be imported and used directly.

## Basic Import

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

Here:

- `import math` makes the `math` module available.
- `math.sqrt(25)` finds the square root of `25`.

## Import a Specific Function

```python
from math import sqrt

print(sqrt(25))
```

This imports only the `sqrt` function.

## Import with an Alias

```python
import math as m

print(m.sqrt(25))
```

Here, `m` is a shorter name for `math`.

## Another Built-in Module

```python
import random

number = random.randint(1, 10)

print(number)
```

`random.randint(1, 10)` gives a random whole number from `1` to `10`.

## Avoid Importing Everything

Avoid this:

```python
from math import *
```

It can create name conflicts when two modules use the same function name.

Better:

```python
import math

print(math.sqrt(25))
```

---

# 2. Creating Modules

You can create your own module by writing code in a separate Python file.

Create a file named `calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Now create another file named `main.py` in the same folder:

```python
import calculator

result = calculator.add(10, 20)

print(result)
```

Output:

```text
30
```

Python uses the file name as the module name:

```text
calculator.py → calculator
```

Do not include `.py` when importing:

```python
import calculator       # Correct
import calculator.py    # Wrong
```

## Import One Function

```python
from calculator import add

print(add(10, 20))
```

Example project structure:

```text
my_project/
├── calculator.py
└── main.py
```

---

# 3. Package Management

A **package** is reusable code made by other developers that you can install and use in your project.

For example, `requests` is a package used to communicate with websites and APIs.

## What Is `pip`?

`pip` is Python’s package installer.

Use `pip` commands in the terminal, not inside a Python file.

## Install a Package

```bash
python -m pip install requests
```

After installing it, use it in Python:

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

Common status codes:

```text
200 → Success
404 → Page not found
500 → Server error
```

## List Installed Packages

```bash
python -m pip list
```

## Show Details About a Package

```bash
python -m pip show requests
```

## Install a Specific Version

```bash
python -m pip install requests==2.32.3
```

## Uninstall a Package

```bash
python -m pip uninstall requests
```

---

# 4. Virtual Environments

A **virtual environment** gives each Python project its own separate packages.

This prevents one project’s packages from affecting another project.

```text
Project A
└── venv → Flask 2.0

Project B
└── venv → Flask 3.0
```

## Create a Virtual Environment on Linux

Open the terminal inside your project folder and run:

```bash
python3 -m venv venv
```

This creates a `venv` folder.

```text
my_project/
├── venv/
└── main.py
```

## Activate the Virtual Environment

Run this from the project folder:

```bash
source venv/bin/activate
```

Your terminal should show:

```text
(venv)
```

This means the virtual environment is active.

## Install a Package Inside the Environment

```bash
python -m pip install requests
```

The package is installed only for this project.

## Create `requirements.txt`

```bash
python -m pip freeze > requirements.txt
```

This saves package names and versions in a file called `requirements.txt`.

Example:

```text
requests==2.32.3
```

## Install Packages from `requirements.txt`

Use this when someone else downloads your project, or when you create a new virtual environment:

```bash
python -m pip install -r requirements.txt
```

## Deactivate the Virtual Environment

```bash
deactivate
```

## `.gitignore`

Do not upload the `venv` folder to GitHub. Add this to `.gitignore`:

```text
venv/
```

---

# 5. Reusable Security Tools

Reusable security tools are small functions kept in a separate module so they can be used in many projects.

Example file:

```text
security_tools.py
```

## Generate a Secure Token

```python
import secrets

def generate_token():
    return secrets.token_hex(16)
```

Use it in `main.py`:

```python
import security_tools

token = security_tools.generate_token()

print(token)
```

`secrets` creates random values that are difficult to predict. Use it for tokens, password-reset codes, and other security-related values.

## Generate a Secure Password

In `security_tools.py`:

```python
import secrets
import string

def generate_password():
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(char) for _ in range(12))
    return password
```

In `main.py`:

```python
import security_tools

password = security_tools.generate_password()

print(password)
```

This creates a random password with 12 characters.

## Do Not Store Passwords Directly

```text
Wrong:  password = mypassword123
Better: store a password hash
```

For now, remember:

```text
generate_password() → creates a new password
hash_password(password) → hides an existing password before storing it
```

## Keep Secrets Out of Code

Do not write API keys or passwords directly in Python files.

Wrong:

```python
api_key = "my-secret-key"
```

Better:

```python
import os

api_key = os.getenv("API_KEY")
```

Add secret files to `.gitignore`:

```text
.env
venv/
```

---

# Key Points

- A module is a Python file containing reusable code.
- Use `import` to use built-in modules or your own modules.
- Use `pip` in the terminal to install packages.
- Use a virtual environment for each Python project.
- Use `requirements.txt` to list a project’s required packages.
- Do not upload `venv/` or secret files to GitHub.
- Use `secrets` for security-related random values.
- Put reusable security functions in a module such as `security_tools.py`.
