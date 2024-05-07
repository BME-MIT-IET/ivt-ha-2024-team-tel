from algorithms.greedy import (
    max_contiguous_subsequence_sum,
)

import unittest

class TestMaxContiguousSubsequenceSum(unittest.TestCase):
    def test_max_contiguous_subsequence_sum(self):
        arr1 = [-2, 3, 8, -1, 4]
        arr2 = [-1, 1, 0]
        arr3 = [-1, -3, -4]
        arr4 = [-2, 3, 8, -12, 8, 4]

        self.assertEqual(max_contiguous_subsequence_sum(arr1), 14)
        self.assertEqual(max_contiguous_subsequence_sum(arr2), 1)
        self.assertEqual(max_contiguous_subsequence_sum(arr3), -1)
        self.assertEqual(max_contiguous_subsequence_sum(arr4), 12)

    #added 
    def test_empty_array(self):
        self.assertEqual(max_contiguous_subsequence_sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(max_contiguous_subsequence_sum([5]), 5)
        self.assertEqual(max_contiguous_subsequence_sum([-5]), -5)

    def test_all_positive_elements(self):
        self.assertEqual(max_contiguous_subsequence_sum([1, 2, 3, 4, 5]), 15)

    def test_all_zero_elements(self):
        self.assertEqual(max_contiguous_subsequence_sum([0, 0, 0, 0]), 0)

    def test_all_negative_elements(self):
        self.assertEqual(max_contiguous_subsequence_sum([-1, -2, -3, -4]), -1)
if __name__ == '__main__':

    unittest.main()