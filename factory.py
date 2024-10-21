class User:
    def __init__(self, name) -> None:
        self.name = name
        
class AdminUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)
        
class CommonUser(User):
    def __init__(self, name, balance) -> None:
        super().__init__(name)
        self.currency = "US"
        self.balance = balance
        
class ForeignUser(User):
    def __init__(self, name, currency, balance) -> None:
        super().__init__(name)
        self.currency = currency
        self.balance = balance