import unittest


# test case 5
from exception import *
class WalletTest(unittest.TestCase):

    def test_amount(self):

        print()
        print('test_amount function started: ')

        with self.assertRaises(InsufficientAmount):
            
            try:
                wallet = Wallet(60)
                result = wallet.spend_cash(90)

                if result < 0:
                    # print('result < 0\nInsufficientAmount')
                    raise InsufficientAmount
                else:
                    print('Eligible for amount')

            # except InsufficientAmount:
            #     print('Exception occured: Not enough balance')   ->  "AssertionError: InsufficientAmount not raised"
            # To avoid this error, add finally block
            finally:
                print('End of test')
        



if __name__ == '__main__':
    unittest.main()