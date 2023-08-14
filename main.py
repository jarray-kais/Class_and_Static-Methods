class BankAccount:
    accounts=[]
    #Create a BankAccount class with the attributes interest rate and balance
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate=int_rate
    #Add a deposit method to the BankAccount class: increases the account balance by the given amount
    def deposit(self, amount):
        self.balance+= amount
        return self
    #Add a withdraw method to the BankAccount class:decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance-= amount
        else :
            print("Fonds insuffisants : frais de 5 $ facturés")
            self.balance-=5
        return self
    #Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self
    #Add a yield_interest method to the BankAccount class: increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance>0 :
            self.balance*=self.int_rate
        return self
    #use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()   
#Create 2 accounts
compte_1=BankAccount(0.03,0)
compte_2=BankAccount(0.01,0)
compte_1.deposit(100).deposit(500).deposit(200).withdraw(700).yield_interest().display_account_info()
compte_2.deposit(100).deposit(500).withdraw(200).withdraw(300).withdraw(100).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all_accounts()