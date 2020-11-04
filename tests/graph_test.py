import unittest

from src.davil.graph import Graph


class TestPartitions(unittest.TestCase):

    def test_fish_pose(self):
        edges = [(0, 1),
                 (1, 2)]

        g = Graph(edges, True)
        assert g.num_nodes == 3

        path = g.breadth_first_search(0)
        assert path == [(0, 1), (1, 2)]

        path = g.breadth_first_search(1)
        assert path == [(1, 0), (1, 2)]

        path = g.breadth_first_search(2)
        assert path == [(2, 1), (1, 0)]

    def test_directed(self):
        edges = [(0, 1),
                 (1, 2),
                 (0, 2),
                 (1, 3)]

        g = Graph(edges, True)
        assert g.num_nodes == 4

        path = g.breadth_first_search(0)
        assert path == [(0, 1), (0, 2), (1, 3)]

    def test_undirected(self):
        edges = [(0, 1),
                 (1, 2),
                 (0, 2),
                 (1, 3)]

        g = Graph(edges, False)
        assert g.num_nodes == 4

        path = g.breadth_first_search(0)
        assert path == [(0, 1), (0, 2), (1, 3)]

        path = g.breadth_first_search(2)
        assert path == []

        path = g.breadth_first_search(1)
        assert path == [(1, 2), (1, 3)]


if __name__ == '__main__':
    unittest.main()
