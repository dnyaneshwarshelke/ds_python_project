'''class BankAccount():
    __var_pass="" #private variable of class it will hide 
    def __init__(self,password):
        self.__var_pass=password
        self.balance=balance
        self.account_num=account_num

obj=BankAccount(23452,1000,9099255)
print(obj)'''

class New_Bank_Account():
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self,amount):
        if amount>0 and amount <=self.balance:
            self.balance=self.balance-amount
    def get_balance(self):
        return self.balance

result=New_Bank_Account("954545",5000)
amount_val=1000
withdraw_val=600
result.deposit(amount_val)
result.withdraw(withdraw_val)
print(result.balance)
print(result.get_balance())


