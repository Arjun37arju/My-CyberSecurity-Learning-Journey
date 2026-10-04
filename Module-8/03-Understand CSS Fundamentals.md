# Understand CSS Fundamentals

## 📑 Content

 #  Topic                                               

 1 . Styling Concepts](#1-styling-concepts)             
 2 . [Layout Systems](#2-layout-systems)                 
 3 . [Responsive Design](#3-responsive-design)           
 4 . [UI Components](#4-ui-components)                   
 5 . [User Experience Basics](#5-user-experience-basics) 
 6 . [Summary](#summary)                                 

---

# 1. Styling Concepts

## What is CSS?

**CSS (Cascading Style Sheets)** is used to control the appearance and design of HTML elements.

HTML provides the **structure**, while CSS provides the **style**.

For example:

```html
<h1>Hello World</h1>
```

CSS can change its color:

```css
h1 {
    color: blue;
}
```

## CSS Syntax

```css
selector {
    property: value;
}
```

Example:

```css
h1 {
    color: blue;
    font-size: 30px;
}
```

* `h1` → selector
* `color` → property
* `blue` → value
* `font-size` → property
* `30px` → value

## Ways to Add CSS

### Inline CSS

CSS is written directly inside the HTML element.

```html
<h1 style="color: blue;">Hello</h1>
```

### Internal CSS

CSS is written inside the `<style>` tag.

```html
<head>
    <style>
        h1 {
            color: blue;
        }
    </style>
</head>
```

### External CSS

CSS is written in a separate `.css` file.

HTML:

```html
<link rel="stylesheet" href="style.css">
```

CSS:

```css
h1 {
    color: blue;
}
```

## Common CSS Properties

```css
color: blue;
background-color: lightgray;
font-size: 20px;
text-align: center;
width: 200px;
border: 1px solid black;
```

---

# 2. Layout Systems

CSS layout systems are used to arrange elements on a webpage.

The two important layout systems are:

* **Flexbox**
* **CSS Grid**

## Flexbox

Flexbox is mainly used to arrange elements in a **row or column**.

Example:

```html
<div class="container">
    <div class="box">Box 1</div>
    <div class="box">Box 2</div>
    <div class="box">Box 3</div>
</div>
```

CSS:

```css
.container {
    display: flex;
    justify-content: center;
    gap: 20px;
}
```

### `display: flex`

Enables Flexbox.

```css
display: flex;
```

### `justify-content`

Controls the arrangement of items along the main direction.

```css
justify-content: center;
```

Other common values:

```css
justify-content: space-between;
justify-content: space-around;
```

### `gap`

Creates space between items.

```css
gap: 20px;
```

## CSS Grid

CSS Grid is useful for arranging elements in **rows and columns**.

Example:

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}
```

This creates three equal columns.

```text
Box 1    Box 2    Box 3
Box 4    Box 5    Box 6
```

### What is `fr`?

`fr` means **fraction**.

It represents a portion of the available space.

```css
grid-template-columns: 1fr 1fr;
```

Creates two equal columns.

```css
grid-template-columns: 1fr 2fr;
```

The second column gets twice as much space as the first.

---

# 3. Responsive Design

## What is Responsive Design?

Responsive design means making a website adjust to different screen sizes.

A responsive website should work properly on:

* Desktop
* Tablet
* Mobile

## Media Query

A media query allows us to apply different CSS rules based on the screen size.

Syntax:

```css
@media (max-width: 600px) {
    /* CSS rules */
}
```

This means the CSS inside the media query applies when the screen width is **600px or smaller**.

## Example with Grid

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}

@media (max-width: 600px) {
    .container {
        grid-template-columns: 1fr;
    }
}
```

Desktop:

```text
Box 1    Box 2    Box 3
Box 4    Box 5    Box 6
```

Mobile:

```text
Box 1
Box 2
Box 3
Box 4
Box 5
Box 6
```

### Important

For Flexbox, we can use:

```css
flex-direction: column;
```

For Grid, we can use:

```css
grid-template-columns: 1fr;
```

---

# 4. UI Components

## What is UI?

**UI (User Interface)** is the part of a website that the user sees and interacts with.

Common UI components include:

* Buttons
* Cards
* Navigation bars
* Forms
* Search boxes

## Button

HTML:

```html
<button>Learn More</button>
```

CSS:

```css
button {
    background-color: blue;
    color: white;
    padding: 10px 20px;
    border: none;
}
```

### Important Properties

* `background-color` → changes the background
* `color` → changes the text color
* `padding` → creates space inside
* `border: none` → removes the border

## Card

A card is a container used to display related information.

HTML:

```html
<div class="card">
    <h2>Cybersecurity</h2>
    <p>I am learning cybersecurity.</p>
    <button>Learn More</button>
</div>
```

CSS:

```css
.card {
    width: 250px;
    padding: 20px;
    background-color: lightgray;
}
```

---

# 5. User Experience Basics

## What is User Experience?

**User Experience (UX)** means how easy and comfortable a website is for users to use.

A good website should be:

* Easy to understand
* Easy to navigate
* Easy to read
* Easy to use
* Mobile-friendly

## Readable Text

Use a suitable font size.

```css
p {
    font-size: 18px;
}
```

## Good Spacing

Spacing makes content easier to read.

```css
.card {
    padding: 20px;
    margin: 20px;
}
```

### Padding vs Margin

**Padding** → space inside the element.

```css
padding: 20px;
```

**Margin** → space outside the element.

```css
margin: 20px;
```

Example:

```text
        Margin
    ↓            ↓
+----------------------+
|       Padding        |
|    +----------+      |
|    |  Content |      |
|    +----------+      |
+----------------------+
```

## Easy-to-use Buttons

Buttons should have enough space to make them easy to click.

```css
button {
    padding: 10px 20px;
}
```

## Clear Colors

Text should have enough contrast with the background.

Good example:

```css
body {
    background-color: white;
    color: black;
}
```

## Mobile-Friendly Design

Use media queries to make the website work on smaller screens.

```css
@media (max-width: 600px) {
    .container {
        grid-template-columns: 1fr;
    }
}
```

---

# Summary

CSS is used to style and design HTML webpages.

### Topics Covered

| Topic             | What I Learned                                              |
| ----------------- | ----------------------------------------------------------- |
| Styling Concepts  | CSS syntax, properties, values, colors, fonts               |
| Layout Systems    | Flexbox and CSS Grid                                        |
| Responsive Design | Media queries and mobile layouts                            |
| UI Components     | Buttons and cards                                           |
| User Experience   | Readability, spacing, usability, and mobile-friendly design |

### Important CSS Concepts

```css
display: flex;
display: grid;
gap: 20px;
padding: 20px;
margin: 20px;
grid-template-columns: 1fr 1fr 1fr;
@media (max-width: 600px) {
    /* responsive CSS */
}
```

## CSS Fundamentals Completed ✅

I have completed the fundamentals of CSS including **styling, layouts, responsive design, UI components, and basic UX principles**.
