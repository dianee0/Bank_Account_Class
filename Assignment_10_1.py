'''
Diane Poeng
Assignment_10_1.py
Assignment 10.1
The purpose of this assignment is to implement a real world object as a class and have it perform behaviors it would typically 
perform. In this case, I will be creating a bank as a real world object with the abilities to set the deposit, withdrawal, and get these two
as getter-methods, display the balance, transfer balances from an account to another, and provide bank details.
Citations: https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide, https://www.datacamp.com/community/tutorials/property-getters-setters
https://www.geeksforgeeks.org/encapsulation-in-python/, 
'''
# Imported modules
import random as r
# creating Bank class
class Bank:
    # randomly generate routing number and accounting number -> class variables
    routing_number = r.randint(100000000,199999999)
    account_number = r.randint(100000000000,199999999999)
    def __init__(self, checkings, savings):
        self.checkings = checkings
        self.savings = savings
    # setDeposit deposits money on the designated account (checkings or savings)
    def setDeposit(self, deposit):
        self.__deposit = deposit
        print(f'your bank statement before: {self.checkings}')
        account = str(input('Deposit to Checkings or Savings account: ')).lower()
        if account == 'checkings' or account == 'savings':
            if account == 'checkings':
                self.checkings = self.__deposit + self.checkings
                return self.checkings
            if account == 'savings':
                self.savings = self.__deposit + self.savings
                return self.savings
        else:
            raise ValueError
    # setWithdraw withdraws money on the designated account (checkings or savings)
    def setWithdraw(self, withdraw):
        self.__withdraw = withdraw
        account = str(input('Deposit to Checkings or Savings account: ')).lower()
        if account == 'checkings' or account == 'savings':
            if account == 'checkings':
                self.checkings = self.checkings - self.__withdraw
                return self.checkings
            if account == 'savings':
                self.savings = self.savings - self.__withdraw
                return self.savings
        else:
            raise ValueError
    # getter-method: returns how much the user wants to deposit
    def getDeposit(self):
        return self.__deposit
    # getter-method: returns how much the user wants to withdraw
    def getWithdraw(self):
        return self.__withdraw
    # displays the balances of both accounts
    def display_bal(self):
        print(f"Your Checkings Balance: {self.checkings}")
        print(f"Your Savings Balance: {self.savings}")
    # transfers money based from on account to another
    def transfer(self, amount):
        self.amount = amount
        transfer = int(input("If you would like to transfer from checkings to savings enter '1'. Enter '0' to transfer savings to checkings. "))
        if transfer == 0 or transfer == 1:
            print(transfer)
            if bool(transfer) == True:
                print("Checkings to savings")
                self.checkings,self.savings = self.checkings - self.amount, self.savings + self.amount
                print(f'Checkings New Balance: {self.checkings}, Savings New Balance: {self.savings}')
            if bool(transfer) == False:
                print("Savings to Checkings")
                self.savings,self.checkings = self.savings - self.amount, self.checkings + self.amount
                print(f'Savings New Balance: {self.savings}, Checkings New Balance: {self.checkings}')
        else:
            raise ValueError
    # returns the randomly generated routing numbers and account numbers
    def bankDetails(self):
        return f'Routing Number: {self.routing_number}, Account Number: {self.account_number}'


def main():
    b = Bank(5000,6000)
    # b.setDeposit(600)
    # b.setDeposit(800)
    # b.getDeposit()
    # b.setWithdraw(500)
    # b.getWithdraw()
    # b.transfer(4000)
    # b.display_bal()
    # print(b.bankDetails())
if __name__ == "__main__":
    main()
