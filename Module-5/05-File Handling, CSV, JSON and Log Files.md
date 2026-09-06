## File Handling, CSV, JSON and Log Files

## Navigation

- [1. Reading Files](#1-reading-files)
- [2. Writing a CSV File](#2-writing-a-csv-file)
- [3. Reading CSV Using csv.reader()](#3-reading-csv-using-csvreader)
- [4. Reading CSV Using csv.DictReader()](#4-reading-csv-using-csvdictreader)
- [5. Writing JSON Data](#5-writing-json-data)
- [6. Edit a JSON File](#6-edit-a-json-file)
- [7. Print a Log File](#7-print-a-log-file)
- [8. Find Specific Events](#8-find-specific-events)
- [9. Count Failed Login Events](#9-count-failed-login-events)
- [10. Logging Levels](#10-logging-levels)
- [11. Create a Basic Log File](#11-create-a-basic-log-file)
- [12. Print the Log File](#12-print-the-log-file)
- [13. Print Specific Log Messages](#13-print-specific-log-messages)
- [14. Count Specific Log Messages](#14-count-specific-log-messages)
- [15. Extract IP Addresses](#15-extract-ip-addresses-from-a-log-file)
- [16. Print IP Addresses](#16-print-ip-addresses-line-by-line)
- [17. Print Unique IP Addresses](#17-print-unique-ip-addresses)

---

## 1. Reading Files

```python
file = open("info.txt", "r")

content = file.read()
print(content)

file.close()
```

### Using `with open()`

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

`with open()` automatically closes the file.

### `readlines()`

```python
with open("intro.txt", "r") as file:
    print(file.readlines())
```

- `read()` → 📖 Reads the whole file.
- `readline()` → 📄 Reads one line.
- `readlines()` → 📚 Reads all lines and puts them into a list.
- `with open()` → Automatically closes the file.

### File Modes

- `"r"` → Read
- `"w"` → Write / overwrite
- `"a"` → Add content to the end of a file

---

## 2. Writing a CSV File

```python
with open("log.csv", "w", encoding="utf-8") as file:
    file.writelines([
        "name,course,place\n",
        "arjun,cyber,kodagu\n",
        "jeevan,info,mandya\n",
        "vivek,hardware,vpt\n"
    ])
```

---

## 3. Reading CSV Using `csv.reader()`

```python
import csv

with open("log.csv", "r", encoding="utf-8", newline="") as file:
    cont = csv.reader(file)

    next(cont)  # Skips the header row

    for i in cont:
        print(i[0], i[1], i[2])
```

Example output:

```text
arjun cyber kodagu
jeevan info mandya
vivek hardware vpt
```

### Read Every Row

```python
import csv

with open("people.csv", "r", encoding="utf-8", newline="") as file:
    cont = csv.reader(file)

    for i in cont:
        print(i[0], i[1], i[2])
```

---

## 4. Reading CSV Using `csv.DictReader()`

```python
import csv

with open("arj.csv", "r", encoding="utf-8", newline="") as file:
    connt = csv.DictReader(file)

    for i in connt:
        print(i["name"], i["age"])
```

Example CSV file:

```csv
name,age
Arjun,22
Jeevan,23
```

---

# JSON

## 5. Writing JSON Data

```python
import json

data = {
    "name": "Asha",
    "age": 28,
    "city": "Delhi"
}

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
```

- `json.dump()` → Saves Python data into a JSON file.
- `indent=2` → Makes JSON easy to read.

---

## 6. Edit a JSON File

To edit JSON, always follow this order:

```text
Read → Change → Save
```

```python
import json

# 1. Read
with open("test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. Change
data["name"] = "Ravi"
data["age"] = 30
data["is_student"] = True  # Add a new item
del data["city"]  # Delete an item

# 3. Save
with open("test.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# Print data
print(data["name"])
print(data["age"])
```

---

# Log File Handling

## 7. Print a Log File

```python
with open("practice.log", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

## 8. Find Specific Events

```python
with open("practice.log", "r", encoding="utf-8") as file:
    for line in file:
        if "failed login" in line.lower():
            print(line.strip())
```

Using `line.lower()` makes the search case-insensitive.

---

## 9. Count Failed Login Events

```python
count = 0

with open("practice.log", "r", encoding="utf-8") as file:
    for line in file:
        if "failed login" in line.lower():
            count += 1

print("Failed logins:", count)
```

---

# Python Logging

## 10. Logging Levels

```python
logging.debug("Checking variable value")    # Detailed developer information
logging.info("Program started")             # Normal activity
logging.warning("Storage is nearly full")   # Possible problem
logging.error("Could not open file")        # Something failed
logging.critical("Application stopped")     # Serious failure
```

```text
DEBUG → INFO → WARNING → ERROR → CRITICAL
```

If you set the level to `INFO`, Python shows:

```text
INFO, WARNING, ERROR, and CRITICAL
```

It does not show `DEBUG`.

---

## 11. Create a Basic Log File

```python
import logging

logging.basicConfig(
    filename="new4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Logging information")
logging.error("Error details")
logging.warning("Warning information")
```

---

## 12. Print the Log File

```python
with open("new4.log", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

## 13. Print Specific Log Messages

```python
with open("new4.log", "r", encoding="utf-8") as file:
    for line in file:
        if "login" in line.lower():
            print(line.strip())
```

## 14. Count Specific Log Messages

```python
count = 0

with open("new4.log", "r", encoding="utf-8") as file:
    for line in file:
        if "login" in line.lower():
            count += 1

print(count)
```

---

## 15. Extract IP Addresses from a Log File

```python
import re

with open("new4.log", "r", encoding="utf-8") as file:
    text = file.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)

print(ips)
```

## 16. Print IP Addresses Line by Line

```python
import re

with open("new4.log", "r", encoding="utf-8") as file:
    text = file.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)

for ip in ips:
    print(ip)
```

## 17. Print Unique IP Addresses

```python
import re

with open("new4.log", "r", encoding="utf-8") as file:
    text = file.read()

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)

unique_ips = set(ips)

for ip in unique_ips:
    print(ip)
```

---

## Final Note

> **Understand the code — do not just memorize it.**
>
> Try changing filenames, values, CSV columns, JSON keys, and log messages. Run the code and observe what changes. When you understand *why* each line is used, you can write similar programs confidently without memorizing every example.
