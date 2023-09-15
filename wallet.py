# Custom Exception 
# We can define User-Defined Excpetion, too

"""  This first class example is aimed to "Customizing Exception Classes":  """

class Wallet(Exception):
    
    def __init__(self, balance, message='InsufficientAmount'):
        self.balance = balance
        self.message = message
        super().__init__(self.message)


    def spend_cash(self, amount):
        self.balance = self.balance - amount
        return self.balance


    def add_cash(self, amount):
        self.balance = self.balance + amount
        return self.balance


wallet = Wallet(120)
print(wallet.spend_cash(30), 'spend_cash')
print(wallet.add_cash(30), 'add_cash')

wallet_1 = Wallet(10)
print(wallet_1.add_cash(70), 'add_cash')


wallet_2 = Wallet(60)
# print(wallet_2.spend_cash(90))
res = wallet_2.spend_cash(90)
print('res', res)


if res < 0:
    print("Traceback error will be raised at below. It is on purpose! Don't be panic! :)")
    print()
    raise Wallet(res)
else:
    print('Eligible balance: ', res)