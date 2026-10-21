# Bank Account Manager

## Project Goal

Build a `BankAccount` class that manages a bank account in a safe and controlled way.

This project is focused on practicing **encapsulation** in Python.

You will learn how to:

- Create and use a class
- Store object data
- Protect internal state
- Validate input data
- Use properties
- Control how data is changed
- Keep a transaction history
- Prevent external code from accidentally modifying internal data

---

## Main OOP Principle

### Encapsulation

Encapsulation means keeping an object's internal data protected and allowing access to it only through controlled methods.

In this project, the account balance should not be changed directly from outside the class.

The balance should only change when the user makes a valid deposit or withdrawal.

---

## Required Class

Create a class named:

```python
BankAccount
```

The class should allow creating an account like this:

```python
account = BankAccount("Anna", 100)
```

The account should store:

- The account owner
- The current balance
- A transaction history

---

## Required Public Interface

Your class must support the following usage:

```python
account = BankAccount("Anna", 100)

account.owner
account.balance

account.deposit(50)
account.withdraw(30)

account.get_transaction_history()
```

---

# Step 1 — Create a Bank Account

The program should allow creating a bank account with:

- An owner name
- An initial balance

Example:

```python
account = BankAccount("Anna", 100)
```

After creation:

```python
account.owner
```

should return:

```python
"Anna"
```

And:

```python
account.balance
```

should return:

```python
100
```

---

# Step 2 — Validate Account Creation

The program should reject invalid accounts.

## Rules

The owner name must not be empty.

The initial balance must not be negative.

If the owner name is invalid, the program should raise:

```python
ValueError
```

If the initial balance is invalid, the program should raise:

```python
ValueError
```

## Invalid Examples

```python
BankAccount("", 100)
BankAccount("Anna", -50)
```

Both examples should raise `ValueError`.

---

# Step 3 — Protect the Balance

The account balance should be readable from outside the class.

Example:

```python
account.balance
```

However, the balance should not be directly editable from outside the class.

This should not be allowed:

```python
account.balance = 9999
```

Trying to change the balance directly should raise:

```python
AttributeError
```

The balance should only change through:

```python
deposit()
withdraw()
```

---

# Step 4 — Deposit Money

The account should allow depositing money.

Example:

```python
account.deposit(50)
```

If the account balance was `100`, after depositing `50`, the balance should become:

```python
150
```

## Rules

The deposit amount must be greater than `0`.

A valid deposit should increase the balance.

A valid deposit should be saved in the transaction history.

Invalid deposits should raise:

```python
ValueError
```

## Invalid Examples

```python
account.deposit(0)
account.deposit(-10)
```

Both examples should raise `ValueError`.

---

# Step 5 — Withdraw Money

The account should allow withdrawing money.

Example:

```python
account.withdraw(30)
```

If the account balance was `150`, after withdrawing `30`, the balance should become:

```python
120
```

## Rules

The withdrawal amount must be greater than `0`.

The withdrawal amount cannot be greater than the current balance.

A valid withdrawal should decrease the balance.

A valid withdrawal should be saved in the transaction history.

Invalid withdrawals should raise:

```python
ValueError
```

## Invalid Examples

```python
account.withdraw(0)
account.withdraw(-10)
account.withdraw(1000)
```

All examples should raise `ValueError`.

---

# Step 6 — Store Transaction History

The account should store all valid transactions.

Each transaction should contain:

- The transaction type
- The transaction amount
- The balance after the transaction

The transaction type should be one of:

```python
"deposit"
"withdraw"
```

Each transaction should be represented as a dictionary.

Example transaction:

```python
{
    "type": "deposit",
    "amount": 50,
    "balance_after": 150
}
```

---

# Step 7 — Read Transaction History

The user should be able to read the transaction history.

Example:

```python
history = account.get_transaction_history()
```

The returned history should contain all valid deposits and withdrawals in the order they happened.

Example:

```python
[
    {
        "type": "deposit",
        "amount": 50,
        "balance_after": 150
    },
    {
        "type": "withdraw",
        "amount": 30,
        "balance_after": 120
    }
]
```

---

# Step 8 — Protect Transaction History

The returned transaction history should not allow accidental modification of the account's internal transaction history.

For example:

```python
external_history = account.get_transaction_history()

external_history.append({
    "type": "deposit",
    "amount": 999,
    "balance_after": 999
})
```

This should not change the real transaction history stored inside the account.

---

# Expected Behavior Example

```python
account = BankAccount("Anna", 100)

account.deposit(50)
account.withdraw(30)

print(account.balance)
print(account.get_transaction_history())
```

Expected balance:

```python
120
```

Expected transaction history:

```python
[
    {
        "type": "deposit",
        "amount": 50,
        "balance_after": 150
    },
    {
        "type": "withdraw",
        "amount": 30,
        "balance_after": 120
    }
]
```

---

# Test Cases

Copy these tests at the bottom of your Python file after you finish your implementation.

If the program runs without errors, your solution passes the tests.

```python
# Project 1 — BankAccount tests

account = BankAccount("Anna", 100)

assert account.owner == "Anna"
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(30)
assert account.balance == 120

history = account.get_transaction_history()
assert len(history) == 2

assert history[0]["type"] == "deposit"
assert history[0]["amount"] == 50
assert history[0]["balance_after"] == 150

assert history[1]["type"] == "withdraw"
assert history[1]["amount"] == 30
assert history[1]["balance_after"] == 120

try:
    account.deposit(0)
    assert False
except ValueError:
    assert True

try:
    account.deposit(-10)
    assert False
except ValueError:
    assert True

try:
    account.withdraw(0)
    assert False
except ValueError:
    assert True

try:
    account.withdraw(1000)
    assert False
except ValueError:
    assert True

try:
    invalid_account = BankAccount("", 100)
    assert False
except ValueError:
    assert True

try:
    invalid_account = BankAccount("Anna", -50)
    assert False
except ValueError:
    assert True

try:
    account.balance = 9999
    assert False
except AttributeError:
    assert True

external_history = account.get_transaction_history()

external_history.append({
    "type": "deposit",
    "amount": 999,
    "balance_after": 999
})

assert len(account.get_transaction_history()) == 2

print("All BankAccount tests passed!")
```

---

# Completion Checklist

Your project is complete when:

- A `BankAccount` object can be created with an owner and an initial balance.
- Invalid owner names are rejected.
- Negative initial balances are rejected.
- The owner can be read.
- The balance can be read.
- The balance cannot be changed directly from outside the class.
- Deposits increase the balance.
- Withdrawals decrease the balance.
- Invalid deposits raise `ValueError`.
- Invalid withdrawals raise `ValueError`.
- Withdrawals greater than the balance raise `ValueError`.
- Each valid transaction is saved.
- Transaction history can be read.
- External changes to the returned history do not change the real internal history.
- All test cases pass.

---

# Important Rule

Do not focus on making the code short.

Focus on making the object safe, predictable, and easy to use.
