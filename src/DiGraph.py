from GraphInterface import GraphInterface


class NodeData:

    def __init__(self, key: int, pos: tuple = None, enter=None, exit=None):
        self.id = key
        self.pos = pos
        if enter is None:
            self.enter = {}
        if exit is None:
            self.exit = {}
        self.info = ""
        self.tag = 0.0

    def getNi(self):
        return self.exit

    def getParents(self):
        return self.enter

    def hasNi(self, key: int):
        return self.exit.__contains__(key)

    def hasParent(self, key: int):
        return self.enter.__contains__(key)

    def __str__(self):
        return "NodeData: " + str(self.id)

    def __repr__(self):
        return str(self)


class DiGraph(GraphInterface):

    def __init__(self, nodes=None, edges=None):
        if nodes is None:
            self.nodes = {}
        if edges is None:
            self.edges = {}
        self.mc = 0

    def getNode(self, key: int) -> NodeData:
        return self.nodes[key]
        #
        # if self.nodes.__contains__(key):
        #     return NodeData(self.nodes.get(key))
        # else:
        #     return None

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not (self.nodes.__contains__(id1) or self.nodes.__contains__(id2)):
            return False
        s = (id1, "-->", id2)
        if self.edges.__contains__(s) and self.edges[s] == weight:
            return False
        self.edges[s] = weight
        n1 = self.getNode(id1)
        n2 = self.getNode(id2)
        n1.exit[id2] = n2
        n2.enter[id1] = n1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.__contains__(node_id):
            return False
        node = NodeData(node_id, pos)
        self.nodes[node_id] = node
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.__contains__(node_id):
            node = self.getNode(node_id)
            for temp in node.enter:
                ni = self.getNode(temp)
                ni.exit.pop(node_id)
            for temp in node.exit:
                ni = self.getNode(temp)
                ni.enter.pop(node_id)
            self.nodes.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def __str__(self):
        return "DiGraph: " + str(self.nodes)

    def __repr__(self):
        return str(self)


def main():
    # n1 = NodeData(1)
    # n2 = NodeData(2)
    g = DiGraph()
    g.add_node(1)
    g.add_node(2)
    print(g)
    print(g.add_edge(1, 2, 1))
    print(g.getNode(1).exit)
    print(g.getNode(2).enter)



if __name__ == '__main__':
    main()
