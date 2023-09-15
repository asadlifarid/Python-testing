import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        sums = [2, 5, 9]
        
        # We can write our messages
        self.assertEqual(16, sum(sums))
        
        # To check for object. List sums=[] from which class?
        self.assertIsInstance(sums, list) 
    

    def test_name(self):
        name = 'Asad'
        self.assertTrue(name, name.startswith('A'))
    

    def test_names(self):
        name = 'Lala'
        self.assertIs(name, 'lala', 'Lala is not equal to lala')  # Failed

    
    def test_NotNone(self):
        string = ''
        self.assertIsNotNone(string)
    

    def test_None(self):
        string = None
        self.assertIsNone(string)

    
    def test_member(self):
        list_ = ['x', 'y', 'z']
        string = 'python'

        self.assertIn('b', list_)  # a member of object is in container or not
        self.assertIn('py', string)






# if you want to see result that is called Test1, run in the terminal -> python sum_of_test Test_1
class Test_1(unittest.TestCase):

    def test_euqality(self):
        a = 65
        b = 56

        self.assertGreater(a, b)


    def test_lessequal(self):
        a = 88
        b = 88

        self.assertLessEqual(a, b)


    def test_division(self):

        with self.assertRaises(ZeroDivisionError):
            a = 17
            b = a // 0   # ZeroDivisionError raised


if __name__ == '__main__':
        unittest.main()