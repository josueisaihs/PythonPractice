import unittest
from FindTheMedian.main import findMedian
from FlippingTheMatrix.main import flippingMatrix
from SorkMerchant.sorkMerchant import sorkMerchant
from SubarrayDivision1.main import birthday
from XORStrings2.main import strings_xor

class MainTestCase(unittest.TestCase):    
    def test_birthday(self):
        s = [2, 2, 1, 3, 2]
        d = 4
        m = 2
        expected = 2

        result = birthday(s, d, m)
        self.assertEqual(result, expected)
    
    def test_xor(self):
        input_1 = "1100"
        input_2 = "1001"
        expected =  "0101"

        self.assertEqual(strings_xor(input_1, input_2), expected)

    def test_find_median(self):
        arr = [0, 1, 2, 4, 6, 5, 3]
        expected = 3

        self.assertEqual(findMedian(arr), expected)

    def test_flipping_matrix(self):
        matrix_1 = [[112, 42, 83, 119], [56, 125, 56, 49],[15, 78, 101, 43], [62, 98, 114, 108]]
        expected_1 = 414

        matrix_2 = [[34, 56, 234, 12],[45, 23, 76, 54],[98, 89, 90, 67],[76, 87, 78, 85]]
        expected_2 = 507

        self.assertEqual(flippingMatrix(matrix_1), expected_1)
        self.assertEqual(flippingMatrix(matrix_2), expected_2)

    def test_sork_merchant(self):
        n = 9
        arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        expected = 3

        self.assertEqual(sorkMerchant(n, arr), expected)


if __name__ == '__main__':
    unittest.main()