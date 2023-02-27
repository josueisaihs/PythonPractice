import unittest

from main import birthday

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.s = [2, 2, 1, 3, 2]
        self.d = 4
        self.m = 2

        self.variants_expected = [[2, 2], [1, 3]]
        self.expected = 2

    
    def test_birthday(self):
        result = birthday(self.s, self.d, self.m)
        self.assertEqual(result, self.expected)


if __name__ == '__main__':
    unittest.main()