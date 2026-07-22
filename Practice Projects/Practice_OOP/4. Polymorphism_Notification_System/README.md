# Notification System

## Project Goal

Build a notification system that can send different types of notifications using the same public behavior.

This project is focused on practicing **polymorphism** in Python.

You will learn how to:

- Create different classes with the same method name
- Use objects of different types in the same list
- Call the same method on different object types
- Design objects around shared behavior
- Avoid checking object types manually
- Write flexible and extensible code

---

## Main OOP Principle

### Polymorphism

Polymorphism means that different objects can respond to the same method call in their own way.

In this project, every notification type should have a method named:

```python
send()
```

The program should be able to call `send()` on any notification object without caring what exact type of notification it is.

---

## Required Classes

Create the following classes:

```python
EmailNotification
SMSNotification
PushNotification
```

Each class should have a method named:

```python
send()
```

---

## Required Function

Create a function named:

```python
send_all(notifications)
```

This function should receive a list of notification objects.

It should call `send()` on each notification object.

It should return a list of sent message strings.

---

# Step 1 — Create an Email Notification

Create a class named:

```python
EmailNotification
```

The program should allow creating an email notification with:

- recipient email
- subject
- message

Example:

```python
email = EmailNotification(
    "anna@example.com",
    "Welcome",
    "Your account has been created."
)
```

The email notification should be able to send itself.

Example:

```python
email.send()
```

Expected result:

```python
"Email sent to anna@example.com: Welcome - Your account has been created."
```

---

# Step 2 — Validate Email Notification Data

The email notification should reject invalid data.

## Rules

The recipient email must contain `"@"`.

The subject must not be empty.

The message must not be empty.

If one of these values is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
EmailNotification("annaexample.com", "Welcome", "Message")
EmailNotification("anna@example.com", "", "Message")
EmailNotification("anna@example.com", "Welcome", "")
```

All examples should raise `ValueError`.

---

# Step 3 — Create an SMS Notification

Create a class named:

```python
SMSNotification
```

The program should allow creating an SMS notification with:

- phone number
- message

Example:

```python
sms = SMSNotification(
    "123456789",
    "Your code is 1234."
)
```

The SMS notification should be able to send itself.

Example:

```python
sms.send()
```

Expected result:

```python
"SMS sent to 123456789: Your code is 1234."
```

---

# Step 4 — Validate SMS Notification Data

The SMS notification should reject invalid data.

## Rules

The phone number must contain only digits.

The phone number must have at least `7` characters.

The message must not be empty.

If one of these values is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
SMSNotification("123abc", "Message")
SMSNotification("123", "Message")
SMSNotification("123456789", "")
```

All examples should raise `ValueError`.

---

# Step 5 — Create a Push Notification

Create a class named:

```python
PushNotification
```

The program should allow creating a push notification with:

- device ID
- message

Example:

```python
push = PushNotification(
    "device-001",
    "You have a new message."
)
```

The push notification should be able to send itself.

Example:

```python
push.send()
```

Expected result:

```python
"Push notification sent to device-001: You have a new message."
```

---

# Step 6 — Validate Push Notification Data

The push notification should reject invalid data.

## Rules

The device ID must not be empty.

The message must not be empty.

If one of these values is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
PushNotification("", "Message")
PushNotification("device-001", "")
```

Both examples should raise `ValueError`.

---

# Step 7 — Send Multiple Notifications

Create a function named:

```python
send_all(notifications)
```

The function should receive a list of notification objects.

It should call:

```python
send()
```

on each notification object.

It should return a list containing all sent message strings.

The function should work with:

- email notifications
- SMS notifications
- push notifications

The function should not check the exact class of each notification.

---

# Expected Behavior Example

```python
notifications = [
    EmailNotification("anna@example.com", "Welcome", "Your account has been created."),
    SMSNotification("123456789", "Your code is 1234."),
    PushNotification("device-001", "You have a new message.")
]

results = send_all(notifications)

print(results)
```

Expected result:

```python
[
    "Email sent to anna@example.com: Welcome - Your account has been created.",
    "SMS sent to 123456789: Your code is 1234.",
    "Push notification sent to device-001: You have a new message."
]
```

---

# Test Cases

Copy these tests at the bottom of your Python file after you finish your implementation.

If the program runs without errors, your solution passes the tests.

```python
# Project 4 — Notification System tests

email = EmailNotification(
    "anna@example.com",
    "Welcome",
    "Your account has been created."
)

assert email.send() == "Email sent to anna@example.com: Welcome - Your account has been created."

sms = SMSNotification(
    "123456789",
    "Your code is 1234."
)

assert sms.send() == "SMS sent to 123456789: Your code is 1234."

push = PushNotification(
    "device-001",
    "You have a new message."
)

assert push.send() == "Push notification sent to device-001: You have a new message."

notifications = [email, sms, push]

results = send_all(notifications)

assert results == [
    "Email sent to anna@example.com: Welcome - Your account has been created.",
    "SMS sent to 123456789: Your code is 1234.",
    "Push notification sent to device-001: You have a new message."
]

try:
    EmailNotification("annaexample.com", "Welcome", "Message")
    assert False
except ValueError:
    assert True

try:
    EmailNotification("anna@example.com", "", "Message")
    assert False
except ValueError:
    assert True

try:
    EmailNotification("anna@example.com", "Welcome", "")
    assert False
except ValueError:
    assert True

try:
    SMSNotification("123abc", "Message")
    assert False
except ValueError:
    assert True

try:
    SMSNotification("123", "Message")
    assert False
except ValueError:
    assert True

try:
    SMSNotification("123456789", "")
    assert False
except ValueError:
    assert True

try:
    PushNotification("", "Message")
    assert False
except ValueError:
    assert True

try:
    PushNotification("device-001", "")
    assert False
except ValueError:
    assert True

print("All Notification System tests passed!")
```

---

# Completion Checklist

Your project is complete when:

- An email notification can be created.
- Invalid email data is rejected.
- An email notification can send itself.
- An SMS notification can be created.
- Invalid SMS data is rejected.
- An SMS notification can send itself.
- A push notification can be created.
- Invalid push notification data is rejected.
- A push notification can send itself.
- `send_all()` works with a list of different notification objects.
- `send_all()` does not need to know the exact class of each notification.
- All test cases pass.

---

# Important Rule

Do not write separate sending logic inside `send_all()` for each notification type.

The function should trust that each notification object knows how to send itself.
