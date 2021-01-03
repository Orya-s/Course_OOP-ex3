from unittest import TestCase

from DiGraph import DiGraph

from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        gra = "graph"
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(0, 1, 0.5)
        g.add_edge(0, 1, 0.5)
        g.add_edge(1, 0, 0.5)
        g.add_edge(5, 4, 0.5)
        g.add_edge(2, 1, 1.5)
        g.add_edge(2, 3, 2.5)
        g.add_edge(4, 1, 1.5)
        g.add_edge(5, 3, 3.5)
        # load_from_json("graph")

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
