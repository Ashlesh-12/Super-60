from datetime import datetime

# Define custom exceptions based on the MBW rules
class AccountNotActiveException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class WithdrawalFailedException(Exception):
    pass

class DepositFailedException(Exception):
    pass

class TransferLimitExceededException(Exception):
    pass

# Define account privileges with transfer limits
PRIVILEGE_LIMITS = {
    "PREMIUM": 100000,
    "GOLD": 50000,
    "SILVER": 25000
}

class Account:
    account_counter = 1000  # To generate unique account numbers

    def _init_(self, name, account_type, privilege="SILVER", is_active=True, balance=0):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.name = name
        self.account_type = account_type
        self.privilege = privilege
        self.is_active = is_active
        self.balance = balance
        self.activated_date = datetime.now()
        self.closed_date = None
        self.transactions = []

    def deposit(self, amount):
        if not self.is_active:
            raise AccountNotActiveException("Cannot deposit to an inactive account.")
        self.balance += amount
        self.log_transaction("Deposit", amount)
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if not self.is_active:
            raise AccountNotActiveException("Cannot withdraw from an inactive account.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.log_transaction("Withdrawal", amount)
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def transfer(self, target_account, amount):
        if not self.is_active or not target_account.is_active:
            raise AccountNotActiveException("Both accounts must be active to perform transfer.")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds for transfer.")
        if amount > PRIVILEGE_LIMITS.get(self.privilege, 0):
            raise TransferLimitExceededException(f"Transfer limit exceeded for {self.privilege} account.")
        
        self.balance -= amount
        target_account.balance += amount
        self.log_transaction("Transfer Out", amount)
        target_account.log_transaction("Transfer In", amount)
        print(f"Transferred {amount} to Account {target_account.account_number}. New balance is {self.balance}.")

    def close_account(self):
        self.is_active = False
        self.closed_date = datetime.now()
        print(f"Account {self.account_number} is now closed.")

    def log_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now()
        }
        self.transactions.append(transaction)
        print(f"Logged {transaction_type} of {amount}.")

# Testing the Account functionality
try:
    # Creating accounts
    account1 = Account(name="Alice", account_type="Savings", privilege="PREMIUM", balance=50000)
    account2 = Account(name="Bob", account_type="Current", privilege="GOLD", balance=10000)

    # Testing deposit
    account1.deposit(10000)

    # Testing withdrawal
    account1.withdraw(15000)

    # Testing transfer
    account1.transfer(account2, 20000)

    # Closing account
    account1.close_account()

except (AccountNotActiveException, InsufficientFundsException, 
        WithdrawalFailedException, DepositFailedException, 
        TransferLimitExceededException) as e:
    print(e)