class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Пополнение на {amount} тенге ")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Снятие {amount} тенге ")
        else:
            print("Недопустимая сумма для снятия или недостаточно средств на счете.")

    def __str__(self):
        return f"Владелец счета: {self._owner_name}\nНомер счета: {self._account_number}\nБаланс: {self._balance} тенге."

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Баланс не может быть отрицательным.")
    
    def __eq__(self, other):
        return self._balance == other._balance

    def __lt__(self, other):
        return self._balance < other._balance

    def __gt__(self, other):
        return self._balance > other._balance


class SavingAccount(BankAccount):
    def __init__(self, owner_name, account_number, balance=0, interest_rate=0):
        super().__init__(owner_name, account_number, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        self.deposit(interest)
        print(f"Начислены проценты в размере {interest} тг.")

# Пример использования классов:
if __name__ == "__main__":
    # Создаем обычный банковский счет
    account1 = BankAccount("Кумаров Мади", "1234567890")
    print(account1)
    account1.deposit(1000)
    print(account1)
    account1.withdraw(500)
    print(account1)

    # Создаем сберегательный счет с процентной ставкой
    savings1 = SavingAccount("Назар Дамир", "0987654321", interest_rate=5)
    print(savings1)
    savings1.deposit(2000)
    print(savings1)
    savings1.calculate_interest()
    print(savings1)

    # Сравнение счетов
    account2 = BankAccount("Жакысылык Мерей", "1357924680", balance=1500)
    print(account1 == account2)  # False
    print(account1 < account2)   # True
    print(account1 > account2)   # False
