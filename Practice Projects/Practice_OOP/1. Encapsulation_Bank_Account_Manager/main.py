class BankAccount:
    def __init__(self, owner, balance):
        check_valid_nr(balance, "balance")
        self.__balance = balance

        self.owner = owner
        self.__transaction_history = []

    @property
    def owner(self):
        return self.__owner_name

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError("owner should be str")
        elif value.strip() == "":
            raise ValueError("owner should no be empty")
        self.__owner_name = value

    @property
    def balance(self):
        return self.__balance

    @property
    def transaction_history(self):
        return self.__transaction_history.copy()

    def deposit(self, value):
        check_valid_nr(value, 'deposit_value')
        if value == 0:
            raise ValueError(f"deposit_value should be greater than 0")
        self.__balance += value
        self.__transaction_history.append({
                                            "type": "deposit",
                                            "amount": value,
                                            "balance_after": self.balance
                                        })

    def withdraw(self, value):
        check_valid_nr(value, 'deposit_value')
        if value == 0:
            raise ValueError(f"deposit_value should be greater than 0")
        if value > self.balance:
            raise ValueError("not enought balance")
        self.__balance -= value
        self.__transaction_history.append({
                                    "type": "withdraw",
                                    "amount": value,
                                    "balance_after": self.balance
                                })

    def get_transaction_history(self):
        return(self.transaction_history)


def check_valid_nr(value, attribute):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{attribute} should be int or float")
    elif value < 0:
        raise ValueError(f"{attribute} should be greater than 0")

def main():
    # BankAccount tests:

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


if __name__ == "__main__":
    main()