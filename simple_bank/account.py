from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(
            self, agency: float, account: float, balance: float = 0
    ) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    @abstractmethod
    def withdraw(self, value: float) -> float: ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'Value ${value} deposited')
        return self.balance

    def details(self, msg: str = '') -> float:
        print(f'{msg}\nYour balance is ${self.balance}')
        return self.balance


class CurrentAccount(Account):
    def __init__(self, agency, account, balance, balance_limit: float = 1000):
        super().__init__(agency, account, balance)
        self.balance_limit = balance_limit

    def withdraw(self, value: float) -> float:
        if value <= self.balance:
            self.balance -= value
            self.details(f'Value ${value} withdrawn')
            return self.balance
        else:
            self.balance_limit += self.balance
            self.balance = 0
            self.balance_limit -= value
            self.details(
                f'Value ${value} withdrawn using account limit\n'
                f'Account limit: {self.balance_limit}'
            )
            return self.balance


class SavingsAccount(Account):
    def withdraw(self, value: float) -> float:
        if value <= self.balance:
            self.balance -= value
            self.details(f'Value ${value} withdrawn')
            return self.balance
        else:
            self.details('Insuficient balance currency to withdraw')
            return self.balance


if __name__ == '__main__':
    savings_account = SavingsAccount(123, 12345, 5000)
    # savings_account.withdraw(5000)
    current_account = CurrentAccount(123, 12345, 400)
    # current_account.withdraw(5500)
    savings_account.deposit(-100)
    current_account.deposit(500)
