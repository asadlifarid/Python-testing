import unittest


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



if __name__ == '__main__':
    unittest.main()