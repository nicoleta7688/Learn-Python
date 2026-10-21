# Python OOP Practice Projects

## Overview

This folder contains four Python practice projects focused on the main principles of Object-Oriented Programming.

The goal is to practice OOP step by step by building small, testable projects with clear requirements.

Each project focuses mainly on one OOP principle:

1. **Encapsulation** — Bank Account Manager
2. **Abstraction** — Shape Calculator
3. **Inheritance** — Employee Payroll System
4. **Polymorphism** — Notification System

Each project has its own README file with detailed requirements and test cases.

---

## Recommended Project Order

Complete the projects in this order:

```text
1. bank-account-manager
2. shape-calculator
3. employee-payroll-system
4. notification-system
```

Do not skip directly to the harder projects.

Each project builds on ideas from the previous one.

---

## Suggested Folder Structure

Your folder should look like this:

```text
oop-practice/
│
├── README.md
│
├── bank-account-manager/
│   ├── README.md
│   └── main.py
│
├── shape-calculator/
│   ├── README.md
│   └── main.py
│
├── employee-payroll-system/
│   ├── README.md
│   └── main.py
│
└── notification-system/
    ├── README.md
    └── main.py
```

You may use a different file name instead of `main.py`, but each project should have its own separate Python file.

---

## Main Learning Goals

By completing these projects, you should understand how to:

- Create classes
- Create objects from classes
- Store data inside objects
- Use instance attributes
- Use methods
- Validate data inside classes
- Protect internal object state
- Use properties
- Reuse common behavior through inheritance
- Override methods in child classes
- Use the same method name with different object types
- Write code that works with behavior, not exact class names
- Create small systems that are easy to test

---

## General Rules

Follow these rules for all projects.

### 1. Write clean and readable code

Your code should be easy to read.

Use meaningful names for:

- classes
- variables
- attributes
- methods

Avoid unclear names such as:

```python
x
y
data1
thing
stuff
```

unless they are used in a very small and obvious context.

---

### 2. Do not overcomplicate the solution

The goal is to practice OOP basics.

Do not use advanced Python features unless they are really necessary.

Avoid using:

- external libraries
- databases
- files
- frameworks
- decorators, unless needed
- complex inheritance trees

Focus on simple class design.

---

### 3. Validate input data

Each class should reject invalid data according to the project requirements.

Invalid data should raise:

```python
ValueError
```

Do not silently ignore invalid data.

Do not allow objects to be created in an invalid state.

---

### 4. Keep object data consistent

After an object is created, its internal data should remain valid.

For example:

- A bank account balance should not become negative.
- A rectangle should not have a width of `0`.
- An employee should not have an empty name.
- A notification should not have an empty message.

---

### 5. Use methods to change object state

When an object has important internal data, it should not be changed randomly from outside the class.

For example, in the Bank Account project, the balance should change only through valid operations such as deposit and withdrawal.

---

### 6. Keep responsibilities clear

Each class should represent one clear concept.

For example:

- `BankAccount` should manage account data.
- `Rectangle` should represent a rectangle.
- `Employee` should represent common employee information.
- `EmailNotification` should represent an email notification.

Avoid putting unrelated logic inside a class.

---

### 7. Avoid unnecessary global variables

Do not store important project data in global variables unless there is a very clear reason.

Objects should store their own data.

Functions should receive the data they need through arguments.

---

### 8. Do not hardcode test results

Your code should calculate results correctly.

Do not write code that only works for the exact examples from the tests.

The solution should also work with other valid inputs.

---

## Testing Rules

Each project includes test cases.

Copy the test cases at the bottom of your Python file after your implementation.

If the file runs without errors, the tests pass.

Example:

```bash
python main.py
```

If all tests pass, you should see a success message such as:

```text
All tests passed!
```

If a test fails, Python will show an error.

Read the error message carefully and fix the code.

---

## How to Work on Each Project

For each project, follow this process:

