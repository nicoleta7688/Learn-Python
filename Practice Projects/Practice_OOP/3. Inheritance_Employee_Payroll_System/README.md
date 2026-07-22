# Employee Payroll System

## Project Goal

Build an employee payroll system that calculates pay for different employee types.

This project is focused on practicing **inheritance** in Python.

You will learn how to:

- Create a parent class
- Create child classes
- Reuse shared attributes and behavior
- Override methods
- Validate data in related classes
- Build a system where different objects share a common structure

---

## Main OOP Principle

### Inheritance

Inheritance allows one class to reuse behavior from another class.

In this project, all employees should share common data:

- name
- employee ID

But different employee types should calculate pay differently.

---

## Required Classes

Create the following classes:

```python
Employee
SalariedEmployee
HourlyEmployee
CommissionEmployee
```

---

## Required Function

Create a function named:

```python
generate_payroll_report(employees)
```

This function should receive a list of employee objects and return a payroll report.

---

# Step 1 — Create the Base Employee Class

Create a class named:

```python
Employee
```

The program should allow creating an employee with:

- name
- employee ID

Example:

```python
employee = Employee("Anna", "E001")
```

The employee should store:

- the employee name
- the employee ID

The employee should allow reading these values:

```python
employee.name
employee.employee_id
```

---

# Step 2 — Validate Employee Data

The base employee class should reject invalid data.

## Rules

The name must not be empty.

The employee ID must not be empty.

If the name or employee ID is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
Employee("", "E001")
Employee("Anna", "")
```

Both examples should raise `ValueError`.

---

# Step 3 — Get Employee Information

Every employee should be able to return a formatted information string.

Example:

```python
employee.get_info()
```

Expected result:

```python
"Anna (E001)"
```

The format must be:

```python
"<name> (<employee_id>)"
```

---

# Step 4 — Base Pay Calculation

The base employee class should define a pay calculation behavior.

However, a generic employee should not have a real salary calculation.

Calling pay calculation on a base employee should raise:

```python
NotImplementedError
```

Example:

```python
employee.calculate_pay()
```

This should raise `NotImplementedError`.

---

# Step 5 — Create a Salaried Employee

Create a class named:

```python
SalariedEmployee
```

A salaried employee should be created with:

- name
- employee ID
- monthly salary

Example:

```python
salaried = SalariedEmployee("John", "E002", 3000)
```

A salaried employee should reuse the common employee data.

The pay should be equal to the monthly salary.

Example:

```python
salaried.calculate_pay()
```

Expected result:

```python
3000
```

---

# Step 6 — Validate Salaried Employee Data

The monthly salary should be validated.

## Rules

The monthly salary must be greater than or equal to `0`.

If the monthly salary is invalid, the program should raise:

```python
ValueError
```

## Invalid Example

```python
SalariedEmployee("John", "E002", -1)
```

This should raise `ValueError`.

---

# Step 7 — Create an Hourly Employee

Create a class named:

```python
HourlyEmployee
```

An hourly employee should be created with:

- name
- employee ID
- hourly rate
- hours worked

Example:

```python
hourly = HourlyEmployee("Maya", "E003", 20, 80)
```

The pay should be calculated as:

```python
hourly rate * hours worked
```

Example:

```python
hourly.calculate_pay()
```

Expected result:

```python
1600
```

---

# Step 8 — Validate Hourly Employee Data

The hourly employee should reject invalid numeric values.

## Rules

The hourly rate must be greater than or equal to `0`.

The hours worked must be greater than or equal to `0`.

If one of these values is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
HourlyEmployee("Maya", "E003", -20, 80)
HourlyEmployee("Maya", "E003", 20, -80)
```

Both examples should raise `ValueError`.

---

# Step 9 — Create a Commission Employee

Create a class named:

```python
CommissionEmployee
```

A commission employee should be created with:

- name
- employee ID
- base salary
- sales amount
- commission rate

Example:

```python
commission = CommissionEmployee("Leo", "E004", 1000, 5000, 0.1)
```

The pay should be calculated as:

```python
base salary + sales amount * commission rate
```

Example:

```python
commission.calculate_pay()
```

Expected result:

```python
1500
```

---

# Step 10 — Validate Commission Employee Data

The commission employee should reject invalid values.

## Rules

The base salary must be greater than or equal to `0`.

The sales amount must be greater than or equal to `0`.

The commission rate must be between `0` and `1`.

The value `0` is allowed.

The value `1` is allowed.

Values lower than `0` or greater than `1` are invalid.

