# Python User-Defined Exception   


# Class inherits from Exception, in turn, Exception inherits from BaseException
class InsufficientAmount(Exception):
    pass


class Wallet:
    
    def __init__(self, balance):
        self.balance = balance


    def spend_cash(self, amount):
        self.balance = self.balance - amount
        return self.balance


    def add_cash(self, amount):
        self.balance = self.balance + amount
        return self.balance


"""  test option'lar from task  """
# wallet = Wallet(120)
# print(wallet.spend_cash(30), 'spend_cash')
# print(wallet.add_cash(30), 'add_cash')

# wallet_1 = Wallet(10)
# print(wallet_1.add_cash(70), 'add_cash')


wallet_2 = Wallet(60)
result = wallet_2.spend_cash(90)
print('result: ', result)


# If we write, TypeError will raise

# if result < 0:
#     print('Traceback error will be raised. It is on purpose! ')
#     print()
#     raise Wallet(result)


# # Traceback (most recent call last):
#   File "wallet.py", line 92, in <module>
#     raise Wallet(result)
# TypeError: exceptions must derive from BaseException

# Because Wallet class can't get Inheritance from Exception class, In case, raise Wallet(result) can't recognize and create error


# we can use try/except block for solution

try:
    # wallet = Wallet(190)
    wallet = Wallet(90)
    result = wallet.spend_cash(120)

    if result < 0:
        print('result < 0\nRaise an exception: ')
        raise InsufficientAmount
    else:
        print('Available for amount')

except InsufficientAmount:
    print('InsufficientAmount')
