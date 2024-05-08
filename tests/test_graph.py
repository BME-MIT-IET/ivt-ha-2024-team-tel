from algorithms.graph import Tarjan
from algorithms.graph import check_bipartite
from algorithms.graph.dijkstra import Dijkstra
from algorithms.graph import ford_fulkerson
from algorithms.graph import edmonds_karp
from algorithms.graph import dinic
from algorithms.graph import maximum_flow_bfs
from algorithms.graph import maximum_flow_dfs
from algorithms.graph import all_pairs_shortest_path
from algorithms.graph import bellman_ford
from algorithms.graph import count_connected_number_of_component
from algorithms.graph import prims_minimum_spanning
from algorithms.graph import check_digraph_strongly_connected
from algorithms.graph import cycle_detection
from algorithms.graph import find_path
from algorithms.graph import path_between_two_vertices_in_digraph
from algorithms.graph import strongly_connected_components_kosaraju
from algorithms.graph import Node
from algorithms.graph import clone_graph
from algorithms.graph import count_connected_components
from algorithms.graph import find_all_cliques

import unittest
#added 
class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned_graph = clone_graph(node1)
        self.assertNotEqual(id(node1), id(cloned_graph))
        self.assertNotEqual(id(node1.neighbors[0]), id(cloned_graph.neighbors[0]))
        self.assertEqual(node1.val, cloned_graph.val)
class TestCountConnectedComponents(unittest.TestCase):
    def test_disconnected_graph(self):
        graph = [
            [1],  # Node 0 is connected to Node 1
            [0],  # Node 1 is connected to Node 0
            [],   # Node 2 is isolated
            []    # Node 3 is isolated
        ]
        self.assertEqual(count_connected_components(graph), 3)  # Expecting three components

class TestFindAllCliques(unittest.TestCase):
    def test_fully_connected_graph(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [1, 2, 3]
        }
        self.assertEqual(find_all_cliques(graph), [[1, 2, 3, 4]])
        
class TestAllPairsShortestPath(unittest.TestCase):
    def test_negative_weights(self):
        graph = [
            [0, -1, 4],
            [float('inf'), 0, 3],
            [float('inf'), float('inf'), 0]
        ]
        result = all_pairs_shortest_path(graph)
        expected = [
            [0, -1, 2],
            [float('inf'), 0, 3],
            [float('inf'), float('inf'), 0]
        ]
        self.assertEqual(result, expected)

class TestTarjan(unittest.TestCase):
    """
    Test for the file tarjan.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_tarjan_example_1(self):
        # Graph from https://en.wikipedia.org/wiki/File:Scc.png
        example = {
            'A': ['B'],
            'B': ['C', 'E', 'F'],
            'C': ['D', 'G'],
            'D': ['C', 'H'],
            'E': ['A', 'F'],
            'F': ['G'],
            'G': ['F'],
            'H': ['D', 'G']
        }

        g = Tarjan(example)
        self.assertEqual(g.sccs, [['F', 'G'], ['C', 'D', 'H'],
                                  ['A', 'B', 'E']])

    def test_tarjan_example_2(self):
        # Graph from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm#/media/File:Tarjan%27s_Algorithm_Animation.gif
        example = {
            'A': ['E'],
            'B': ['A'],
            'C': ['B', 'D'],
            'D': ['C'],
            'E': ['B'],
            'F': ['B', 'E', 'G'],
            'G': ['F', 'C'],
            'H': ['G', 'H', 'D']
        }

        g = Tarjan(example)
        self.assertEqual(g.sccs, [['A', 'B', 'E'], ['C', 'D'], ['F', 'G'],
                                  ['H']])


class TestCheckBipartite(unittest.TestCase):
    def test_check_bipartite(self):
        adj_list_1 = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
        self.assertEqual(True, check_bipartite(adj_list_1))
        adj_list_2 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        self.assertEqual(True, check_bipartite(adj_list_2))
        adj_list_3 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        self.assertEqual(False, check_bipartite(adj_list_3))


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        g = Dijkstra(9)
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]]

        self.assertEqual(g.dijkstra(0), [0, 4, 12, 19, 21, 11, 9, 8, 14])
        #added
    def test_empty_graph(self):
        g = Dijkstra(0)
        self.assertEqual(g.dijkstra(0), [])


class TestMaximumFlow(unittest.TestCase):
    """
    Test for the file maximum_flow.py

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_ford_fulkerson(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, ford_fulkerson(capacity, 0, 6))

    def test_edmonds_karp(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, edmonds_karp(capacity, 0, 6))

    def dinic(self):
        capacity = [
                [0, 10, 10, 0, 0, 0, 0],
                [0, 0, 2, 0, 4, 8, 0],
                [0, 0, 0, 0, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 6, 0, 10],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        self.assertEqual(19, dinic(capacity, 0, 6))


class TestMaximum_Flow_Bfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_bfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    def test_maximum_flow_bfs(self):
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]
        maximum_flow = maximum_flow_bfs(graph)

        self.assertEqual(maximum_flow, 23)


class TestMaximum_Flow_Dfs(unittest.TestCase):

    """
    Test for the file def maximum_flow_dfs.py
    Arguments:
        unittest {[type]} -- [description]
    """
    def test_maximum_flow_dfs(self):
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]
        maximum_flow = maximum_flow_dfs(graph)

        self.assertEqual(maximum_flow, 23)


