# Apply Through Hands-on Tasks

## Contents

* [Introduction](#introduction)
* [Project Goal](#project-goal)
* [1. Build a Simple Web Application](#1-build-a-simple-web-application)
* [2. Implement Authentication Workflows](#2-implement-authentication-workflows)
* [3. Analyze Application Logs](#3-analyze-application-logs)
* [4. Identify Security Weaknesses](#4-identify-security-weaknesses)
* [5. Create a Secure Development Report](#5-create-a-secure-development-report)
* [Conclusion](#conclusion)

---

## Introduction

In this hands-on task, you will build a small web application and use it to practice basic web development and security concepts.

The goal is not to create a production-level application.

The goal is to **build something simple, understand how it works, and identify security weaknesses yourself.**

---

## Project Goal

You will create a simple **User Portal** with:

* Home page
* Registration page
* Login page
* Dashboard
* Logout
* Basic session-based authentication

You will then analyze the application logs and identify security weaknesses.

### Technologies

* HTML
* Python
* Flask

---

# 1. Build a Simple Web Application

First, create a simple web application.

### Step 1: Create the project

Create a project folder.

Inside the project, create:

```text
project/
├── app.py
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    └── dashboard.html
```

### Step 2: Create the Home Page

Create `index.html`.

Add:

* A welcome heading
* A short description
* A Login option
* A Register option

Make sure the Login and Register options can navigate to their respective pages.

### Step 3: Create the Login Page

Create `login.html`.

Add:

* Username field
* Password field
* Login button
* Link to Register

### Step 4: Create the Register Page

Create `register.html`.

Add:

* Username field
* Email field
* Password field
* Confirm password field
* Register button
* Link to Login

### Step 5: Create the Dashboard

Create `dashboard.html`.

Add:

* Dashboard heading
* Welcome message
* Logout button

### Step 6: Run the Application

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open the Flask address in your browser.

Test the navigation between the pages.

---

# 2. Implement Authentication Workflows

Now make the Login process work using Flask.

### Step 1: Create a Login Route

Create a Flask route for `/login`.

The route should:

1. Display the login page.
2. Receive the username and password.
3. Check the credentials.
4. Allow the user to access the dashboard if the credentials are correct.

For this learning project, you can use a simple fixed username and password.

Example:

```text
Username: admin
Password: 1234
```

> This is only for demonstrating the authentication workflow.

### Step 2: Add Sessions

Use Flask sessions to remember that the user has logged in.

The basic workflow should be:

```text
User enters credentials
        ↓
Server checks credentials
        ↓
Correct credentials
        ↓
Session created
        ↓
Dashboard allowed
```

### Step 3: Protect the Dashboard

The dashboard should check whether a login session exists.

If there is no session:

```text
User → Dashboard
        ↓
No session
        ↓
Redirect to Login
```

If the session exists:

```text
User → Dashboard
        ↓
Session exists
        ↓
Allow access
```

### Step 4: Implement Logout

Create a logout route.

When the user logs out:

* Clear the session.
* Redirect the user to the home page.

Test the complete workflow:

```text
Home
 ↓
Login
 ↓
Correct credentials
 ↓
Dashboard
 ↓
Logout
 ↓
Home
```

---

# 3. Analyze Application Logs

Now observe what happens when users interact with your application.

Start Flask:

```bash
python app.py
```

Look at the terminal while using the application.

You should see logs similar to:

```text
127.0.0.1 - - "GET / HTTP/1.1" 200 -
127.0.0.1 - - "GET /login HTTP/1.1" 200 -
127.0.0.1 - - "POST /login HTTP/1.1" 302 -
127.0.0.1 - - "GET /dashboard HTTP/1.1" 200 -
```

### Analyze the Logs

Look at:

* Requested URL
* HTTP method
* Status code
* Successful requests
* Redirects
* Failed requests

### Understand Status Codes

```text
200 → Successful request
302 → Redirect
404 → Page not found
```

Try different actions in your application and observe how the logs change.

---

# 4. Identify Security Weaknesses

Now inspect your application from a security perspective.

Don't immediately try to fix everything.

First, **identify the weaknesses.**

### Check 1: Password Exposure

Look at the registration request.

If the password appears in the URL, ask:

> Is it safe to send sensitive information through the URL?

Identify this as a security weakness.

### Check 2: Hard-Coded Credentials

Look at your login code.

If the username and password are directly written in the Python code, ask:

> Would this be safe in a real application?

Identify this as a weakness.

### Check 3: Input Validation

Try entering:

* Empty username
* Short password
* Different password confirmation
* Unexpected input

Ask:

> Does the application properly validate the input?

Identify missing validation as a weakness.

### Check 4: Session Security

Look at how the Flask session is configured.

Ask:

> Is the session secret strong enough for a real application?

Identify any weak configuration.

### Record Your Findings

Create a simple list:

```text
1. Password exposed in URL
2. Hard-coded credentials
3. Missing input validation
4. Weak session configuration
```

---

# 5. Create a Secure Development Report

Finally, create a short report about your project.

Your report should contain:

## Project Overview

Explain what you built.

## Technologies Used

Mention:

* HTML
* Python
* Flask

## Authentication

Explain:

* Login
* Session creation
* Dashboard protection
* Logout

## Log Analysis

Explain what you observed in the Flask logs.

## Security Weaknesses

List the weaknesses you identified.

Example:

```text
- Password exposed through URL
- Hard-coded credentials
- Missing input validation
- Weak session configuration
```

## Recommendations

Explain how these weaknesses could be improved in a real application.

For example:

```text
- Use POST for sensitive form data.
- Store user information securely.
- Validate user input.
- Use a strong secret key.
- Use secure password storage.
```

---

# Conclusion

By completing this project, you practiced five important hands-on activities:

```text
1. Build a simple web application
2. Implement authentication workflows
3. Analyze application logs
4. Identify security weaknesses
5. Create a secure development report
```


The purpose of this project is not to build a perfect production application.

The purpose is to **build, test, observe, and identify security issues yourself.**

Use this project as a starting point and try changing different parts of the application to understand how web applications and their security work.


## References

* [View User-Portal Project](../resources/User-Portal/)
* [View Hands-on Tasks Report](../resources/hands-on-report/Hands-on-Tasks-Report.pdf)
