import unittest


# test case 2
class ListTest(unittest.TestCase):
    
    empty_list = []

    def test_list(self):
        list_ = ['komputer', 'klaviatura', 'monitor', 'proqramci']

        for l in list_:
            if 'a' in l:
                ListTest.empty_list.append(l)
                # self.assertIn('a', l)
                self.assertRegex(l, 'a')   # assertRegex(s, r) -> r.search(s), r'de s-i axtar məntiqi ilə işləyir
                """if not expected_regex.search(text):
                    TypeError: expected string or bytes-like object"""

        print(ListTest.empty_list)



if __name__ == '__main__':
    unittest.main()