from unittest import TestCase
from NodeData import NodeData


class TestNodeData(TestCase):
    def test_get_ni(self):
        n = NodeData(0)
        self.assertEqual({}, n.getNi())

    def test_get_parents(self):
        self.fail()

    def test_has_ni(self):
        self.assertEqual(1,2)

    def test_has_parent(self):
        self.fail()

    def test_add_ni(self):
        self.fail()

    def test_remove_ni(self):
        self.fail()
