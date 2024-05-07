from algorithms.bfs import (
    count_islands,
    maze_search,
    ladder_length,
    shortest_distance_from_all_buildings
)

import unittest


class TestCountIslands(unittest.TestCase):

    def test_count_islands(self):
        grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        self.assertEqual(1, count_islands(grid_1))
        grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 1]]
        self.assertEqual(3, count_islands(grid_2))
        grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
        self.assertEqual(3, count_islands(grid_3))
        grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0]]
        self.assertEqual(5, count_islands(grid_4))


class TestMazeSearch(unittest.TestCase):

    def test_maze_search(self):
        grid_1 = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1, 1]]
        self.assertEqual(14, maze_search(grid_1))
        grid_2 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(-1, maze_search(grid_2))


class TestWordLadder(unittest.TestCase):

    def test_ladder_length(self):

        # hit -> hot -> dot -> dog -> cog
        self.assertEqual(5, ladder_length('hit', 'cog', ["hot", "dot", "dog",
                                          "lot", "log"]))

        # pick -> sick -> sink -> sank -> tank == 5
        self.assertEqual(5, ladder_length('pick', 'tank',
                                          ['tock', 'tick', 'sank', 'sink',
                                           'sick']))

        # live -> life == 1, no matter what is the word_list.
        self.assertEqual(1, ladder_length('live', 'life', ['hoho', 'luck']))

        # 0 length from ate -> ate
        self.assertEqual(0, ladder_length('ate', 'ate', []))

        # not possible to reach !
        self.assertEqual(-1, ladder_length('rahul', 'coder', ['blahh',
                                           'blhah']))

class TestShortestDistance(unittest.TestCase):

    def test_no_buildings(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(shortest_distance(grid), -1, "Should return -1 if no buildings are present")

    def test_no_empty_space(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(shortest_distance(grid), -1, "Should return -1 if there is no empty space")

    def test_single_building(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(shortest_distance(grid), 4, "Should return total distance to all reachable plots")

    def test_multiple_buildings(self):
        grid = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
        ]
        self.assertEqual(shortest_distance(grid), 7, "Should return minimum distance sum to all buildings")

    def test_unreachable_space(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        self.assertEqual(shortest_distance(grid), -1, "Should return -1 if a cell is unreachable")

    def test_large_grid(self):
        grid = [
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1]
        ]
        self.assertEqual(shortest_distance(grid), 18, "Should handle larger grids correctly")

    def test_edge_cases(self):
        grid = [[1]]
        self.assertEqual(shortest_distance(grid), -1, "Single building should result in -1")
        grid = [[0]]
        self.assertEqual(shortest_distance(grid), -1, "Single empty space should result in -1")
        
if __name__ == "__main__":
    unittest.main()
