# Teardown-to delete the tests we wrote


import unittest
import os


class TestSum(unittest.TestCase):

    @classmethod  # will be generated once 
    def setUpClass(self):
        print('setup function')  
        with open ('setup.txt', 'w') as f:
            f.write('Test text')


    def test_equality(self):
        print('name_of_test equality') 
        
        a = 12
        b = 4

        self.assertGreater(a, b)


    def test_lessequal(self):
        print('name_of_test lessequal') 
        
        a = 7
        b = 7

        self.assertLessEqual(a, b)


    def test_division(self):
        print('name_of_test division')
        
        
        with self.assertRaises(ZeroDivisionError):
            a = 22
            b = a // 0


    def test_file(self):
        print('test file') 
        expected_result = 'Test text'

        with open('setup.txt', 'r') as f:
            actual_result = f.read()

        self.assertEqual(actual_result, expected_result)

    @classmethod  # once, at the end will remove
    def tearDownClass(self):
        print('tearDown function') 
        os.remove('setup.txt')


if __name__ == '__main__':
    unittest.main()