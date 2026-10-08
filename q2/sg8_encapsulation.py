class BankAccount: # Define the class BankAccount.
    
    # Initialize the data fields account_number and balance as private attributes.
    def __init__(self, a: int, b: float):
        self.__account_number = a
        self.__balance = b
    
    # Create setter methods for account_number and balance to have the user set their values.
    def set_account_number(self):
        a = int(input("Update account number to "))
        self.__account_number = a
        
    def set_balance(self):
        b = float(input("Update balance to "))
        
        # Ensure the balance cannot be negative; if it is, display an error message and do not update the balance.
        if b < 0:
            print("The balance must not be negative.")
        else:       
            self.__balance = b
    
    # Make use of the @property decorator to create getter methods for account_number and balance to access them.
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000.00) # Create an object of the class BankAccount with any account number and balance.

"""
Display the account number and balance of the object using the defined getter methods.
Then, use the defined setter methods to change the account number and balance of the object and then display them again.
These are done to showcase the methods.
"""

print("Account 1:")
print("")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")
print("")
a1.set_account_number()
a1.set_balance()
print("")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")