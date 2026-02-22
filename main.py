class MpesaAccount:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self):
        entered_pin = int(input("Enter PIN: "))
        if entered_pin == self.pin:
            return True
        else:
            print("Wrong PIN")
            return False

    def deposit(self, amount):
        if self.verify_pin():
            self.balance += amount
            print("Deposit successful")
            print("New balance:", self.balance)

    def withdraw(self, amount):
        if self.verify_pin():
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal successful")
                print("New balance:", self.balance)
            else:
                print("Insufficient funds")

account = MpesaAccount(1234, 1000)

account.deposit(500)
account.withdraw(300)