class TestAll_Pairs_Shortest_Path(unittest.TestCase):
    def test_all_pairs_shortest_path(self):
        graph = [[0, 0.1, 0.101, 0.142, 0.277],
                 [0.465, 0, 0.191, 0.192, 0.587],
                 [0.245, 0.554, 0, 0.333, 0.931],
                 [1.032, 0.668, 0.656, 0, 0.151],
                 [0.867, 0.119, 0.352, 0.398, 0]]
        result = all_pairs_shortest_path(graph)

        self.assertEqual(result, [
                                    [0, 0.1, 0.101, 0.142, 0.277],
                                    [0.436, 0, 0.191, 0.192,
                                     0.34299999999999997],
                                    [0.245, 0.345, 0, 0.333, 0.484],
                                    [0.706, 0.27, 0.46099999999999997, 0,
                                     0.151],
                                    [0.5549999999999999, 0.119, 0.31, 0.311,
                                     0],
                                ])


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        graph1 = {
            'a': {'b': 6, 'e': 7},
            'b': {'c': 5, 'd': -4, 'e': 8},
            'c': {'b': -2},
            'd': {'a': 2, 'c': 7},
            'e': {'b': -3}
        }
        self.assertEqual(True, bellman_ford(graph1, 'a'))
        graph2 = {
            'a': {'d': 3, 'e': 4},
            'b': {'a': 7, 'e': 2},
            'c': {'a': 12, 'd': 9, 'e': 11},
            'd': {'c': 5, 'e': 11},
            'e': {'a': 7, 'b': 5, 'd': 1}
        }
        self.assertEqual(True, bellman_ford(graph2, 'a'))


class TestConnectedComponentInGraph(unittest.TestCase):
    """
     Class for testing different cases for connected components in graph
    """
    def test_count_connected_components(self):
        """
           Test Function that test the different cases of count connected
           components
            2----------0    1--------5      3
            |
            |
            4
                output = 3
        """
        expected_result = 3
        # adjacency list representation of graph
        l = [[2],
             [5],
             [0,4],
             [],
             [2],
             [1]]

        size = 5
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)

    def test_connected_components_with_empty_graph(self):

        """
            input :
            output : 0
        """
        l = [[]]
        expected_result = 0
        size = 0
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)

    def test_connected_components_without_edges_graph(self):
        """
          input : 0          2             3          4
          output : 4
        """
        l = [[0], [], [2], [3], [4]]
        size = 4
        expected_result = 4
        result = count_connected_number_of_component.count_components(l, size)
        self.assertEqual(result, expected_result)


class PrimsMinimumSpanning(unittest.TestCase):
    def test_prim_spanning(self):
        graph1 = {
            1: [[3, 2], [8, 3]],
            2: [[3, 1], [5, 4]],
            3: [[8, 1], [2, 4], [4, 5]],
            4: [[5, 2], [2, 3], [6, 5]],
            5: [[4, 3], [6, 4]]
        }
        self.assertEqual(14, prims_minimum_spanning(graph1))
        graph2 = {
            1: [[7, 2], [6, 4]],
            2: [[7, 1], [9, 4], [6, 3]],
            3: [[8, 4], [6, 2]],
            4: [[6, 1], [9, 2], [8, 3]]
        }
        self.assertEqual(19, prims_minimum_spanning(graph2))

class TestDigraphStronglyConnected(unittest.TestCase):
    def test_digraph_strongly_connected(self):
        g1 = check_digraph_strongly_connected.Graph(5)
        g1.add_edge(0, 1)
        g1.add_edge(1, 2)
        g1.add_edge(2, 3)
        g1.add_edge(3, 0)
        g1.add_edge(2, 4)
        g1.add_edge(4, 2)
        self.assertTrue(g1.is_strongly_connected())

        g2 = check_digraph_strongly_connected.Graph(4)
        g2.add_edge(0, 1)
        g2.add_edge(1, 2)
        g2.add_edge(2, 3)
        self.assertFalse(g2.is_strongly_connected())

class TestCycleDetection(unittest.TestCase):
    def test_cycle_detection_with_cycle(self):
        graph = {'A': ['B', 'C'],
                 'B': ['D'],
                 'C': ['F'],
                 'D': ['E', 'F'],
                 'E': ['B'],
                 'F': []}
        self.assertTrue(cycle_detection.contains_cycle(graph))

    def test_cycle_detection_with_no_cycle(self):
        graph = {'A': ['B', 'C'],
                 'B': ['D', 'E'],
                 'C': ['F'],
                 'D': ['E'],
                 'E': [],
                 'F': []}
        self.assertFalse(cycle_detection.contains_cycle(graph))
        #added
    def test_acyclic_graph(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        self.assertFalse(contains_cycle(graph))

class TestFindPath(unittest.TestCase):
    def test_find_all_paths(self):
        graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D', 'F'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}

        paths = find_path.find_all_path(graph, 'A', 'F')
        print(paths)
        self.assertEqual(sorted(paths), sorted([
            ['A', 'C', 'F'],
            ['A', 'B', 'C', 'F'],
            ['A', 'B', 'D', 'C', 'F'],
        ]))

class TestPathBetweenTwoVertices(unittest.TestCase):
    def test_node_is_reachable(self):
        g = path_between_two_vertices_in_digraph.Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        self.assertTrue(g.is_reachable(1, 3))
        self.assertFalse(g.is_reachable(3, 1))

class TestStronglyConnectedComponentsKosaraju(unittest.TestCase):
    def test_kosaraju_algorithm(self):
        V = 6
        adj = [
            [2],
            [0],
            [3],
            [1, 4],
            [5],
            [4]
        ]

        result = strongly_connected_components_kosaraju.Kosaraju().kosaraju(V, adj)

        # Expected result: 2 strongly connected components
        self.assertEqual(result, 2)
