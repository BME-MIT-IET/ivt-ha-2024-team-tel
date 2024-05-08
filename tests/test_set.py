from algorithms.set import (
    find_keyboard_row,RandomizedSet,set_covering 
)

import unittest


class TestFindKeyboardRow(unittest.TestCase):
    def test_find_keyboard_row(self):
        # Test with given example
        self.assertEqual(["Alaska", "Dad"],
                         find_keyboard_row(["Hello", "Alaska", "Dad", "Peace"]))
    
    def test_all_one_row(self):
        # Test where all words can be typed on one row
        self.assertEqual(["Alaska", "Dad", "Qwerty"],
                         find_keyboard_row(["Alaska", "Dad", "Qwerty", "Peace"]))

    def test_no_words_one_row(self):
        # Test where no words can be typed on one row
        self.assertEqual([],
                         find_keyboard_row(["Hello", "World", "Peace"]))
    
    def test_mixed_case(self):
        # Test with mixed case words
        self.assertEqual(["Alaska", "Dad"],
                         find_keyboard_row(["HeLLo", "AlAsKa", "DaD", "PeAcE"]))
    
    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual([], find_keyboard_row([]))
    
    def test_uppercase_words(self):
        # Test with uppercase words that belong to one row
        self.assertEqual(["QWERTY", "ASDFG", "ZXCVB"],
                         find_keyboard_row(["QWERTY", "ASDFG", "ZXCVB", "HELLO"]))
    
    def test_lowercase_words(self):
        # Test with lowercase words that belong to one row
        self.assertEqual(["qwerty", "asdfg", "zxcvb"],
                         find_keyboard_row(["qwerty", "asdfg", "zxcvb", "hello"]))
        
class TestRandomizedSet(unittest.TestCase):
    def setUp(self):
        self.random_set = RandomizedSet()

    def test_insert(self):
        self.assertIsNone(self.random_set.insert(1))
        self.assertIn(1, self.random_set.elements)
        self.assertEqual(len(self.random_set.elements), 1)

        self.assertIsNone(self.random_set.insert(2))
        self.assertIn(2, self.random_set.elements)
        self.assertEqual(len(self.random_set.elements), 2)

        self.assertIsNone(self.random_set.insert(1))  # Duplicate insert
        self.assertEqual(len(self.random_set.elements), 2)  # Length should not change

    def test_remove(self):
        self.random_set.insert(1)
        self.random_set.insert(2)

        self.assertIsNone(self.random_set.remove(1))
        self.assertNotIn(1, self.random_set.elements)
        self.assertEqual(len(self.random_set.elements), 1)

        self.assertIsNone(self.random_set.remove(2))
        self.assertNotIn(2, self.random_set.elements)
        self.assertEqual(len(self.random_set.elements), 0)

        self.assertIsNone(self.random_set.remove(3))  # Removing non-existent element

    def test_random_element(self):
        self.random_set.insert(1)
        self.random_set.insert(2)
        self.random_set.insert(3)

        elements = set()
        for _ in range(100):
            elements.add(self.random_set.random_element())

        self.assertTrue(elements.issubset({1, 2, 3}))
        self.assertEqual(len(elements), 3)

    def test_combined_operations(self):
        self.random_set.insert(1)
        self.random_set.insert(2)
        self.random_set.insert(3)
        self.random_set.remove(2)

        self.assertNotIn(2, self.random_set.elements)
        self.assertEqual(len(self.random_set.elements), 2)

        remaining_elements = {self.random_set.elements[self.random_set.index_map[i]] for i in self.random_set.index_map}
        self.assertTrue(remaining_elements.issubset({1, 3}))

class TestSetCovering(unittest.TestCase):
    def setUp(self):
        self.universe = {1, 2, 3, 4, 5}
        self.subsets = {
            'S1': {4, 1, 3},
            'S2': {2, 5},
            'S3': {1, 4, 3, 2}
        }
        self.costs = {
            'S1': 5,
            'S2': 10,
            'S3': 3
        }

    def test_optimal_set_cover(self):
        optimal_cover = set_covering.optimal_set_cover(self.universe, self.subsets, self.costs)
        optimal_cost = sum(self.costs[s] for s in optimal_cover)

        self.assertEqual(set(optimal_cover), {'S3'})
        self.assertEqual(optimal_cost, 3)

    def test_greedy_set_cover(self):
        greedy_cover = set_covering.greedy_set_cover(self.universe, self.subsets, self.costs)
        greedy_cost = sum(self.costs[s] for s in greedy_cover)

        self.assertEqual(set(greedy_cover), {'S3'})
        self.assertEqual(greedy_cost, 3)

    def test_partial_cover(self):
        universe = {1, 2, 3, 4, 5, 6}
        subsets = {
            'S1': {1, 2, 3},
            'S2': {4, 5},
            'S3': {1, 4, 6},
            'S4': {3, 6}
        }
        costs = {
            'S1': 6,
            'S2': 5,
            'S3': 4,
            'S4': 3
        }

        optimal_cover = set_covering.optimal_set_cover(universe, subsets, costs)
        optimal_cost = sum(costs[s] for s in optimal_cover)
        self.assertEqual(set(optimal_cover), {'S3', 'S4'})
        self.assertEqual(optimal_cost, 7)

        greedy_cover = set_covering.greedy_set_cover(universe, subsets, costs)
        greedy_cost = sum(costs[s] for s in greedy_cover)
        self.assertEqual(set(greedy_cover), {'S3', 'S4'})
        self.assertEqual(greedy_cost, 7)

    def test_disjoint_sets(self):
        universe = {1, 2, 3, 4}
        subsets = {
            'S1': {1},
            'S2': {2},
            'S3': {3},
            'S4': {4}
        }
        costs = {
            'S1': 1,
            'S2': 1,
            'S3': 1,
            'S4': 1
        }

        optimal_cover = set_covering.optimal_set_cover(universe, subsets, costs)
        optimal_cost = sum(costs[s] for s in optimal_cover)
        self.assertEqual(set(optimal_cover), {'S1', 'S2', 'S3', 'S4'})
        self.assertEqual(optimal_cost, 4)

        greedy_cover = set_covering.greedy_set_cover(universe, subsets, costs)
        greedy_cost = sum(costs[s] for s in greedy_cover)
        self.assertEqual(set(greedy_cover), {'S1', 'S2', 'S3', 'S4'})
        self.assertEqual(greedy_cost, 4)

    def test_empty_universe(self):
        universe = set()
        subsets = {
            'S1': {1, 2, 3},
            'S2': {4, 5}
        }
        costs = {
            'S1': 6,
            'S2': 5
        }

        optimal_cover = set_covering.optimal_set_cover(universe, subsets, costs)
        self.assertEqual(optimal_cover, [])

        greedy_cover = set_covering.greedy_set_cover(universe, subsets, costs)
        self.assertEqual(greedy_cover, [])
        
if __name__ == '__main__':
    unittest.main()