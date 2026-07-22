# Shape Calculator

## Project Goal

Build a small shape calculator that works with different geometric shapes.

This project is focused on practicing **abstraction** in Python.

You will learn how to:

- Create multiple classes with similar behavior
- Hide calculation details inside methods
- Use clean public methods
- Validate object data
- Work with objects through a common interface
- Write code that depends on behavior, not implementation details

---

## Main OOP Principle

### Abstraction

Abstraction means exposing only the important behavior of an object and hiding the internal details.

In this project, the user should be able to ask a shape for its:

- area
- perimeter
- description

The user should not need to know how the shape calculates these values internally.

---

## Required Classes

Create the following classes:

```python
Rectangle
Circle
Triangle
```

Each class should support these methods:

```python
area()
perimeter()
describe()
```

---

## Required Function

Create a function named:

```python
summarize_shape(shape)
```

This function should accept any valid shape object and return a summary dictionary.

The function should not check if the shape is a rectangle, circle, or triangle.

It should simply use the public methods available on the shape object.

---

# Step 1 — Create a Rectangle

The program should allow creating a rectangle with:

- width
- height

Example:

```python
rect = Rectangle(4, 5)
```

The rectangle should be able to calculate its area.

```python
rect.area()
```

Expected result:

```python
20
```

The rectangle should be able to calculate its perimeter.

```python
rect.perimeter()
```

Expected result:

```python
18
```

The rectangle should be able to describe itself.

```python
rect.describe()
```

Expected result:

```python
"Rectangle with width 4 and height 5"
```

---

# Step 2 — Validate Rectangle Data

The rectangle should reject invalid dimensions.

## Rules

The width must be greater than `0`.

The height must be greater than `0`.

If the width or height is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
Rectangle(0, 5)
Rectangle(4, 0)
Rectangle(-4, 5)
Rectangle(4, -5)
```

All examples should raise `ValueError`.

---

# Step 3 — Create a Circle

The program should allow creating a circle with:

- radius

Example:

```python
circle = Circle(3)
```

Use this value of pi:

```python
3.14159
```

The circle should be able to calculate its area.

```python
circle.area()
```

The circle should be able to calculate its perimeter.

```python
circle.perimeter()
```

The perimeter of a circle is also called circumference.

The circle should be able to describe itself.

```python
circle.describe()
```

Expected result:

```python
"Circle with radius 3"
```

---

# Step 4 — Validate Circle Data

The circle should reject invalid radius values.

## Rules

The radius must be greater than `0`.

If the radius is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
Circle(0)
Circle(-3)
```

Both examples should raise `ValueError`.

---

# Step 5 — Create a Triangle

The program should allow creating a triangle with:

- side `a`
- side `b`
- side `c`

Example:

```python
triangle = Triangle(3, 4, 5)
```

The triangle should be able to calculate its perimeter.

```python
triangle.perimeter()
```

Expected result:

```python
12
```

The triangle should be able to calculate its area using Heron's formula.

The triangle should be able to describe itself.

```python
triangle.describe()
```

Expected result:

```python
"Triangle with sides 3, 4, 5"
```

---

# Step 6 — Validate Triangle Data

The triangle should reject invalid side values.

## Rules

Each side must be greater than `0`.

The three sides must form a valid triangle.

A triangle is valid only if:

```python
a + b > c
a + c > b
b + c > a
```

If the sides are invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
Triangle(0, 4, 5)
Triangle(3, 0, 5)
Triangle(3, 4, 0)
Triangle(-3, 4, 5)
Triangle(1, 2, 10)
```

All examples should raise `ValueError`.

---

# Step 7 — Summarize Any Shape

Create a function that receives a shape object and returns a dictionary.

Example:

```python
summary = summarize_shape(rect)
```

The returned dictionary should contain:

```python
{
    "description": "...",
    "area": ...,
    "perimeter": ...
}
```

The function should work with:

- `Rectangle`
- `Circle`
- `Triangle`

The function should not use different logic for each shape type.

---

# Expected Behavior Example

```python
rect = Rectangle(4, 5)

print(rect.describe())
print(rect.area())
print(rect.perimeter())
print(summarize_shape(rect))
```

Expected output:

```python
Rectangle with width 4 and height 5
20
18
{
    "description": "Rectangle with width 4 and height 5",
    "area": 20,
    "perimeter": 18
}
```

---

# Test Cases

Copy these tests at the bottom of your Python file after you finish your implementation.

If the program runs without errors, your solution passes the tests.

```python
# Project 2 — Shape Calculator tests

rect = Rectangle(4, 5)

assert rect.area() == 20
assert rect.perimeter() == 18
assert rect.describe() == "Rectangle with width 4 and height 5"

circle = Circle(3)

assert round(circle.area(), 2) == 28.27
assert round(circle.perimeter(), 2) == 18.85
assert circle.describe() == "Circle with radius 3"

triangle = Triangle(3, 4, 5)

assert triangle.perimeter() == 12
assert round(triangle.area(), 2) == 6.00
assert triangle.describe() == "Triangle with sides 3, 4, 5"

summary = summarize_shape(rect)

assert summary["description"] == "Rectangle with width 4 and height 5"
assert summary["area"] == 20
assert summary["perimeter"] == 18

summary = summarize_shape(circle)

assert summary["description"] == "Circle with radius 3"
assert round(summary["area"], 2) == 28.27
assert round(summary["perimeter"], 2) == 18.85

summary = summarize_shape(triangle)

assert summary["description"] == "Triangle with sides 3, 4, 5"
assert round(summary["area"], 2) == 6.00
assert summary["perimeter"] == 12

try:
    Rectangle(0, 5)
    assert False
except ValueError:
    assert True

try:
    Rectangle(4, 0)
    assert False
except ValueError:
    assert True

try:
    Circle(-3)
    assert False
except ValueError:
    assert True

try:
    Circle(0)
    assert False
except ValueError:
    assert True

try:
    Triangle(1, 2, 10)
    assert False
except ValueError:
    assert True

try:
    Triangle(0, 4, 5)
    assert False
except ValueError:
    assert True

print("All Shape Calculator tests passed!")
```

---

# Completion Checklist

Your project is complete when:

- A rectangle can be created with width and height.
- A rectangle can calculate its area.
- A rectangle can calculate its perimeter.
- A rectangle can describe itself.
- Invalid rectangle dimensions are rejected.
- A circle can be created with a radius.
- A circle can calculate its area.
- A circle can calculate its perimeter.
- A circle can describe itself.
- Invalid circle radius values are rejected.
- A triangle can be created with three sides.
- A triangle can calculate its perimeter.
- A triangle can calculate its area.
- A triangle can describe itself.
- Invalid triangle sides are rejected.
- Invalid triangle combinations are rejected.
- `summarize_shape()` works with all shape types.
- All test cases pass.

---

# Important Rule

Do not expose unnecessary calculation details to the user.

The user should interact with each shape through simple methods:

```python
area()
perimeter()
describe()
```
