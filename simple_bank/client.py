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

    def __repr__(self) -> str:
        class_name = f'{type(self).__name__}'
        attrs = f'(Name: {self.name!r}Age: {self.age!r}'\
            f'Assignment: Shinigami Substitute)'
        return f'{class_name}{attrs}\n'


class Client(People):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: Account | None = None

    def create_account(
            self, account_type: str, agency: int, account: int,
            balance: float = 0
    ) -> Account | None:
        if account_type == 'current':
            self.account = CurrentAccount(agency, account, balance)
            return self.account
        elif account_type == 'savings':
            self.account = SavingsAccount(agency, account, balance)
            return self.account
        else:
            print('Unknown account type')
            return None

    def __repr__(self) -> str:
        return super().__repr__() + f', Account: {self.account}'


if __name__ == '__main__':
    client = Client('Kurosaki Ichigo', 17)
    client.create_account('savings', 111, 151515, 20000)
    print(client)
