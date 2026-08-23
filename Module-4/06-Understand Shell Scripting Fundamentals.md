#  Understand Shell Scripting Fundamentals

## Table of Contents

* [Introduction](#introduction)
* [a. Variables](#a-variables)
* [b. Conditional Statements](#b-conditional-statements)
* [c. Loops](#c-loops)
* [d. Functions](#d-functions)
* [e. Script Execution](#e-script-execution)


## Introduction

**Shell scripting** is the process of writing a series of commands in a file so that the shell can execute them automatically.

In Linux, common shells include:

* **Bash** — Bourne Again Shell
* Sh — Bourne Shell
* Zsh — Z Shell
* Fish — Friendly Interactive Shell

For cybersecurity and Linux administration, **Bash scripting** is especially useful for automating tasks such as:

* Log analysis
* System monitoring
* File operations
* User management
* Network checks
* Security automation
* Incident-response tasks

A Bash script normally starts with:

```bash
#!/bin/bash
```

This is called a **shebang**. It tells Linux to use Bash to execute the script.

---

# a. Variables

A **variable** is used to store information that can be reused inside a script.

### Creating a variable

```bash
name="Arix"
age=21
```

⚠️ There should be **no spaces** around `=`.

Correct:

```bash
name="Arix"
```

Incorrect:

```bash
name = "Arix"
```

### Accessing a variable

Use `$` before the variable name:

```bash
echo $name
echo $age
```

Output:

```text
Arix
21
```

### User input

The `read` command allows the script to receive input.

```bash
#!/bin/bash

echo "Enter your name:"
read name

echo "Hello $name"
```

### Command substitution

You can store the output of a command in a variable:

```bash
current_user=$(whoami)

echo "Current user: $current_user"
```

Another example:

```bash
ip=$(hostname -I)

echo "Your IP is $ip"
```

### Important special variables

| Variable | Meaning                         |
| -------- | ------------------------------- |
| `$0`     | Script name                     |
| `$1`     | First argument                  |
| `$2`     | Second argument                 |
| `$#`     | Number of arguments             |
| `$@`     | All arguments                   |
| `$?`     | Exit status of previous command |
| `$$`     | Current process ID              |

Example:

```bash
#!/bin/bash

echo "Script: $0"
echo "First argument: $1"
echo "Second argument: $2"
```

Run:

```bash
./test.sh hello world
```

Output:

```text
Script: ./test.sh
First argument: hello
Second argument: world
```

---

# b. Conditional Statements

Conditional statements allow a script to **make decisions**.

The main structure is:

```bash
if condition
then
    commands
fi
```

### Basic `if`

```bash
#!/bin/bash

age=20

if [ $age -ge 18 ]
then
    echo "Adult"
fi
```

### `if-else`

```bash
#!/bin/bash

age=16

if [ $age -ge 18 ]
then
    echo "Adult"
else
    echo "Minor"
fi
```

### `if-elif-else`

```bash
#!/bin/bash

marks=75

if [ $marks -ge 90 ]
then
    echo "Excellent"
elif [ $marks -ge 60 ]
then
    echo "Good"
else
    echo "Needs improvement"
fi
```

### Common comparison operators

#### Numbers

| Operator | Meaning               |
| -------- | --------------------- |
| `-eq`    | Equal                 |
| `-ne`    | Not equal             |
| `-gt`    | Greater than          |
| `-ge`    | Greater than or equal |
| `-lt`    | Less than             |
| `-le`    | Less than or equal    |

Example:

```bash
if [ $age -ge 18 ]
then
    echo "Allowed"
fi
```

### String comparisons

```bash
if [ "$user" = "root" ]
then
    echo "Root user"
fi
```

Common operators:

| Operator | Meaning             |
| -------- | ------------------- |
| `=`      | Equal               |
| `!=`     | Not equal           |
| `-z`     | String is empty     |
| `-n`     | String is not empty |

### File conditions

Shell scripting is heavily used for checking files.

```bash
if [ -f "/etc/passwd" ]
then
    echo "File exists"
fi
```

Useful file operators:

| Operator | Meaning               |
| -------- | --------------------- |
| `-f`     | Regular file exists   |
| `-d`     | Directory exists      |
| `-e`     | File/directory exists |
| `-r`     | Readable              |
| `-w`     | Writable              |
| `-x`     | Executable            |

Example:

```bash
if [ -d "/home" ]
then
    echo "Directory exists"
fi
```

---

# c. Loops

Loops allow you to **repeat commands automatically**.

The main Bash loops are:

1. `for`
2. `while`
3. `until`

## 1. For loop

Used when you want to iterate through a known set of values.

```bash
for i in 1 2 3 4 5
do
    echo $i
done
```

Output:

```text
1
2
3
4
5
```

### Using a range

```bash
for i in {1..5}
do
    echo "Number: $i"
done
```

### Loop through files

```bash
for file in *.txt
do
    echo "$file"
done
```

This is useful for automation and file analysis.

---

## 2. While loop

A `while` loop continues **as long as the condition is true**.

```bash
count=1

while [ $count -le 5 ]
do
    echo $count
    count=$((count + 1))
done
```

Output:

```text
1
2
3
4
5
```

### Practical example

```bash
count=1

while [ $count -le 3 ]
do
    echo "Checking system..."
    count=$((count + 1))
done
```

---

## 3. Until loop

An `until` loop continues until the condition becomes **true**.

```bash
count=1

until [ $count -gt 5 ]
do
    echo $count
    count=$((count + 1))
done
```

---

## `break` and `continue`

### `break`

Stops the loop completely.

```bash
for i in {1..10}
do
    if [ $i -eq 5 ]
    then
        break
    fi

    echo $i
done
```

Output:

```text
1
2
3
4
```

### `continue`

Skips the current iteration.

```bash
for i in {1..5}
do
    if [ $i -eq 3 ]
    then
        continue
    fi

    echo $i
done
```

Output:

```text
1
2
4
5
```

---

# d. Functions

A **function** is a reusable block of commands.

Instead of writing the same commands multiple times, put them inside a function.

### Creating a function

```bash
#!/bin/bash

hello() {
    echo "Hello from Bash"
}

hello
```

Output:

```text
Hello from Bash
```

### Function with arguments

```bash
#!/bin/bash

greet() {
    echo "Hello $1"
}

greet "Arix"
```

Output:

```text
Hello Arix
```

Here:

```text
$1
```

represents the first argument passed to the function.

### Function with multiple arguments

```bash
add() {
    result=$(( $1 + $2 ))
    echo $result
}

add 10 20
```

Output:

```text
30
```

### Returning a value

Bash functions can use `return` for an **exit status**.

```bash
check_file() {
    if [ -f "$1" ]
    then
        return 0
    else
        return 1
    fi
}

check_file "/etc/passwd"

if [ $? -eq 0 ]
then
    echo "File exists"
else
    echo "File not found"
fi
```

---

# e. Script Execution

After creating a Bash script, you need to know how to execute it.

Suppose we create:

```text
script.sh
```

### Step 1: Create the script

```bash
nano script.sh
```

Add:

```bash
#!/bin/bash

echo "Hello Linux"
```

Save the file.

### Step 2: Give execute permission

```bash
chmod +x script.sh
```

`chmod` changes file permissions.

`+x` means **add execute permission**.

Check permissions:

```bash
ls -l script.sh
```

You may see:

```text
-rwxr-xr-x
```

The `x` indicates executable permission.

### Step 3: Execute the script

Use:

```bash
./script.sh
```

Output:

```text
Hello Linux
```

---

## Other ways to execute a script

### Using Bash directly

You don't necessarily need execute permission:

```bash
bash script.sh
```

### Using the full path

```bash
/bin/bash script.sh
```

### Running with `sh`

```bash
sh script.sh
```

However, if the script specifically uses Bash features, prefer:

```bash
bash script.sh
```

because `sh` may point to another shell.

---

# Complete Example

Here is a small script combining **variables, conditions, loops, and functions**:

```bash
#!/bin/bash

name="Arix"

greet() {
    echo "Hello $1"
}

greet "$name"

for i in {1..5}
do
    if [ $i -eq 3 ]
    then
        echo "Found number 3"
    else
        echo "Number: $i"
    fi
done
```

Output:

```text
Hello Arix
Number: 1
Number: 2
Found number 3
Number: 4
Number: 5
```

---

# Cybersecurity Use of Shell Scripting

Shell scripting is very useful in cybersecurity because you can automate repetitive tasks.

For example:

### Check current user

```bash
whoami
```

### Check IP address

```bash
ip addr
```

### Check listening ports

```bash
ss -tuln
```

### Check running processes

```bash
ps aux
```

### Search logs

```bash
grep "failed" /var/log/auth.log
```

A Bash script can combine these commands and automatically perform security checks.

For example:

```bash
#!/bin/bash

echo "=== Security Check ==="

echo "Current User:"
whoami

echo
echo "IP Address:"
hostname -I

echo
echo "Listening Ports:"
ss -tuln

echo
echo "Running Processes:"
ps aux
```

This is where shell scripting becomes particularly useful for **Linux administration, SOC work, system monitoring, and security automation**.

# Quick Revision

| Topic            | Purpose                | Example              |
| ---------------- | ---------------------- | -------------------- |
| Variables        | Store data             | `name="Arix"`        |
| Conditions       | Make decisions         | `if [ ... ]`         |
| Loops            | Repeat commands        | `for`, `while`       |
| Functions        | Reuse commands         | `function_name()`    |
| Script execution | Run scripts            | `./script.sh`        |
| `chmod +x`       | Add execute permission | `chmod +x script.sh` |
| Shebang          | Specify interpreter    | `#!/bin/bash`        |

