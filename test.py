import unittest
from FindTheMedian.main import findMedian
from FlippingTheMatrix.main import flippingMatrix
from OpenAI.enviroment import environ
from ReverseLinkedList.main import create_linked_list, reverse_linked_list, reverse_linked_list_recursive
from SorkMerchant.sorkMerchant import sorkMerchant
from SubarrayDivision1.main import birthday
from UseProperty.main import User
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

    def test_reverse_linked_list(self):
        list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        expected_1 = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        list_2 = [100, 99, 98, 97, 96, 95]
        expected_2 = [95, 96, 97, 98, 99, 100]

        self.assertEqual(create_linked_list(list_1).get_list(), list_1)
        self.assertEqual(create_linked_list(list_2).get_list(), list_2)

        self.assertEqual(reverse_linked_list(create_linked_list(list_1)).get_list(), expected_1)
        self.assertEqual(reverse_linked_list(create_linked_list(list_2)).get_list(), expected_2)

        self.assertEqual(reverse_linked_list_recursive(create_linked_list(list_1)).get_list(), expected_1)
        self.assertEqual(reverse_linked_list_recursive(create_linked_list(list_2)).get_list(), expected_2)
    
    def test_use_property(self):
        user = User("John")
        self.assertEqual(user.username, "John")

    def test_read_env(self):
        self.assertEqual(environ(".env")["TEST"], "TEST")

if __name__ == '__main__':
    unittest.main()