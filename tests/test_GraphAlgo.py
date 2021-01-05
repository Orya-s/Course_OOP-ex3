from unittest import TestCase
from paintGraph import *
from DiGraph import DiGraph

from GraphAlgo import GraphAlgo


def createGraph():
    g = DiGraph()
    g.add_node(0, (32, 30, 6))
    g.add_node(1, (22, 43))
    g.add_node(2, (50, 50))
    g.add_node(3, (52, 13))
    g.add_node(4, (52, 33))
    g.add_node(5, (12, 33))
    g.add_node(6, (1, 2))
    g.add_edge(0, 1, 0.5)
    g.add_edge(5, 1, 0.5)
    g.add_edge(1, 0, 0.5)
    g.add_edge(5, 4, 0.5)
    g.add_edge(2, 1, 1.5)
    g.add_edge(2, 3, 2.5)
    g.add_edge(4, 1, 1.5)
    g.add_edge(5, 3, 3.5)
    g.add_edge(3, 5, 4)
    g.add_edge(4, 2, 6)
    g.add_edge(1, 2, 0.5)

    return g


class TestGraphAlgo(TestCase):
    def test_load_and_save_from_json(self):
        graph = createGraph()
        ga = GraphAlgo(graph)
        fileName = "g.json"
        ga.save_to_json(fileName)
        ga.load_from_json(fileName)
        self.assertTrue(graph.__eq__(ga.graph))

    def test_shortest_path(self):
        graph = createGraph()
        ga = GraphAlgo(graph)
        self.assertEqual((2.0, [4, 1, 2]), ga.shortest_path(4, 2))
        self.assertEqual((0.5, [0, 1]), ga.shortest_path(0, 1))
        self.assertEqual((3.5, [0, 1, 2, 3]), ga.shortest_path(0, 3))

    def test_connected_component(self):
        graph = createGraph()
        ga = GraphAlgo(graph)
        list = [graph.getNode(6)]
        self.assertEqual(list, ga.connected_component(6))
        list.clear()
        list.append(graph.getNode(0))
        list.append(graph.getNode(1))
        list.append(graph.getNode(2))
        list.append(graph.getNode(3))
        list.append(graph.getNode(4))
        list.append(graph.getNode(5))
        self.assertEqual(list, ga.connected_component(4))

    def test_connected_components(self):
        ans = []
        graph = createGraph()
        ga = GraphAlgo(graph)
        list1 = [graph.getNode(0), graph.getNode(1), graph.getNode(2), graph.getNode(3),
                 graph.getNode(4), graph.getNode(5)]
        ans.append(list1)
        list = [graph.getNode(6)]
        ans.append(list)
        self.assertEqual(ans, ga.connected_components())

    def test_plot_graph(self):
        graph = createGraph()
        ga = GraphAlgo(graph)
        ga.plot_graph()
        graph.add_node(7)
        graph.add_node(8)
        graph.add_node(9, (30, 35))
        ga = GraphAlgo(graph)
        ga.plot_graph()
        g = self.randomGraph(1000)
        algo = GraphAlgo(g)
        algo.plot_graph()

    def randomGraph(self, nodes: int):
        graph = DiGraph()
        for i in range(nodes):
            graph.add_node(i)
        for i in range(int(nodes)):
            graph.add_edge(random.randint(0, nodes), i, random.randint(1, 5))
        return graph
