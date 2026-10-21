from abc import ABC, abstractmethod
# from dataclasses import dataclass
# from typing import ClassVar

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, new_account):
        for current_account in self.accounts:
            if current_account.id == new_account.id:
                print("ID deja existent!")
                return

        self.accounts.append(new_account)

    def total_sold(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def print_accounts(self):
        print("Disponible accounts: ")
        for account in self.accounts:
            print(account)
        print("-----------------------")

    def find_account(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
        return None

    def deposit_to_account(self, id, amount):
        account = self.find_account(id)
        if account is not None:
            account.deposit(amount)
        else:
            print("Contul nu a fost găsit.")

    def withdraw_from_account(self, id, amount):
        account = self.find_account(id)
        if account is not None:
            account.withdraw(amount)
        else:
            print("Contul nu a fost găsit.")

    def transfer(self, from_id, to_id, amount):
        if not BankAccount.is_valid_amount(amount):
            print("Suma transferului trebuie sa fie pozitiva!")
            return

        from_account = self.find_account(from_id)
        to_account = self.find_account(to_id)

        if (from_account is not None) and (to_account is not None):
            if from_account is not to_account:
                if from_account.withdraw(amount):
                    to_account.deposit(amount)
            else:
                print("The from and to accounts are for the same")
        else:
            print("Contul nu a fost găsit.")

    def sort_accounts_by_balance(self):
        return sorted(self.accounts, key=lambda account: account.balance)

class BankAccount(ABC):
    bank_name = "Nicoleta's Bank"

    def __init__(self, id, owner, balance = 0):
        self.id = id
        self.owner = owner
        # self.__balance = 0 # initializam cu 0, in cazul in care initializam cu o valorea negativa, sa nu daie eroare - dar preferam sa primim eroare in acest caz
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Soldul nu poate fi negativ")
        self.__balance = value

    @abstractmethod
    def account_type(self):
        pass

    def account_description(self):
        return f"Proprietar: {self.owner}"

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            print("Depositul trebuie sa fie pozitiv!")
        else:
            self.balance += amount # use blance settter
            print(f"In contul {self.id}:{self.owner} au fost adaugati cu succes {amount}$")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            print("Suma extrasa trebuie sa fie pozitiva!")
            return False

        if self.balance < amount:
            print(f"{self.owner}, Sold insuficient!")
            print(f"Sold actual: {self.balance}$")
            print(f"Suma ceruta: {amount}$")
            print(f"Nu va ajung {abs(self.balance - amount)}$")
            print("-----------------------")
            return False
        else:
            self.balance -= amount
            print(f"In contul {self.id}:{self.owner} au fost extrasi cu succes {amount}$")

        return True

    def __str__(self):
        return f"{type(self).bank_name} | {self.owner}: {self.balance}$"


    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"id={self.id!r}, "
            f"owner={self.owner!r}, "
            f"balance={self.balance!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.id == other.id
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

class BasicAccount(BankAccount):
    def account_type(self):
        return "Cont obisnuit"


# Savings Account mosteneste de la Bank Account
class SavingsAccount(BankAccount):
    def __init__(self, id, owner, balance, interest_rate):
        super().__init__(id, owner, balance) #init-ul mosteneste de la bank account id, owner si balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    # Method Overriding - avem aceeasi metoda pentru ambele clase, da returneaza 2 lucruri diferite
    def account_type(self):
        return "Cont de economii"

    # Nu inlocuim complet toata metoda, dar mai adaugam la final ceva
    def account_description(self):
        description = super().account_description()
        return description + " | Tip: economii"

# @dataclass
# class Transaction():
#     id: int
#     account_id: str
#     amount: float
#     transaction_type: str
#     types: ClassVar[list[str]] = ["DEPOSIT", "WITHDRAW", "TRANSFER"]

#     def __post_init__(self):
#         if self.amount <= 0:
#             raise ValueError("amount trebuie să fie strict pozitiv")

#         if self.transaction_type not in self.types:
#             raise ValueError(f"transaction_type trebuie să fie una dintre valorile {', '.join(self.types)}")

def print_account_info(account):
    print(account.account_description())
    print(account.account_type())

def main():
    bank = Bank("Nicoleta's Bank")

    cont1 = BasicAccount("A001", "Ana", 100)
    cont2 = BasicAccount("A002", "Mihai", 250)
    cont3 = BasicAccount("A003", "Nicoleta", 60000)
    cont4 = BasicAccount("A004", "Alex")

    bank.add_account(cont1)
    bank.add_account(cont2)
    bank.add_account(cont3)
    bank.add_account(cont4)

    BasicAccount.change_bank_name("Nicoleta's Bank VIP")

    #atributul balance e privat si nu il putem modifica direct
    cont1.balance = 300  # modificare atributului prin setter
    cont1.deposit(200)   # modificare atributului folosind metoda

    bank.print_accounts()

    cont1.withdraw(100)
    cont1.withdraw(1000)

    print("Soldul total al tuturor conturilor este:", bank.total_sold())

    account = bank.find_account(cont2.id)
    if account is not None:
        print(account.balance)
    else:
        print("Contul nu a fost găsit.")

    bank.deposit_to_account(cont1.id, 1000)

    bank.withdraw_from_account(cont2.id, 50)
    bank.print_accounts()

    bank.transfer(cont1.id, cont3.id, 1000)
    bank.transfer(cont1.id, cont3.id, 10000)

    bank.print_accounts()

    bank.transfer(cont1.id, cont2.id, -50)

    savings = SavingsAccount("S001", "Ana", 1000, 0.05)
    print(savings.calculate_interest())

    print("---------------------------")

    print_account_info(cont1)
    print_account_info(savings)

    print(cont1)
    print(repr(cont1))

    print(cont1 == cont2)  # False
    print(cont1 == cont3)  # False

    for account in bank.sort_accounts_by_balance():
        print(account)

    # trans1 = Transaction(1, "A001", 23.3, "DEPOSIT")
    # trans2 = Transaction(1, "A001", 23.3, "DEPOSIT")
    # trans2 = Transaction(1, "A001", 23.3, "B2B")
    # trans3 = Transaction(1, "A001", -56, "DEPOSIT")
    # print(trans1)
    # print(trans1 == trans2)
    # print(trans1 == trans3)

    try:
        savings.balance = -500
    except ValueError as err:
        print(err)

    print(savings)

    savings.balance = 30
    print(savings)

    try:
        saving2 = SavingsAccount("S002", "Emma", -1000, 0.05)
    except ValueError as err:
        print(err)
    else:
        print("Cont creat cu succes")
    finally:
        print("Etapa finalizata")

    print("programul continua!")

if __name__ == "__main__":
    main()
