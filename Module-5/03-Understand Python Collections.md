##Understand Python Collections

## Contents

1. [Lists](#1-lists)
2. [Tuples](#2-tuples)
3. [Sets](#3-sets)
4. [Dictionaries](#4-dictionaries)
5. [Collection Manipulation](#5-collection-manipulation)

---

# 1. Lists

A **list** is an ordered and changeable collection.

* Ordered
* Mutable (changeable)
* Allows duplicate values
* Allows different data types

### Creating a List

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange']
```

### Accessing Elements

List indexing starts from `0`.

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output:

```text
apple
banana
orange
```

### Changing an Element

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)
```

Output:

```text
['apple', 'mango', 'orange']
```

### Adding Elements

```python
fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange']
```

### Removing Elements

```python
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)
```

Output:

```text
['apple', 'orange']
```

### List Length

```python
fruits = ["apple", "banana", "orange"]

print(len(fruits))
```

Output:

```text
3
```

### Loop Through a List

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

---

# 2. Tuples

A **tuple** is an ordered and unchangeable collection.

* Ordered
* Immutable (cannot be changed)
* Allows duplicate values
* Allows different data types

### Creating a Tuple

```python
numbers = (10, 20, 30, 40)

print(numbers)
```

### Accessing Elements

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

### Tuple Cannot Be Changed

```python
numbers = (10, 20, 30)

# This will cause an error
numbers[0] = 50
```

Tuples are useful when the data should remain unchanged.

### Tuple Length

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

### Loop Through a Tuple

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

---

# 3. Sets

A **set** is an unordered collection that stores unique values.

* Unordered
* Mutable
* Does not allow duplicates
* Useful for set operations

### Creating a Set

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

### Duplicate Values

Duplicate values are automatically removed.

```python
numbers = {10, 20, 20, 30, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

### Adding an Element

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

### Removing an Element

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

### Loop Through a Set

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

> Sets do not support indexing like lists and tuples.

### Set Operations

#### Union

Combines elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

Output:

```text
{1, 2, 3, 4, 5}
```

#### Intersection

Returns common elements.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))
```

Output:

```text
{3}
```

#### Difference

Returns elements present in the first set but not the second.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))
```

Output:

```text
{1, 2}
```

---

# 4. Dictionaries

A **dictionary** stores data as **key-value pairs**.

```text
key → value
```

### Creating a Dictionary

```python
student = {
    "name": "Arjun",
    "age": 22,
    "course": "Python"
}

print(student)
```

### Accessing Values

```python
student = {
    "name": "Arjun",
    "age": 22
}

print(student["name"])
print(student["age"])
```

Output:

```text
Arjun
22
```

### Adding a New Key-Value Pair

```python
student = {
    "name": "Arjun",
    "age": 22
}

student["city"] = "Kodagu"

print(student)
```

### Updating a Value

```python
student = {
    "name": "Arjun",
    "age": 22
}

student["age"] = 23

print(student)
```

### Removing a Key-Value Pair

```python
student = {
    "name": "Arjun",
    "age": 22,
    "city": "Kodagu"
}

del student["city"]

print(student)
```

### Loop Through a Dictionary

#### Keys

```python
student = {
    "name": "Arjun",
    "age": 22
}

for key in student:
    print(key)
```

#### Values

```python
student = {
    "name": "Arjun",
    "age": 22
}

for value in student.values():
    print(value)
```

#### Keys and Values

```python
student = {
    "name": "Arjun",
    "age": 22
}

for key, value in student.items():
    print(key, ":", value)
```

---

# 5. Collection Manipulation

Collection manipulation means **adding, removing, updating, accessing, and processing data** inside collections.

---

## List Manipulation

### Add

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Insert

`insert()` adds an element at a specific position.

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

### Update

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

### Remove

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

### Sort

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30]
```

### Reverse

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

---

## Tuple Manipulation

Tuples cannot be directly changed because they are immutable.

You can access and process their values.

```python
numbers = (10, 20, 30, 40)

print(numbers[1])
print(len(numbers))
```

You can also create a new tuple:

```python
numbers = (10, 20, 30)

new_numbers = numbers + (40, 50)

print(new_numbers)
```

---

## Set Manipulation

### Add

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

### Update

Add multiple elements:

```python
numbers = {10, 20}

numbers.update({30, 40, 50})

print(numbers)
```

### Remove

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

### Union

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.union(b))
```

### Intersection

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

### Difference

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))
```

---

## Dictionary Manipulation

### Add

```python
student = {
    "name": "Arjun"
}

student["age"] = 22

print(student)
```

### Update

```python
student = {
    "name": "Arjun",
    "age": 22
}

student["age"] = 23

print(student)
```

### Remove

```python
student = {
    "name": "Arjun",
    "age": 22
}

del student["age"]

print(student)
```

### Check if a Key Exists

```python
student = {
    "name": "Arjun",
    "age": 22
}

if "name" in student:
    print("Name exists")
```

---

# Collection Comparison

| Collection | Ordered | Changeable | Duplicates | Syntax         |
| ---------- | ------- | ---------- | ---------- | -------------- |
| List       | Yes     | Yes        | Yes        | `[]`           |
| Tuple      | Yes     | No         | Yes        | `()`           |
| Set        | No      | Yes        | No         | `{}`           |
| Dictionary | Yes*    | Yes        | Keys: No   | `{key: value}` |

> `*` Dictionaries preserve insertion order in modern Python.

---

# Simple Example Using Multiple Collections

```python
student = {
    "name": "Arjun",
    "age": 22,
    "skills": ["Python", "Linux", "Git"]
}

print(student["name"])
print(student["age"])

for skill in student["skills"]:
    print(skill)
```

Output:

```text
Arjun
22
Python
Linux
Git
```

---

# Key Points

* **List** → ordered, changeable, allows duplicates.
* **Tuple** → ordered, unchangeable, allows duplicates.
* **Set** → unique values, unordered, useful for set operations.
* **Dictionary** → stores data using key-value pairs.
* **Collection manipulation** → accessing, adding, removing, updating, sorting, and processing collection data.
* Use **lists** when data needs to change.
* Use **tuples** when data should remain unchanged.
* Use **sets** when you need unique values or set operations.
* Use **dictionaries** when data needs to be stored with meaningful keys.