1. Read the full project README.
2. Understand what the class or classes should do.
3. Implement only the first requirement.
4. Run the tests if possible.
5. Continue requirement by requirement.
6. Do not write everything at once.
7. When all requirements are done, run all tests.
8. If all tests pass, move to the next project.

---

## Recommended Workflow

Use this workflow for each project:

```text
Read requirement
↓
Write a small part of the code
↓
Run the file
↓
Fix errors
↓
Run again
↓
Continue
```

Do not wait until the end to test your code.

Testing often makes debugging much easier.

---

## OOP Checklist

Before finishing each project, check the following questions.

### Classes and Objects

- Did I create the required classes?
- Can I create objects from those classes?
- Does each object store the correct data?
- Are the attributes and methods easy to understand?

### Validation

- Does the program reject invalid data?
- Does invalid data raise `ValueError`?
- Can an object be created with bad data?
- Can an object become invalid after creation?

### Encapsulation

- Is important internal data protected?
- Can external code accidentally change important internal state?
- Are state changes controlled through methods?

### Abstraction

- Does the user interact with simple methods?
- Are calculation details hidden inside the class?
- Is the public interface easy to use?

### Inheritance

- Is common behavior placed in the parent class?
- Do child classes reuse parent behavior?
- Do child classes override only what needs to be different?

### Polymorphism

- Can different objects use the same method name?
- Can a function work with different object types without checking their exact class?
- Does each object know how to perform its own behavior?

---

## Project 1 — Bank Account Manager

Main topic:

```text
Encapsulation
```

You will build a `BankAccount` class that protects the account balance and allows balance changes only through valid operations.

You will practice:

- private/internal attributes
- read-only properties
- validation
- controlled updates
- transaction history
- protecting internal data from external modification

This project is complete when:

- the account can be created
- the owner can be read
- the balance can be read
- the balance cannot be directly modified
- deposits work
- withdrawals work
- invalid operations raise `ValueError`
- transaction history is stored correctly
- external changes do not modify internal history
- all tests pass

---

## Project 2 — Shape Calculator

Main topic:

```text
Abstraction
```

You will build shape classes that hide their internal area and perimeter calculations behind simple public methods.

You will practice:

- multiple classes with similar behavior
- clean public interfaces
- calculation methods
- validation
- summary functions
- working with objects through behavior

This project is complete when:

- rectangles work correctly
- circles work correctly
- triangles work correctly
- invalid dimensions are rejected
- each shape can describe itself
- each shape can calculate area and perimeter
- a summary function works with all shapes
- all tests pass

---

## Project 3 — Employee Payroll System

Main topic:

```text
Inheritance
```

You will build a payroll system with a base employee class and multiple specialized employee types.

You will practice:

- parent classes
- child classes
- shared attributes
- shared methods
- method overriding
- reusable behavior
- payroll report generation

This project is complete when:

- a base employee can be created
- common employee data is reused
- salaried employees calculate pay correctly
- hourly employees calculate pay correctly
- commission employees calculate pay correctly
- invalid employee data is rejected
- the payroll report works with different employee types
- all tests pass

---

## Project 4 — Notification System

Main topic:

```text
Polymorphism
```

You will build different notification classes that all use the same method name to send messages.

You will practice:

- same method name, different behavior
- working with a list of different object types
- avoiding class type checks
- designing around shared behavior
- writing flexible code

This project is complete when:

- email notifications work
- SMS notifications work
- push notifications work
- invalid notification data is rejected
- a function can send all notifications using the same method call
- the function does not check the exact class of each notification
- all tests pass

---

## Submission Format

When you finish a project, send the Python code for that project for review.

You can send:

- the full code from the Python file
- or a screenshot only if needed for an error

The code should include:

- your implementation
- the test cases at the bottom
- any error message if the tests fail

---

## Important Rule

Do not focus only on passing the tests.

Passing tests is important, but the main goal is to understand why the code works.

After each project, you should be able to explain:

- what classes you created
- what data each object stores
- what each method does
- what invalid inputs are rejected
- which OOP principle the project practices
- why that principle is useful
