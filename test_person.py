import unittest


# test case 3
from person import *
class PersonTest(unittest.TestCase):
    
    
    def setUp(self):
        with open('test.txt', 'w') as f:
            # f.write(person.name.capitalize() + ' ' + person.surname.capitalize())
            f.write(person1.get_fullname())
        
        # with open('test.txt', 'a') as f:
        #     f.write(person1.get_fullname())
        #     f.close()


    def test_file(self):
        # expected_result = 'Anar Veliyev'
        expected_result = 'Koroglu Mirzeyev'

        with open('test.txt', 'r') as f:
            actual_result = f.read()

            self.assertEqual(expected_result, actual_result)


            # Check if 'person' obj is instance of 'Person' class
            self.assertIsInstance(person, Person)
            

            


if __name__ == '__main__':
    unittest.main()