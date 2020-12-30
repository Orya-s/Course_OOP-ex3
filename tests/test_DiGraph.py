from unittest import TestCase

from DiGraph import DiGraph, NodeData


class TestNodeData(TestCase):
    def test_get_ni(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        self.assertEqual({}, g.getNode(1).getNi())
        g.add_edge(1, 2, 1)
        g.add_edge(2, 1, 1)
        self.assertDictEqual(({2:  g.getNode(2)}), g.getNode(1).getNi())
        g.add_edge(2, 3, 1.5)
        g.add_edge(2, 5, 3)
        g.add_edge(2, 6, 2.8)
        self.assertDictEqual(({1: g.getNode(1), 3: g.getNode(3), 5: g.getNode(5), 6: g.getNode(6)}), g.getNode(2).getNi())
        g.remove_edge(2, 3)
        self.assertDictEqual(({1: g.getNode(1),  5: g.getNode(5), 6: g.getNode(6)}), g.getNode(2).getNi())
        # g.remove_node(2)
        # self.assertEqual({}, g.getNode(2).getNi()) ###check what to do if graph doesnt contain node

    def test_get_parents(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        self.assertDictEqual({}, g.getNode(1).getParents())
        g.add_edge(2, 1, 1)
        g.add_edge(3, 1, 1)
        g.add_edge(4, 1, 3)
        g.add_edge(5, 1, 2.8)
        g.add_edge(6, 1, 1.5)
        self.assertDictEqual({2: g.getNode(2), 3: g.getNode(3), 4: g.getNode(4), 5: g.getNode(5), 6: g.getNode(6)},
                             g.getNode(1).getParents())
        g.remove_edge(5, 1)
        g.remove_edge(3, 1)
        self.assertDictEqual({2: g.getNode(2), 4: g.getNode(4), 6: g.getNode(6)}, g.getNode(1).getParents())

    def test_has_ni(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        self.assertFalse(g.getNode(1).hasNi(2))
        g.add_edge(2, 1, 1)
        self.assertFalse(g.getNode(1).hasNi(2))
        self.assertTrue(g.getNode(2).hasNi(1))
        g.remove_node(1)
        self.assertFalse(g.getNode(2).hasNi(1))

    def test_has_parent(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        self.assertFalse(g.getNode(1).hasParent(2))
        g.add_edge(2, 1, 1)
        self.assertFalse(g.getNode(2).hasParent(1))
        self.assertTrue(g.getNode(1).hasParent(2))
        g.remove_node(1)
        g.add_node(1)
        self.assertFalse(g.getNode(1).hasParent(2))


class TestDiGraph(TestCase):
    def test_get_node(self):
        self.fail()

    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
