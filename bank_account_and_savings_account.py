class BankAccount(object):
    def __init__(self, account_number = "00000", account_holder_name = "", 
                     account_balance = 0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = round(account_balance, 2)

    def __str__(self) -> str:
        return (("'account_number': '{}'," +
                "'account_holder_name': '{}',"+
                "'current_account_balance': '{}'")
                .format(self.get_account_number(),
                        self.get_account_holder_name(),
                        self.get_account_balance()))
    
    # TO DO ITEM: implement input value checks on this class
    def get_account_number(self):
        return self._account_number
    
    def set_account_number(self, value):
        self._account_number = value
        
    def get_account_holder_name(self):
        return self._account_holder_name

    def set_account_holder_name(self, value):
        self._acount_holder_name = value
        
    def get_account_balance(self):
        return self._account_balance
    
    def set_account_balance(self, value):
        self._account_balance = round(value, 2)
    

    def deposit(self, amount):
        # check if amount is integer or float
        # check if amount is "numeric," not necessarily integer or float
        if type(amount) != int and type(amount) != float:
            output_message = "Deposit amount must be a numeric value."
            return output_message

        # check if amount is negative
        if amount < 0:
            output_message = "Deposit must be a positive value."
            return output_message

        balance_before_deposit = self.get_account_balance()
        balance_after_deposit = balance_before_deposit + amount
        
        self.set_account_balance(balance_after_deposit)

        output_message = ("Deposit successful. Deposited $" 
                              + str(amount) + "\n")
        output_message += ("The current balance is $" 
                               + str(self.get_account_balance()) + "\n")

        return output_message
   
    def withdraw(self, amount):
        # check if amount is integer or float
        # check if amount is "numeric," not necessarily integer or float
        if type(amount) != int and type(amount) != float:
            output_message = "Withdrawal amount must be a numeric value."
            return output_message

        # check if amount is negative
        if amount < 0:
            output_message = "Withdrawal must be a positive value."
            return output_message

        balance_before_withdrawal = self.get_account_balance()
        balance_after_withdrawal = balance_before_withdrawal - amount

        self.set_account_balance(balance_after_withdrawal)

        output_message = ("Withdrawal successful. Withdrew $"
                              + str(amount) + "\n")
        output_message += ("The current balance is $" 
                               + str(self.get_account_balance()) + "\n")

        return output_message


class SavingsAccount(BankAccount):
    def __init__(self, bank_account_instance, interest_rate = 0.075):
        self.__dict__ = bank_account_instance.__dict__.copy()
        self.__class__ = SavingsAccount
        self._interest_rate = interest_rate

    def get_interest_rate(self):
        return self._interest_rate
    
    def set_interest_rate(self, value):
        self._interest_rate = value

    # call once a month or at a certain period
    def apply_interest(self):
        interest = self.get_account_balance() * self.get_interest_rate()
        self.deposit(interest)
        
        output_message = (
            "${:.2f} in interest was applied to the account. " +
            "The current balance is ${:.2f}").format(interest,
                                                 self.get_account_balance())
        
        return output_message

# I initialize a BankAccount with the following values
# Account Number: 5047391
# Account Holder Name: Jonathan Bournough
# Account Balance: 20516"
bank_account = BankAccount(5047391, "Jonathan Bournough", 20516)
print(bank_account) # I validate that the initialization was successful
print(bank_account.get_account_number()) # Print the account number
print(bank_account.get_account_holder_name()) # Print the holder's name
print("Bank account balance: $", bank_account.get_account_balance()) # Print the account balance

# I perform a deposit of fifteen dollars to the account
deposit_output_message = bank_account.deposit(15)
print(deposit_output_message) # print the output
# I confirm that the deposit was successful
print("Bank account balance: $", bank_account.get_account_balance())

# I perform a withdrawal of six thousand dollars to the account
withdrawal_output_message = bank_account.withdraw(6000)
print(withdrawal_output_message) # print the output
# I confirm that the withdrawal was successful
print("Bank account balance: $", bank_account.get_account_balance())

# I intialize a Savings Account for the same account holder
# Which initializes values and available methods from the Parent class.
savings_account = SavingsAccount(bank_account)
print(savings_account) # I validate that the initialization was successful
print(savings_account.get_account_number()) # Print the account number
print(savings_account.get_account_holder_name()) # Print the holder's name
print("Savings account balance: $", savings_account.get_account_balance()) # Print the account balance

# I perform an function/method call to apply interest to the account
print(savings_account.apply_interest()) 
# I validate that the interest is added to the account balance
print("Savings account balance: $", savings_account.get_account_balance())

# I perform a deposit of 
# seven thousand six hundred dollars and thirty eight cents 
# to the account
deposit_output_message = savings_account.deposit(7600.38)
print(deposit_output_message) # print the output
# I confirm that the deposit was successful
print("Savings account balance: $", savings_account.get_account_balance())

# I perform a withdrawal of 
# three thousand four hundred twenty dollars and seventy fifth cents 
# from the account
withdrawal_output_message = savings_account.withdraw(3420.75)
print(withdrawal_output_message) # print the output
# I confirm that the deposit was successful
print("Savings account balance: $", savings_account.get_account_balance())






