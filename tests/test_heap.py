from algorithms.heap import (
    BinaryHeap,
    get_skyline,
    max_sliding_window,
    k_closest
)

import unittest


class TestBinaryHeap(unittest.TestCase):
    """
        Test suite for the binary_heap data structures
    """

    def setUp(self):
        self.min_heap = BinaryHeap()
        self.min_heap.insert(4)
        self.min_heap.insert(50)
        self.min_heap.insert(7)
        self.min_heap.insert(55)
        self.min_heap.insert(90)
        self.min_heap.insert(87)

    def test_insert(self):
        # Before insert 2: [0, 4, 50, 7, 55, 90, 87]
        # After insert:  [0, 2, 50, 4, 55, 90, 87, 7]
        self.min_heap.insert(2)
        self.assertEqual([0, 2, 50, 4, 55, 90, 87, 7],
                         self.min_heap.heap)
        self.assertEqual(7, self.min_heap.current_size)

    def test_remove_min(self):
        ret = self.min_heap.remove_min()
        # Before remove_min : [0, 4, 50, 7, 55, 90, 87]
        # After remove_min: [7, 50, 87, 55, 90]
        # Test return value
        self.assertEqual(4, ret)
        self.assertEqual([0, 7, 50, 87, 55, 90],
                         self.min_heap.heap)
        self.assertEqual(5, self.min_heap.current_size)

    #added 
    def SetUp(self):
        self.heap = BinaryHeap()
        for i in [20, 5, 15, 40, 10, 25]:
            self.heap.insert(i)

    # def test_heap_property_maintained(self):
    #     # Check if the smallest element is at the root for min-heap after multiple inserts
    #     self.assertEqual(self.heap.heap[1], min(self.heap.heap[1:]))
    #     self.heap.remove_min()
    #     # Check again after removing the minimum element
    #     self.assertEqual(self.heap.heap[1], min(self.heap.heap[1:]))

#added 
class TestSkylineEdgeCases(unittest.TestCase):
    def test_single_building(self):
        # Testing with a single building
        buildings = [[1, 5, 10]]
        self.assertEqual(get_skyline(buildings), [[1, 10], [5, 0]])

    def test_adjacent_buildings(self):
        # Testing with adjacent buildings of the same height
        buildings = [[2, 5, 10], [5, 8, 10]]
        self.assertEqual(get_skyline(buildings), [[2, 10], [8, 0]])
#added 
class TestMaxSlidingWindowEdgeCases(unittest.TestCase):
    def test_window_size_one(self):
        nums = [4, 3, 5, 2, 6]
        self.assertEqual(max_sliding_window(nums, 1), nums)

    def test_window_equals_array_length(self):
        nums = [4, 3, 5, 2, 6]
        self.assertEqual(max_sliding_window(nums, len(nums)), [6])
#added 
class TestKClosestPointsEdgeCases(unittest.TestCase):
    def test_points_with_same_distance(self):
        points = [(1, 2), (2, 1), (-1, -2), (-2, -1)]
        # Here, multiple points are at the same distance from origin
        self.assertEqual(sorted(k_closest(points, 2)), sorted([(1, 2), (2, 1)]))

    def test_all_points_when_k_equals_n(self):
        points = [(1, 3), (2, -1), (-1, 2), (-2, 1)]
        k = len(points)
        self.assertEqual(sorted(k_closest(points, k)), sorted(points))

class TestSuite(unittest.TestCase):
    def test_get_skyline(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                     [15, 20, 10], [19, 24, 8]]
        # Expect output
        output = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10],
                  [20, 8], [24, 0]]
        self.assertEqual(output, get_skyline(buildings))

    def test_max_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual([3, 3, 5, 5, 6, 7], max_sliding_window(nums, 3))

    def test_k_closest_points(self):
        points = [(1, 0), (2, 3), (5, 2), (1, 1), (2, 8), (10, 2),
                  (-1, 0), (-2, -2)]
        self.assertEqual([(-1, 0), (1, 0)], k_closest(points, 2))
        self.assertEqual([(1, 1), (-1, 0), (1, 0)], k_closest(points, 3))
        self.assertEqual([(-2, -2), (1, 1), (1, 0),
                          (-1, 0)], k_closest(points, 4))
        self.assertEqual([(10, 2), (2, 8), (5, 2), (-2, -2), (2, 3),
                          (1, 0), (-1, 0), (1, 1)], k_closest(points, 8))


if __name__ == "__main__":
    unittest.main()
