import unittest

from main import strings_xor

class TestXOR(unittest.TestCase):
    def setUp(self):
        self.input_1 = "1100"
        self.input_2 = "1001"
        self.expected =  "0101"
    
    def test_xor(self):
        self.assertEqual(strings_xor(self.input_1, self.input_2), self.expected)

if __name__ == "__main__":
    unittest.main()