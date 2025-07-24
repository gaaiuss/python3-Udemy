from account import Account, CurrentAccount, SavingsAccount


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def __repr__(self):
        class_name = f'{type(self).__name__}'
        attrs = f'Name: {self.name!r}\nAge: {self.age!r}'
        return f'{class_name} {attrs}\nAssignment: Shinigami Substitute'


class Client(People):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: Account | None = None

    def create_account(
            self, account_type: str, agency: int, account: int,
            balance: float = 0
    ) -> None:
        if account_type == 'current':
            self.account = CurrentAccount(agency, account, balance)
        elif account_type == 'savings':
            self.account = SavingsAccount(agency, account, balance)
        else:
            print('Unknown account type')


if __name__ == '__main__':
    client = Client('Caio Guilherme', 25)
    client.create_account('current', 123, 12345, 100)
    print(client)
