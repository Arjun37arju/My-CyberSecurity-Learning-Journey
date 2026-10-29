# Understand HTML Fundamentals

## 📑 Content

| # | Topic                                         |
| - | --------------------------------------------- |
| 1 | [HTML Structure](#1-html-structure)           |
| 2 | [Forms](#2-forms)                             |
| 3 | [User Inputs](#3-user-inputs)                 |
| 4 | [Document Structure](#4-document-structure)   |
| 5 | [Web Page Components](#5-web-page-components) |

---

# 1. HTML Structure

HTML (**HyperText Markup Language**) is used to create the structure of a webpage.

### Basic HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>

<body>

    <h1>Hello World</h1>
    <p>This is my first webpage.</p>

</body>
</html>
```

### Important Elements

| Element           | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| `<!DOCTYPE html>` | Tells the browser that the document uses HTML5 |
| `<html>`          | Root element of the webpage                    |
| `<head>`          | Contains page information and metadata         |
| `<title>`         | Sets the browser tab title                     |
| `<body>`          | Contains visible webpage content               |
| `<h1>`            | Main heading                                   |
| `<p>`             | Paragraph                                      |

---

# 2. Forms

An HTML form is used to collect information from users.

For example:

* Username
* Email
* Password
* Registration details
* Login information

### Basic Form

```html
<form>

    <label>Username:</label>
    <input type="text">

    <br><br>

    <label>Password:</label>
    <input type="password">

    <br><br>

    <button type="submit">Login</button>

</form>
```

### Important Elements

| Element         | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `<form>`        | Groups form controls and handles form submission |
| `<label>`       | Describes an input                               |
| `<input>`       | Creates an input field                           |
| `<button>`      | Creates a clickable button                       |
| `type="submit"` | Makes the button submit the form                 |

### Cybersecurity Connection

Forms collect **user-controlled data**. Applications must properly validate and handle this data.

Poor input handling can contribute to vulnerabilities such as:

* Cross-Site Scripting (XSS)
* Injection
* Other input-validation problems

---

# 3. User Inputs

User inputs allow users to enter or select information.

The main element used is:

```html
<input>
```

### Common Input Types

#### Text

```html
<input type="text">
```

Used for normal text.

#### Password

```html
<input type="password">
```

Used for passwords. Characters are visually hidden while typing.

#### Email

```html
<input type="email">
```

Used for email addresses.

#### Number

```html
<input type="number">
```

Used for numbers.

#### Checkbox

```html
<input type="checkbox">
```

Used when an option can be selected or deselected.

Example:

```html
<input type="checkbox">
<label>I agree to the terms</label>
```

#### Radio Button

```html
<input type="radio" name="gender">
<label>Male</label>

<input type="radio" name="gender">
<label>Female</label>
```

Using the same `name` groups the radio buttons together, allowing the user to select one option from the group.

### Placeholder

```html
<input type="password" placeholder="Enter password">
```

`placeholder` displays a temporary hint inside the input field.

### Example

```html
<form>

    <label>Username:</label>
    <input type="text">

    <br><br>

    <label>Email:</label>
    <input type="email">

    <br><br>

    <label>Password:</label>
    <input type="password" placeholder="Enter password">

    <br><br>

    <label>Gender:</label>
    <br>

    <input type="radio" name="gender">
    <label>Male</label>

    <input type="radio" name="gender">
    <label>Female</label>

    <br><br>

    <input type="checkbox">
    <label>I agree</label>

    <br><br>

    <button type="submit">Submit</button>

</form>
```

---

# 4. Document Structure

Document structure means organizing webpage content into meaningful sections.

A common structure is:

```text
Web Page
│
├── Header
├── Navigation
├── Main Content
│   ├── Section
│   └── Article
└── Footer
```

### `<header>`

Contains introductory or top-level content.

```html
<header>
    <h1>My Website</h1>
</header>
```

### `<nav>`

Contains navigation links.

```html
<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
</nav>
```

### `<main>`

Contains the main content of the webpage.

```html
<main>
    <h2>About Me</h2>
    <p>I am learning cybersecurity.</p>
</main>
```

### `<section>`

Divides content into meaningful sections.

```html
<section>
    <h2>My Skills</h2>
    <p>HTML, Linux and Networking</p>
</section>
```

### `<article>`

Represents an independent piece of content, such as a blog post.

```html
<article>
    <h2>What is Cybersecurity?</h2>
    <p>Cybersecurity protects systems and data.</p>
</article>
```

### `<footer>`

Contains bottom-level information.

```html
<footer>
    <p>My Website</p>
</footer>
```

---

# 5. Web Page Components

Web pages are built using different components.

Common components include:

* Headings
* Paragraphs
* Links
* Images
* Lists
* Tables
* Buttons
* Forms

## Headings

```html
<h1>Main Heading</h1>
<h2>Section Heading</h2>
<h3>Subheading</h3>
```

HTML provides headings from `<h1>` to `<h6>`.

---

## Paragraphs

```html
<p>This is a paragraph.</p>
```

Used for normal text.

---

## Links

```html
<a href="https://example.com">Visit Website</a>
```

`<a>` creates a hyperlink.

`href` specifies the destination.

---

## Images

```html
<img src="image.jpg" alt="Example image">
```

| Attribute | Purpose                                        |
| --------- | ---------------------------------------------- |
| `src`     | Specifies the image location                   |
| `alt`     | Provides alternative text describing the image |

---

## Unordered Lists

```html
<ul>
    <li>HTML</li>
    <li>Linux</li>
    <li>Networking</li>
</ul>
```

Creates a bullet-point list.

---

## Ordered Lists

```html
<ol>
    <li>Learn HTML</li>
    <li>Learn CSS</li>
    <li>Learn JavaScript</li>
</ol>
```

Creates a numbered list.

---

## Tables

Tables display information in rows and columns.

```html
<table>

    <tr>
        <th>Topic</th>
        <th>Status</th>
    </tr>

    <tr>
        <td>HTML</td>
        <td>Completed</td>
    </tr>

    <tr>
        <td>Linux</td>
        <td>Learning</td>
    </tr>

</table>
```

### Table Elements

| Element   | Purpose                |
| --------- | ---------------------- |
| `<table>` | Creates the table      |
| `<tr>`    | Creates a table row    |
| `<th>`    | Creates a heading cell |
| `<td>`    | Creates a data cell    |

---

## Buttons

```html
<button type="button">Click Me</button>
```

Creates a clickable button.

For submitting a form:

```html
<button type="submit">Submit</button>
```

---

# Complete HTML Example

```html
<!DOCTYPE html>
<html>

<head>
    <title>My Cybersecurity Website</title>
</head>

<body>

    <header>
        <h1>Arjun's Cybersecurity Website</h1>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>

    <main>

        <section>
            <h2>About Me</h2>

            <p>
                I am learning HTML and cybersecurity fundamentals.
            </p>

            <img src="cybersecurity.jpg"
                 alt="Cybersecurity image"
                 width="200">
        </section>

        <section>
            <h2>My Skills</h2>

            <ul>
                <li>HTML</li>
                <li>Linux</li>
                <li>Networking</li>
            </ul>
        </section>

        <section>
            <h2>Learning Progress</h2>

            <table>

                <tr>
                    <th>Topic</th>
                    <th>Status</th>
                </tr>

                <tr>
                    <td>HTML</td>
                    <td>Completed</td>
                </tr>

                <tr>
                    <td>Linux</td>
                    <td>Learning</td>
                </tr>

                <tr>
                    <td>Networking</td>
                    <td>Learning</td>
                </tr>

            </table>
        </section>

        <button type="button">Contact Me</button>

    </main>

    <footer>
        <p>My Cybersecurity Learning Journey</p>
    </footer>

</body>

</html>
```

# Summary

You have learned the basic HTML foundation:

```text
HTML Structure
      ↓
Forms
      ↓
User Inputs
      ↓
Document Structure
      ↓
Web Page Components
```

These fundamentals are important before moving into **CSS, JavaScript, and web security**.
