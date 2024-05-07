from algorithms.bit import (
    add_bitwise_operator,
    count_ones_iter, count_ones_recur,
    count_flips_to_convert,
    find_missing_number, find_missing_number2,
    flip_bit_longest_seq,
    is_power_of_two,
    reverse_bits,
    single_number,
    single_number2,
    single_number3,
    subsets,
    get_bit, set_bit, clear_bit, update_bit,
    int_to_bytes_big_endian, int_to_bytes_little_endian,
    bytes_big_endian_to_int, bytes_little_endian_to_int,
    swap_pair,
    find_difference,
    has_alternative_bit, has_alternative_bit_fast,
    insert_one_bit, insert_mult_bits,
    remove_bit,
    binary_gap
)

import unittest
import random


class TestSuite(unittest.TestCase):

    def setUp(self):
        """Initialize seed."""
        random.seed("test")

    def test_add_bitwise_operator(self):
        self.assertEqual(5432 + 97823, add_bitwise_operator(5432, 97823))
        self.assertEqual(0, add_bitwise_operator(0, 0))
        self.assertEqual(10, add_bitwise_operator(10, 0))
        self.assertEqual(10, add_bitwise_operator(0, 10))

    def test_count_ones_recur(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_recur(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_recur(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_recur(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_recur(0))

    def test_count_ones_iter(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_iter(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_iter(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_iter(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_iter(0))

    def test_count_flips_to_convert(self):
        # 29: 11101 and 15: 01111
        self.assertEqual(2, count_flips_to_convert(29, 15))
        # 45: 0000101101 and 987: 1111011011
        self.assertEqual(8, count_flips_to_convert(45, 987))
        # 34: 100010
        self.assertEqual(0, count_flips_to_convert(34, 34))
        # 34: 100010 and 53: 110101
        self.assertEqual(4, count_flips_to_convert(34, 53))

    def test_find_missing_number(self):

        self.assertEqual(7, find_missing_number([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number([1]))
        self.assertEqual(1, find_missing_number([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number(nums))

    def test_find_missing_number2(self):

        self.assertEqual(7, find_missing_number2([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number2([1]))
        self.assertEqual(1, find_missing_number2([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number2(nums))

    def test_flip_bit_longest_seq(self):
        # 1775: 11011101111
        self.assertEqual(8, flip_bit_longest_seq(1775))
        # 5: 101
        self.assertEqual(3, flip_bit_longest_seq(5))
        # 71: 1000111
        self.assertEqual(4, flip_bit_longest_seq(71))
        # 0: 0
        self.assertEqual(1, flip_bit_longest_seq(0))

    def test_is_power_of_two(self):

        self.assertTrue(is_power_of_two(64))
        self.assertFalse(is_power_of_two(91))
        self.assertTrue(is_power_of_two(2**1001))
        self.assertTrue(is_power_of_two(1))
        self.assertFalse(is_power_of_two(0))

    def test_reverse_bits(self):

        self.assertEqual(43261596, reverse_bits(964176192))
        self.assertEqual(964176192, reverse_bits(43261596))
        self.assertEqual(1, reverse_bits(2147483648))

        # bin(0) => 00000000000000000000000000000000
        self.assertEqual(0, reverse_bits(0))

        # bin(2**32 - 1) => 11111111111111111111111111111111
        self.assertEqual(2**32 - 1, reverse_bits(2**32 - 1))

    def test_single_number(self):

        random.seed('test')

        self.assertEqual(0, single_number([1, 0, 2, 1, 2, 3, 3]))
        self.assertEqual(101, single_number([101]))

        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 2  # nums contains pairs of random integers
        nums.append(single)
        random.shuffle(nums)

        self.assertEqual(single, single_number(nums))

    def test_single_number2(self):

        self.assertEqual(3, single_number2([4, 2, 3, 2, 1, 1, 4, 2, 4, 1]))
        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 3  # nums contains triplets of random integers
        nums.append(single)
        random.shuffle(nums)
        self.assertEqual(single, single_number2(nums))

    def test_single_number3(self):
        self.assertEqual(sorted([2, 5]),
                         sorted(single_number3([2, 1, 5, 6, 6, 1])))
        self.assertEqual(sorted([4, 3]),
                         sorted(single_number3([9, 9, 4, 3])))

    def test_subsets(self):

        self.assertSetEqual(subsets([1, 2, 3]),
                            {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3),
                            (1, 2, 3)})

        self.assertSetEqual(subsets([10, 20, 30, 40]),
                            {(10, 40), (10, 20, 40), (10, 30),
                            (10, 20, 30, 40), (40,),
                             (10, 30, 40), (30,), (20, 30), (30, 40), (10,),
                             (),
                             (10, 20), (20, 40), (20, 30, 40), (10, 20, 30),
                             (20,)})

    def test_get_bit(self):
        # 22 = 10110
        self.assertEqual(1, get_bit(22, 2))
        self.assertEqual(0, get_bit(22, 3))

    def test_set_bit(self):
        # 22 = 10110  --> after set bit at 3th position: 30 = 11110
        self.assertEqual(30, set_bit(22, 3))

    def test_clear_bit(self):
        # 22 = 10110 --> after clear bit at 2nd position: 20 = 10010
        self.assertEqual(18, clear_bit(22, 2))

    def test_update_bit(self):
        # 22 = 10110 --> after update bit at 3th position with
        # value 1: 30 = 11110
        self.assertEqual(30, update_bit(22, 3, 1))
        # 22 = 10110 --> after update bit at 2nd position with
        # value 0: 20 = 10010
        self.assertEqual(18, update_bit(22, 2, 0))

    def test_int_to_bytes_big_endian(self):
        self.assertEqual(b'\x11', int_to_bytes_big_endian(17))

    def test_int_to_bytes_little_endian(self):
        self.assertEqual(b'\x11', int_to_bytes_little_endian(17))

    def test_bytes_big_endian_to_int(self):
        self.assertEqual(17, bytes_big_endian_to_int(b'\x11'))

    def test_bytes_little_endian_to_int(self):
        self.assertEqual(17, bytes_little_endian_to_int(b'\x11'))

    def test_swap_pair(self):
        # 22: 10110  --> 41: 101001
        self.assertEqual(41, swap_pair(22))
        # 10: 1010   --> 5 : 0101
        self.assertEqual(5, swap_pair(10))

    def test_find_difference(self):
        self.assertEqual('e', find_difference("abcd", "abecd"))

    def test_has_alternative_bit(self):
        self.assertTrue(has_alternative_bit(5))
        self.assertFalse(has_alternative_bit(7))
        self.assertFalse(has_alternative_bit(11))
        self.assertTrue(has_alternative_bit(10))

    def test_has_alternative_bit_fast(self):
        self.assertTrue(has_alternative_bit_fast(5))
        self.assertFalse(has_alternative_bit_fast(7))
        self.assertFalse(has_alternative_bit_fast(11))
        self.assertTrue(has_alternative_bit_fast(10))

    def test_insert_one_bit(self):
        """
        Input: num = 10101 (21)
        insert_one_bit(num, 1, 2): 101101 (45)
        insert_one_bit(num, 0 ,2): 101001 (41)
        insert_one_bit(num, 1, 5): 110101 (53)
        insert_one_bit(num, 1, 0): 101010 (42)
        """
        self.assertEqual(45, insert_one_bit(21, 1, 2))
        self.assertEqual(41, insert_one_bit(21, 0, 2))
        self.assertEqual(53, insert_one_bit(21, 1, 5))
        self.assertEqual(43, insert_one_bit(21, 1, 0))

    def test_insert_mult_bits(self):
        """
        Input: num = 101 (5)
        insert_mult_bits(num, 7, 3, 1): 101111 (47)
        insert_mult_bits(num, 7, 3, 0): 101111 (47)
        insert_mult_bits(num, 7, 3, 3): 111101 (61)
        """
        self.assertEqual(47, insert_mult_bits(5, 7, 3, 1))
        self.assertEqual(47, insert_mult_bits(5, 7, 3, 0))
        self.assertEqual(61, insert_mult_bits(5, 7, 3, 3))

    def test_remove_bit(self):
        """
        Input: num = 10101 (21)
        remove_bit(num, 2): output = 1001 (9)
        remove_bit(num, 4): output = 101 (5)
        remove_bit(num, 0): output = 1010 (10)
        """
        self.assertEqual(9, remove_bit(21, 2))
        self.assertEqual(5, remove_bit(21, 4))
        self.assertEqual(10, remove_bit(21, 0))

    def test_binary_gap(self):
        # 22 = 10110
        self.assertEqual(2, binary_gap(22))
        # 6 = 110
        self.assertEqual(1, binary_gap(6))
        # 8 = 1000
        self.assertEqual(0, binary_gap(8))
        # 145 = 10010001
        self.assertEqual(4, binary_gap(145))
    class EnhancedBitTests(unittest.TestCase):
    
    def test_count_ones_large_number(self):
        # Testing with a large number for count_ones_iter and count_ones_recur
        large_number = 2**30 - 1  # All bits set till 30th bit
        self.assertEqual(count_ones_iter(large_number), 30)
        self.assertEqual(count_ones_recur(large_number), 30)
        
    def test_flip_bit_all_ones(self):
        # Testing flip_bit_longest_seq with all ones
        all_ones = 2**10 - 1  # 1023, i.e., binary 1111111111
        self.assertEqual(flip_bit_longest_seq(all_ones), 11)  # flipping any 0 gives all ones
    
    def test_is_power_of_two_large_numbers(self):
        # Testing very large numbers
        self.assertTrue(is_power_of_two(2**1500))
        self.assertFalse(is_power_of_two(2**1500 - 1))
    
    def test_reverse_bits_non_trivial_patterns(self):
        # Non-trivial patterns for reverse_bits
        self.assertEqual(reverse_bits(0b10101010101010101010101010101010), 0b01010101010101010101010101010101)
        self.assertEqual(reverse_bits(0b11001100110011001100110011001100), 0b00110011001100110011001100110011)
    
    def test_single_number_no_single(self):
        # Test for single_number2 and single_number3 with no single occurrence
        self.assertRaises(ValueError, single_number2, [1, 2, 1, 2, 1, 2])
        self.assertRaises(ValueError, single_number3, [1, 2, 1, 2, 1, 2])
    
    def test_subsets_empty_set(self):
        # Testing subsets function for an empty set
        self.assertEqual(subsets([]), {()})
    
    def test_bit_operations_random_positions(self):
        # Test get_bit, set_bit, clear_bit, update_bit with random positions on a larger number
        num = random.randint(1, 2**20)
        pos = random.randint(0, 19)
        self.assertEqual(get_bit(set_bit(num, pos), pos), 1)
        self.assertEqual(get_bit(clear_bit(num, pos), pos), 0)
        self.assertEqual(get_bit(update_bit(num, pos, get_bit(num, pos)), pos), get_bit(num, pos))
    
    def test_int_to_bytes_conversion_max_values(self):
        # Converting maximum values for 32-bit and 64-bit integers
        max_32bit = 2**32 - 1
        max_64bit = 2**64 - 1
        self.assertEqual(bytes_big_endian_to_int(int_to_bytes_big_endian(max_32bit)), max_32bit)
        self.assertEqual(bytes_little_endian_to_int(int_to_bytes_little_endian(max_64bit)), max_64bit)
    
    def test_swap_pair_non_trivial_numbers(self):
        # Test swap_pair for non-trivial numbers
        self.assertEqual(swap_pair(0b10100101), 0b01011010)
        self.assertEqual(swap_pair(0b11110000), 0b11110000)  # Should handle even pairs without change

    def test_insert_and_remove_bit_complex_scenarios(self):
        # Testing complex scenarios for insert_one_bit and remove_bit
        num = 0b10100101
        self.assertEqual(remove_bit(insert_one_bit(num, 1, 3), 3), num)
        self.assertEqual(remove_bit(insert_one_bit(num, 0, 5), 5), num)

    def test_binary_gap_no_ones(self):
        # Binary gap tests for numbers without `1`s
        self.assertEqual(binary_gap(0), 0)
        self.assertEqual(binary_gap(2**32), 0)  # 2^32 is beyond the int range but conceptually applicable


if __name__ == '__main__':
    unittest.main()
