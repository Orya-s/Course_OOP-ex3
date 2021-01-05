import unittest
from DiGraph import NodeData


class TestNodeData(unittest.TestCase):
    def test_get_ni(self):
        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n1.exit[2] = n2
        n1.exit[2] = n2
        n1.exit[3] = n3
        self.assertEqual(2, len(n1.getNi()))

    def test_get_parents(self):
        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n1.enter[2] = n2
        n1.enter[2] = n2
        n1.enter[3] = n3
        self.assertEqual(2, len(n1.getParents()))

    def test_has_ni(self):
        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n1.enter[2] = n2
        n1.enter[2] = n2
        n1.enter[3] = n3
        self.assertFalse(n1.hasNi(2))

        n1.exit[2] = n2
        n1.exit[2] = n2
        n1.exit[3] = n3
        self.assertTrue(n1.hasNi(2))

    def test_has_parent(self):
        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n1.enter[2] = n2
        n1.enter[2] = n2
        n1.enter[3] = n3
        self.assertTrue(n1.hasParent(2))

        n1 = NodeData(1)
        n2 = NodeData(2)
        n3 = NodeData(3)
        n1.exit[2] = n2
        n1.exit[2] = n2
        n1.exit[3] = n3
        self.assertFalse(n1.hasParent(2))
