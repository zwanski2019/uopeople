
class BankAccount:
    def __init__(self, initial_balance = 0):
        '''
        Initializes the account balance based on the optional
        argument provided, and initializes the transaction 
        history.
        
        The transaction history is a list of (amount, description)
        tuples. The transaction history should be initialized with
        the initial balance, and updated every time a withdrawal or
        deposit is made to this account. 
        '''
        self.balance = initial_balance
        des = "Initial Balance"
        self.transaction_history = [(self.balance, des)]

    
    def withdraw(self, amount, description=''):
        '''
        Withdraws the amount into this account. The amount
        should always be positive. 
        
        An optional description can be included. The deposit
        amount and description will be placed in the transaction
        history as the tuple (amount, description).
        '''
        self.amount = abs(amount)
        self.balance -= amount
        self.transaction_history += [(-amount, description)]
        return self.transaction_history
        
        
    
    def deposit(self, amount, description=''):
        '''
        Deposits the amount into this account. The amount
        should always be positive. 
        
        An optional description can be included. The deposit
        amount and description will be placed in the transaction
        history as the tuple (amount, description).
        '''
        self.amount = abs(amount)
        self.balance += self.amount
        self.transaction_history += [(amount, description)]
        return self.transaction_history
        

    
    def balance(self):
        '''
        Returns the current account balance.
        '''
        return self.balance
    

    def overdrawn(self):
        '''
        Returns true if the account balance is less than 0.
        '''
        if self.balance < 0:
            return True
        
    
    def print_account(self):
        '''
        Prints the transactions and balance for this account.
        '''
        print 'Transactions:'
        for i in self.transaction_history:
            dollar = '$'
            for element in i:
                dollar += ' ' + str(element)
            print dollar    
        print 'Balance: $',  self.balance   
            
        if self.overdrawn() == True:
            print '\nWARNING: THIS ACCOUNT IS OVERDRAWN!'
        

    def __add__(self, other):
        '''
        Adds together two separate accounts.
        '''
        add = self.balance + other.balance
        return BankAccount(add)
        
    def __sub__(self, other):
        """
        Subtracts account balance from another account.
        """
        sub = self.balance - other.balance
        return BankAccount(sub)
        

    # make sure you add functions to overload 
    # the + and - operators here!


# tests out the bank account class
# shows how to use the deposit() and withdraw() methods

account1 = BankAccount()

account1.deposit(100, 'Pay')
account1.withdraw(23.14, 'Groceries')
account1.deposit(20)
account1.withdraw(11.54)

print '[ Account 1 ]'
account1.print_account()

print

# notice that there is always an "initial transaction"
# when an account is created

account2 = BankAccount(50)

print '[ Account 2 ]'
account2.print_account()

print

# accounts may be added together
account3 = account1 + account2

print '[ Account 3 ]'
account3.print_account()
print

# accounts may be subtraced

account4 = account2 - account1

print '[ Account 4 ]'
account4.print_account()
