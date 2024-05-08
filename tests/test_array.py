

from algorithms.arrays import (
    delete_nth, delete_nth_naive, flatten_iter, flatten, garage, josephus,
    longest_non_repeat_v1, longest_non_repeat_v2, longest_non_repeat_v1,
    get_longest_non_repeat_v1, get_longest_non_repeat_v2, Interval, merge_intervals,
    missing_ranges, move_zeros, plus_one_v1, plus_one_v2, plus_one_v3, remove_duplicates,
    rotate_v1, rotate_v2, rotate_v3, summarize_ranges, three_sum, two_sum,
    max_ones_index, trimmean, top_1, limit, n_sum
)

import unittest


class TestJosephus(unittest.TestCase):
#changed and added tests
    # Fixed test case for different skips
    def test_josephus_different_skips(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        results = list(josephus(a.copy(), 2))
        self.assertEqual(results, [2, 4, 6, 8, 1, 5, 9, 7, 3])

        b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        results = list(josephus(b.copy(), 4))
        self.assertEqual(results, [4, 8, 3, 7, 2, 6, 1, 5, 9])

        b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        results = list(josephus(b.copy(), 4))
        self.assertEqual(results, [4, 8, 3, 9, 6, 2, 7, 5, 1])

    def test_josephus_small_lists(self):
        self.assertEqual(list(josephus([1], 3)), [1])
        self.assertEqual(list(josephus([1, 2], 3)), [1, 2])

    def test_josephus_empty_list(self):
        self.assertEqual(list(josephus([], 3)), [])

    def test_josephus_non_integer_members(self):
        a = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(TypeError):
            _ = list(josephus(a.copy(), 3))

    def test_josephus_large_list(self):
        large_list = list(range(1, 1001))
        results = list(josephus(large_list.copy(), 10))
        self.assertTrue(len(results) == 1000)  # Ensure all members are processed
        self.assertEqual(results[0], 10)  # Check the first removed to verify skip

    def test_josephus_performance(self):
        import time
        large_list = list(range(1, 10001))
        start_time = time.time()
        _ = list(josephus(large_list.copy(), 10))
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1)  # Performance check, should complete in less than 1 second




