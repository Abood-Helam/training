#balance = 0

#def main():
#    print("balance:", balance)
#    deposit(100)
#    withdraw(50)
#    print("balance:", balance)

#def deposit(n):
#    global balance
#    balance += n

#def withdraw(n):
#    global balance
    
#    balance -= n


#if __name__=="__main__":
#    main()

class Acount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    acount = Acount()
    print("Balance", acount.balance)
    acount.deposit(100)
    acount.withdraw(50)
    print("Balance", acount.balance)

if __name__=="__main__":
    main()