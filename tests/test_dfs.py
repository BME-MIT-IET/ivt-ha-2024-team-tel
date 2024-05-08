from algorithms.dfs import (
    get_factors, get_factors_iterative1, get_factors_iterative2,
    num_islands,
    pacific_atlantic,
    Sudoku,
    walls_and_gates,
    find_path
)

import unittest


class TestAllFactors(unittest.TestCase):
    def test_get_factors(self):
        self.assertEqual([[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2],
                         [2, 4, 4], [4, 8]], get_factors(32))

    def test_get_factors_iterative1(self):
        self.assertEqual([[2, 16], [4, 8], [2, 2, 8], [2, 4, 4], [2, 2, 2, 4],
                          [2, 2, 2, 2, 2]], get_factors_iterative1(32))

    def test_get_factors_iterative2(self):
        self.assertEqual([[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 8], [2, 4, 4],
                          [2, 16], [4, 8]], get_factors_iterative2(32))
    #added
    def test_get_factors_zero(self):
        self.assertEqual([], get_factors(0))

    def test_get_factors_one(self):
        self.assertEqual([], get_factors(1))

    def test_get_factors_prime(self):
        self.assertEqual([], get_factors(13))

class TestCountIslands(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(1, num_islands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0],
                                         [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
        self.assertEqual(3, num_islands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                                         [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]))
    #added
    def test_num_islands_empty(self):
        self.assertEqual(0, num_islands([]))

    def test_num_islands_all_water(self):
        self.assertEqual(0, num_islands([[0, 0], [0, 0]]))

    def test_num_islands_all_land(self):
        self.assertEqual(1, num_islands([[1, 1], [1, 1]]))


class TestPacificAtlantic(unittest.TestCase):
    def test_pacific_atlantic(self):
        self.assertEqual([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0],
                          [3, 1], [4, 0]], pacific_atlantic([[1, 2, 2, 3, 5],
                                                            [3, 2, 3, 4, 4],
                                                            [2, 4, 5, 3, 1],
                                                            [6, 7, 1, 4, 5],
                                                            [5, 1, 1, 2, 4]]))
    #added 
    def test_pacific_atlantic_empty(self):
        self.assertEqual([], pacific_atlantic([]))

    def test_pacific_atlantic_single(self):
        self.assertEqual([[0, 0]], pacific_atlantic([[7]]))


class TestSudoku(unittest.TestCase):
    def test_sudoku_solver(self):
        board = [["5", "3", "."], ["6", ".", "."], [".", "9", "8"]]
        test_obj = Sudoku(board, 3, 3)
        test_obj.solve()
        self.assertEqual([['5', '3', '1'], ['6', '1', '2'],
                         ['1', '9', '8']], test_obj.board)



class TestWallsAndGates(unittest.TestCase):
    def test_walls_and_gates(self):
        rooms = [[float("inf"), -1, 0, float("inf")],
                 [float("inf"), float("inf"), float("inf"), -1],
                 [float("inf"), -1, float("inf"), -1],
                 [0, -1, float("inf"), float("inf")]]
        walls_and_gates(rooms)
        self.assertEqual([[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1],
                          [0, -1, 3, 4]], rooms)
    #added 
    def test_walls_and_gates_only_walls(self):
        rooms = [[-1, -1], [-1, -1]]
        expected = [[-1, -1], [-1, -1]]
        walls_and_gates(rooms)
        self.assertEqual(expected, rooms)

    def test_walls_and_gates_no_gates(self):
        rooms = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        expected = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        walls_and_gates(rooms)
        self.assertEqual(expected, rooms)


class TestMazeSearch(unittest.TestCase):
    def test_maze_search(self):
        maze_1 = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
                   1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
                   0, 1, 1, 1, 0, 1]]
        self.assertEqual(37, find_path(maze_1))
        maze_2 = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
        self.assertEqual(14, find_path(maze_2))
        maze_3 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(-1, find_path(maze_3))
    #added 
    def test_maze_search_complex(self):
        maze = [[1, 0, 0, 1], [1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 0]]
        self.assertEqual(6, find_path(maze))  # Assuming path finding works correctly

    def test_maze_search_blocked(self):
        maze = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
        self.assertEqual(-1, find_path(maze))  # No path


if __name__ == "__main__":
    unittest.main()
