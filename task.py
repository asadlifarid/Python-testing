import unittest


"""  all tests in together  """



# test_case 1
class CubTest(unittest.TestCase):
     
    def test_cub(self):
        number = 7
        result = number * number * number

        self.assertEqual(343, result)


    def test_error(self):
        string = 'Tech academy'
        # number = 2  - Failed, TypeError can't raise 
        
        with self.assertRaises(TypeError):
            res = string * string * string
            # print('TypeError occured', res)
            
            


# test_case 2
class ListTest(unittest.TestCase):
    
    empty_list = []

    def test_list(self):
        list_ = ['komputer', 'klaviatura', 'monitor', 'proqramchi']

        for l in list_:
            if 'a' in l:
                ListTest.empty_list.append(l)
                self.assertRegex(l, 'a')   # assertRegex(s, r) -> r.search(s),
                """if not expected_regex.search(text):
                    TypeError: expected string or bytes-like object"""

        print(ListTest.empty_list)


# test case 3
from person import *
class PersonTest(unittest.TestCase):
    
    
    def setUp(self):
        with open('test.txt', 'w') as f:
            # f.write(person.name.capitalize() + ' ' + person.surname.capitalize())
            f.write(person.get_fullname())


    def test_file(self):
        expected_result = 'Anar Veliyev'
        # expected_result = 'Koroglu Mirzeyev'

        with open('test.txt', 'r') as f:
            actual_result = f.read()

            self.assertEqual(expected_result, actual_result)

            # Check if 'person' obj is instance of 'Person' class
            self.assertIsInstance(person, Person)
            




# test case 4
class CapitalizeTest(unittest.TestCase):

    def test_text(self):
        word = 'tech'
        result = word.capitalize()

        self.assertEqual(result, 'Tech')


    def test_error(self):
        number = 33
        
        
        with self.assertRaises(AttributeError):
            number.capitalize()

        with self.assertRaises(TypeError):
            number + ''



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