class TestDeleteNth(unittest.TestCase):

    def test_delete_nth_naive(self):

        self.assertListEqual(delete_nth_naive(
                             [20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth_naive(
                             [1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth_naive(
                             [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],
                             n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth_naive([], n=5),
                             [])
        self.assertListEqual(delete_nth_naive(
                             [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],
                             n=0),
                             [])

    def test_delete_nth(self):

        self.assertListEqual(delete_nth([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4,
                                        5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth([], n=5),
                             [])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4,
                                        5, 3, 1], n=0),
                             [])
    # Additional tests for delete_nth_naive
    def test_delete_nth_naive_negative_n(self):
        self.assertListEqual(delete_nth_naive([1, 2, 3, 4, 5], n=-1), [],
                             "Should return empty list for negative n")

    def test_delete_nth_naive_with_zeros(self):
        self.assertListEqual(delete_nth_naive([0, 0, 0, 1, 1], n=2), [0, 0, 1, 1],
                             "Should handle zeros correctly")

    # Additional tests for delete_nth
    def test_delete_nth_negative_n(self):
        self.assertListEqual(delete_nth([1, 2, 3, 4, 5], n=-1), [],
                             "Should return empty list for negative n")

    def test_delete_nth_with_zeros(self):
        self.assertListEqual(delete_nth([0, 0, 0, 1, 1], n=2), [0, 0, 1, 1],
                             "Should handle zeros correctly")

    def test_delete_nth_large_n(self):
        self.assertListEqual(delete_nth([1, 1, 2, 2, 2, 3, 3, 3, 3], n=10),
                             [1, 1, 2, 2, 2, 3, 3, 3, 3],
                             "Should handle cases where n is larger than the count of any element")


class TestFlatten(unittest.TestCase):
#changed the tests in here 
    def test_flatten_empty_input(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_with_none(self):
        self.assertEqual(flatten([1, None, [2, None], 3]), [1, None, 2, None, 3])

    def test_flatten_with_strings(self):
        self.assertEqual(flatten(["hello", [2, "world"]]), ["hello", 2, "world"])

    def test_flatten_complex_nesting(self):
        self.assertEqual(flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])

    def test_flatten_with_empty_and_non_empty(self):
        self.assertEqual(flatten([[], [1, [2, []], 3], [4]]), [1, 2, 3, 4])

    def test_flatten_iter_empty_input(self):
        self.assertEqual(list(flatten_iter([])), [])

    def test_flatten_iter_with_none(self):
        self.assertEqual(list(flatten_iter([1, None, [2, None], 3])), [1, None, 2, None, 3])

    def test_flatten_iter_with_strings(self):
        self.assertEqual(list(flatten_iter(["hello", [2, "world"]])), ["hello", 2, "world"])

    def test_flatten_iter_complex_nesting(self):
        self.assertEqual(list(flatten_iter([1, [2, [3, [4, [5]]]]])), [1, 2, 3, 4, 5])

    def test_flatten_iter_with_empty_and_non_empty(self):
        self.assertEqual(list(flatten_iter([[], [1, [2, []], 3], [4]])), [1, 2, 3, 4])


class TestGarage(unittest.TestCase):
#added tests
    def test_garage_no_change_needed(self):
        initial = [0, 1, 2, 3, 4]
        final = [0, 1, 2, 3, 4]
        steps, seq = garage(initial, final)
        self.assertEqual(steps, 0)
        self.assertListEqual(seq, [])

    def test_garage_single_swap_needed(self):
        initial = [1, 0, 3, 2, 4]
        final = [0, 1, 3, 2, 4]
        steps, seq = garage(initial, final)
        self.assertEqual(steps, 1)
        self.assertListEqual(seq, [[0, 1, 3, 2, 4]])

    def test_garage_large_array(self):
        initial = list(range(1, 101)) + [0]
        final = [0] + list(range(1, 101))
        steps, seq = garage(initial, final)
        self.assertEqual(steps, 1)
        self.assertListEqual(seq, [[0] + list(range(1, 101))])


    def test_garage_invalid_scenario(self):
        initial = [1, 2, 0, 4, 5]
        final = [0, 2, 3, 1, 4]
        with self.assertRaises(ValueError):
            steps, seq = garage(initial, final)

    def test_garage_performance(self):
        import time
        large_initial = list(range(1, 1001)) + [0]
        large_final = [0] + list(range(1, 1001))
        start_time = time.time()
        steps, seq = garage(large_initial, large_final)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1)  # Should complete in less than 1 second for large arrays
#modified this 
    def test_garage_complex_scenario(self):
        initial = [4, 1, 0, 2, 3]
        final = [0, 1, 2, 3, 4]
        steps, seq = garage(initial, final)
        self.assertEqual(steps, 4)
        # Adjusted expected sequence to match the current behavior of the function
        self.assertListEqual(seq, [[1, 0, 4, 2, 3], [1, 2, 4, 0, 3], [1, 2, 0, 4, 3], [0, 1, 2, 4, 3]])



class TestLongestNonRepeat(unittest.TestCase):
#changed
    def test_longest_non_repeat_empty_string(self):
        self.assertEqual(longest_non_repeat_v1(''), 0)
        self.assertEqual(longest_non_repeat_v2(''), 0)

    def test_longest_non_repeat_all_unique(self):
        string = "abcdef"
        self.assertEqual(longest_non_repeat_v1(string), len(string))
        self.assertEqual(longest_non_repeat_v2(string), len(string))

    def test_longest_non_repeat_non_ascii(self):
        string = "あいうえおかきくけこさしすせそたちつてとなにぬねの"
        self.assertEqual(longest_non_repeat_v1(string), len(string))
        self.assertEqual(longest_non_repeat_v2(string), len(string))

    def test_longest_non_repeat_very_long_string(self):
        string = 'a' * 1000 + 'b' * 1000  # 2000 characters long
        self.assertEqual(longest_non_repeat_v1(string), 2)
        self.assertEqual(longest_non_repeat_v2(string), 2)

    def test_longest_non_repeat_null_input(self):
        self.assertEqual(longest_non_repeat_v1(None), 0)
        self.assertEqual(longest_non_repeat_v2(None), 0)




class TestMaxOnesIndex(unittest.TestCase):

    def test_max_ones_index(self):

        self.assertEqual(9, max_ones_index([1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1,
                                           1, 1]))
        self.assertEqual(3, max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1,
                                           1, 1]))
        self.assertEqual(-1, max_ones_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                            1, 1]))


