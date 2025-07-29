from client import Client
from account import Account


class Bank:
    def __init__(
            self,
            agencies: list[int] | None = None,
            accounts: list[Account] | None = None,
            clients: list[Client] | None = None
    ):
        self.agencies = agencies or []
        self.accounts = accounts or []
        self.clients = clients or []

    def _agency_auth(self, agency):
        if agency in self.agencies:
            print('Agency authentication success')
            return True
        print('Agency authentication failure')
        return False

    def _client_auth(self, client):
        if client in self.clients:
            # print('Client authentication success')
            return True
        # print('Client authentication failure')
        return False

    def _account_auth(self, account):
        if account in self.accounts:
            # print('Account authentication success')
            return True
        # print('Account authentication failure')
        return False

    def _client_account_auth(self, client, account):
        if account is client.account:
            # print('Client account authentication success')
            return True
        # print('Client account authentication failure')
        return False

    def auth(self, agency: int, client: Client, account: Account) -> bool:
        if self._agency_auth(agency) and \
                self._client_auth(client) and \
                self._account_auth(account) and \
                self._client_account_auth(client, account):
            return True
        return False

    def __repr__(self):
        class_name = f'{type(self).__name__}'
        attrs = f'(Agencies: {self.agencies!r}, Accounts: {self.accounts!r}'\
            f', Clients: {self.clients!r})'
        return f'{class_name}{attrs}\n'


if __name__ == '__main__':
    client = Client('Kurosaki Ichigo', 17)
    client.create_account('savings', 111, 151515, 20000)
    client2 = Client('Inoue Orihime', 17)
    client2.create_account('current', 222, 161616, 9000)
    bank = Bank()
    bank.clients.extend([client, client2])
    if client.account is not None and client2.account is not None:
        bank.accounts.extend([client.account, client2.account])
        bank.agencies.extend([client2.account.agency, client2.account.agency])
        if bank.auth(client2.account.agency, client, client.account):
            client.account.withdraw(10000)
        if bank.auth(client2.account.agency, client2, client2.account):
            client2.account.withdraw(10000)

    # print(bank)