If one of these values is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
CommissionEmployee("Leo", "E004", -1000, 5000, 0.1)
CommissionEmployee("Leo", "E004", 1000, -5000, 0.1)
CommissionEmployee("Leo", "E004", 1000, 5000, 1.5)
CommissionEmployee("Leo", "E004", 1000, 5000, -0.1)
```

All examples should raise `ValueError`.

---

# Step 11 — Generate a Payroll Report

Create a function named:

```python
generate_payroll_report(employees)
```

The function should receive a list of employee objects.

It should return a list of dictionaries.

Each dictionary should contain:

```python
{
    "employee": "...",
    "pay": ...
}
```

The `"employee"` value should come from the employee information string.

The `"pay"` value should come from the employee pay calculation.

The function should work with all employee types.

---

# Expected Behavior Example

```python
employees = [
    SalariedEmployee("John", "E002", 3000),
    HourlyEmployee("Maya", "E003", 20, 80),
    CommissionEmployee("Leo", "E004", 1000, 5000, 0.1)
]

report = generate_payroll_report(employees)

print(report)
```

Expected result:

```python
[
    {"employee": "John (E002)", "pay": 3000},
    {"employee": "Maya (E003)", "pay": 1600},
    {"employee": "Leo (E004)", "pay": 1500}
]
```

---

# Test Cases

Copy these tests at the bottom of your Python file after you finish your implementation.

If the program runs without errors, your solution passes the tests.

```python
# Project 3 — Employee Payroll tests

employee = Employee("Anna", "E001")

assert employee.name == "Anna"
assert employee.employee_id == "E001"
assert employee.get_info() == "Anna (E001)"

try:
    employee.calculate_pay()
    assert False
except NotImplementedError:
    assert True

salaried = SalariedEmployee("John", "E002", 3000)

assert salaried.name == "John"
assert salaried.employee_id == "E002"
assert salaried.get_info() == "John (E002)"
assert salaried.calculate_pay() == 3000

hourly = HourlyEmployee("Maya", "E003", 20, 80)

assert hourly.name == "Maya"
assert hourly.employee_id == "E003"
assert hourly.get_info() == "Maya (E003)"
assert hourly.calculate_pay() == 1600

commission = CommissionEmployee("Leo", "E004", 1000, 5000, 0.1)

assert commission.name == "Leo"
assert commission.employee_id == "E004"
assert commission.get_info() == "Leo (E004)"
assert commission.calculate_pay() == 1500

employees = [salaried, hourly, commission]
report = generate_payroll_report(employees)

assert report == [
    {"employee": "John (E002)", "pay": 3000},
    {"employee": "Maya (E003)", "pay": 1600},
    {"employee": "Leo (E004)", "pay": 1500}
]

try:
    Employee("", "E001")
    assert False
except ValueError:
    assert True

try:
    Employee("Anna", "")
    assert False
except ValueError:
    assert True

try:
    SalariedEmployee("John", "E002", -1)
    assert False
except ValueError:
    assert True

try:
    HourlyEmployee("Maya", "E003", -20, 80)
    assert False
except ValueError:
    assert True

try:
    HourlyEmployee("Maya", "E003", 20, -80)
    assert False
except ValueError:
    assert True

try:
    CommissionEmployee("Leo", "E004", -1000, 5000, 0.1)
    assert False
except ValueError:
    assert True

try:
    CommissionEmployee("Leo", "E004", 1000, -5000, 0.1)
    assert False
except ValueError:
    assert True

try:
    CommissionEmployee("Leo", "E004", 1000, 5000, 1.5)
    assert False
except ValueError:
    assert True

try:
    CommissionEmployee("Leo", "E004", 1000, 5000, -0.1)
    assert False
except ValueError:
    assert True

print("All Employee Payroll tests passed!")
```

---

# Completion Checklist

Your project is complete when:

- A base employee can be created with a name and employee ID.
- Invalid employee names are rejected.
- Invalid employee IDs are rejected.
- Every employee can return formatted employee information.
- The base employee pay calculation raises `NotImplementedError`.
- A salaried employee can calculate pay correctly.
- Invalid salaried employee data is rejected.
- An hourly employee can calculate pay correctly.
- Invalid hourly employee data is rejected.
- A commission employee can calculate pay correctly.
- Invalid commission employee data is rejected.
- The payroll report works with different employee types.
- All test cases pass.

---

# Important Rule

Do not duplicate common employee behavior in every child class.

Shared employee data and shared employee behavior should belong to the base employee class.