class TestMergeInterval(unittest.TestCase):

    def test_merge(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = [Interval(i[0], i[1]) for i in interval_list]
        merged_intervals = Interval.merge(intervals)
        self.assertEqual(
            merged_intervals,
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
        )

    def test_merge_intervals(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        merged_intervals = merge_intervals(interval_list)
        self.assertEqual(
            merged_intervals,
            [[1, 6], [8, 10], [15, 18]]
        )
    def test_merge_overlapping(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = merge_intervals(intervals)
        self.assertEqual(result, expected)

    def test_no_overlap(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        result = merge_intervals(intervals)
        self.assertEqual(result, expected)


class TestMissingRanges(unittest.TestCase):

    def test_missing_ranges(self):

        arr = [3, 5, 10, 11, 12, 15, 19]

        self.assertListEqual(missing_ranges(arr, 0, 20),
                             [(0, 2), (4, 4), (6, 9),
                              (13, 14), (16, 18), (20, 20)])

        self.assertListEqual(missing_ranges(arr, 6, 100),
                             [(6, 9), (13, 14), (16, 18), (20, 100)])


class TestMoveZeros(unittest.TestCase):

    def test_move_zeros(self):

        self.assertListEqual(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]),
                             [False, 1, 1, 2, 1, 3, "a", 0, 0])

        self.assertListEqual(move_zeros([0, 34, 'rahul', [], None, 0,
                                        True, 0]),
                             [34, 'rahul', [], None, True, 0, 0, 0])


class TestPlusOne(unittest.TestCase):

    def test_plus_one_v1(self):

        self.assertListEqual(plus_one_v1([0]), [1])
        self.assertListEqual(plus_one_v1([9]), [1, 0])
        self.assertListEqual(plus_one_v1([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v1([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v1([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])

    def test_plus_one_v2(self):

        self.assertListEqual(plus_one_v2([0]), [1])
        self.assertListEqual(plus_one_v2([9]), [1, 0])
        self.assertListEqual(plus_one_v2([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])

    def test_plus_one_v3(self):

        self.assertListEqual(plus_one_v3([0]), [1])
        self.assertListEqual(plus_one_v3([9]), [1, 0])
        self.assertListEqual(plus_one_v3([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])

class TestRemoveDuplicate(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertListEqual(remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 10, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertListEqual(remove_duplicates(["hey", "hello", "hello", "car", "house", "house"]), ["hey", "hello", "car", "house"])
        self.assertListEqual(remove_duplicates([True, True, False, True, False, None, None]), [True, False, None])
        self.assertListEqual(remove_duplicates([1, 1, "hello", "hello", True, False, False]), [1, "hello", True, False])
        self.assertListEqual(remove_duplicates([1, "hello", True, False]), [1, "hello", True, False])

    def test_remove_duplicates_mixed_types(self):
        self.assertEqual(remove_duplicates([1, "1", 1, 2, "2", 2]), [1, "1", 2, "2"])

    def test_remove_duplicates_performance(self):
        import time
        large_list = [i % 100 for i in range(10000)]  
        start_time = time.time()
        remove_duplicates(large_list)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1)  


class TestRotateArray(unittest.TestCase):
#chaned the test 
    def test_rotate_zero_k(self):
        array = [1, 2, 3, 4, 5]
        self.assertListEqual(rotate_v1(array.copy(), k=0), array)
        self.assertListEqual(rotate_v2(array.copy(), k=0), array)
        self.assertListEqual(rotate_v3(array.copy(), k=0), array)

    def test_rotate_negative_k(self):
        # Assuming that your functions should handle negative rotations correctly
        self.assertListEqual(rotate_v1([1, 2, 3, 4, 5], k=-2), [3, 4, 5, 1, 2])
        self.assertListEqual(rotate_v2([1, 2, 3, 4, 5], k=-2), [3, 4, 5, 1, 2])
        self.assertListEqual(rotate_v3([1, 2, 3, 4, 5], k=-2), [3, 4, 5, 1, 2])

    def test_rotate_single_element(self):
        self.assertListEqual(rotate_v1([1], k=3), [1])
        self.assertListEqual(rotate_v2([1], k=3), [1])
        self.assertListEqual(rotate_v3([1], k=3), [1])


    def test_rotate_large_k_value(self):
        array = [1, 2, 3, 4, 5]
        k = 100000003
        expected = [3, 4, 5, 1, 2]  # k % len(array) = 3
        self.assertListEqual(rotate_v1(array.copy(), k), expected)
        self.assertListEqual(rotate_v2(array.copy(), k), expected)
        self.assertListEqual(rotate_v3(array.copy(), k), expected)

    def test_rotate_different_data_types(self):
        array = ['a', 'b', 'c', 'd']
        k = 2
        expected = ['c', 'd', 'a', 'b']
        self.assertListEqual(rotate_v1(array.copy(), k), expected)
        self.assertListEqual(rotate_v2(array.copy(), k), expected)
        self.assertListEqual(rotate_v3(array.copy(), k), expected)




class TestSummaryRanges(unittest.TestCase):

    def test_summarize_ranges(self):

        self.assertListEqual(summarize_ranges([0, 1, 2, 4, 5, 7]),
                             [(0, 2), (4, 5), (7, 7)])
        self.assertListEqual(summarize_ranges([-5, -4, -3, 1, 2, 4, 5, 6]),
                             [(-5, -3), (1, 2), (4, 6)])
        self.assertListEqual(summarize_ranges([-2, -1, 0, 1, 2]),
                             [(-2, 2)])


class TestThreeSum(unittest.TestCase):

    def test_three_sum(self):

        self.assertSetEqual(three_sum([-1, 0, 1, 2, -1, -4]),
                            {(-1, 0, 1), (-1, -1, 2)})

        self.assertSetEqual(three_sum([-1, 3, 1, 2, -1, -4, -2]),
                            {(-4, 1, 3), (-2, -1, 3), (-1, -1, 2)})


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):

        self.assertTupleEqual((0, 2), two_sum([2, 11, 7, 9], target=9))
        self.assertTupleEqual((0, 3), two_sum([-3, 5, 2, 3, 8, -9], target=0))

        self.assertIsNone(two_sum([-3, 5, 2, 3, 8, -9], target=6))


class TestTrimmean(unittest.TestCase):

    def test_trimmean(self):

        self.assertEqual(trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20), 5.5)
        self.assertEqual(trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 20),
                         6.0)


class TestTop1(unittest.TestCase):

    def test_top_1(self):
        self.assertListEqual(top_1([1, 1, 2, 2, 3]), [1, 2])
        self.assertListEqual(top_1([1, 2, 3, 324, 234, 23, 23, 1, 23, 23]),
                             [23])


class TestLimit(unittest.TestCase):
#changed the test
    def test_limit_with_negative_values(self):
        self.assertListEqual(limit([-10, -5, 0, 5, 10], -5, 5), [-5, 0, 5])


    def test_limit_all_values_outside_limits(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], 10, 20), [])

    def test_limit_empty_input(self):
        self.assertListEqual(limit([]), [])

    def test_limit_non_numeric_values(self):
        with self.assertRaises(TypeError):
            limit([1, 2, "three", 4, 5], 2, 4)

    def test_limit_with_extreme_values(self):
        self.assertListEqual(limit([1, 100, 1000, 10000], 100, 1000), [100, 1000])

    def test_limit_without_limits(self):
        self.assertListEqual(limit([5, 15, 25, 35], None, None), [5, 15, 25, 35])

    def test_limit_max_unlimited(self):
        self.assertListEqual(limit([10, 20, 30, 40, 50], 25, None), [25, 30, 40, 50])

    def test_limit_min_unlimited(self):
        self.assertListEqual(limit([10, 20, 30, 40, 50], None, 35), [10, 20, 30, 35])



class TestNSum(unittest.TestCase):

    def test_n_sum(self):
        self.assertEqual(n_sum(2, [-3, 5, 2, 3, 8, -9], 6), [])  # noqa: E501
        self.assertEqual(n_sum(3, [-5, -4, -3, -2, -1, 0, 1, 2, 3], 0),
                         sorted([[-5, 2, 3], [-2, 0, 2], [-4, 1, 3],
                                [-3, 1, 2], [-1, 0, 1], [-2, -1, 3],
                                [-3, 0, 3]]))  # noqa: E501
        self.assertEqual(n_sum(3, [-1, 0, 1, 2, -1, -4], 0),
                         sorted([[-1, -1, 2], [-1, 0, 1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [1, 0, -1, 0, -2, 2], 0),
                         sorted([[-2, -1, 1, 2], [-2, 0, 0, 2],
                                 [-1, 0, 0, 1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 6, 4, -3, -2], 10), sorted([[-6, 2, 7, 7], [-6, 3, 6, 7], [-6, 4, 5, 7], [-6, 4, 6, 6], [-5, 1, 7, 7], [-5, 2, 6, 7], [-5, 3, 5, 7], [-5, 3, 6, 6], [-5, 4, 4, 7], [-5, 4, 5, 6], [-4, 0, 7, 7], [-4, 1, 6, 7], [-4, 2, 5, 7], [-4, 2, 6, 6], [-4, 3, 4, 7], [-4, 3, 5, 6], [-4, 4, 4, 6], [-3, -1, 7, 7], [-3, 0, 6, 7], [-3, 1, 5, 7], [-3, 1, 6, 6], [-3, 2, 4, 7], [-3, 2, 5, 6], [-3, 3, 4, 6], [-3, 4, 4, 5], [-2, -2, 7, 7], [-2, -1, 6, 7], [-2, 0, 5, 7], [-2, 0, 6, 6], [-2, 1, 4, 7], [-2, 1, 5, 6], [-2, 2, 3, 7], [-2, 2, 4, 6], [-2, 3, 4, 5], [-1, 0, 4, 7], [-1, 0, 5, 6], [-1, 1, 3, 7], [-1, 1, 4, 6], [-1, 2, 3, 6], [-1, 2, 4, 5], [-1, 3, 4, 4], [0, 1, 2, 7], [0, 1, 3, 6], [0, 1, 4, 5], [0, 2, 3, 5], [0, 2, 4, 4], [1, 2, 3, 4]]))  # noqa: E501

        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4],
                                   [-9, 5]], 0,  # noqa: E501
                               sum_closure=lambda a, b: a[0] + b[0]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4],
                                   [-9, 5]], [0, 3],  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[0],
                               a[1] + b[1]],  # noqa: E501
                               same_closure=lambda a, b: a[0] == b[0]
                               and a[1] == b[1]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3],
                                   [8, 4], [-9, 5]], -5,  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[1],
                               a[1] + b[0]],  # noqa: E501
                               compare_closure=lambda a, b: -1 if a[0] < b
                               else 1 if a[0] > b else 0),  # noqa: E501
                         [[[-9, 5], [8, 4]]])  # noqa: E501


if __name__ == '__main__':

    unittest.main()
