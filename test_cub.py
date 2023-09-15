import unittest



# test case 1
class CubTest(unittest.TestCase):
     
    def test_cub(self):
        number = 7
        result = number * number * number

        self.assertEqual(343, result)


    def test_error(self):
        string = 'Tech academy'
        # number = 2  - Failed olacaq, çünki TypeError raise olmur
        

        with self.assertRaises(TypeError):
            res = string * string * string
            # print('TypeError occured', res)
            


if __name__ == '__main__':
    unittest.main()