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
        return self.nodes.get(key)

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        in_edges = {}
        # index = 0
        for ni in self.getNode(id1).enter:
            s = (ni, "-->", id1)
            # w = self.edges[s]
            # dict[index] = (ni, w)
            in_edges[ni] = self.edges[s]
            # index += 1
        return in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        out_edges = {}
        for ni in self.getNode(id1).exit:
            s = (id1, "-->", ni)
            out_edges[ni] = self.edges[s]
        return out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        if not self.nodes.__contains__(id1) or not self.nodes.__contains__(id2):
            return False
        s = (id1, "-->", id2)
        if self.edges.__contains__(s) and self.edges[s] == weight:
            return False
        self.edges[s] = weight
        n1 = self.nodes.get(id1)
        n2 = self.getNode(id2)
        n1.exit[id2] = n2
        n2.enter[id1] = n1
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.__contains__(node_id):
            return False
        node = NodeData(node_id, pos)
        self.nodes[node_id] = node
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.__contains__(node_id):
            node = self.getNode(node_id)
            for temp in node.enter:
                ni = self.getNode(temp)
                ni.exit.pop(node_id)
                s = (temp, "-->", node_id)
                self.edges.pop(s)
            for temp in node.exit:
                ni = self.getNode(temp)
                ni.enter.pop(node_id)
                s = (node_id, "-->", temp)
                self.edges.pop(s)

            self.nodes.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        s = (node_id1, "-->", node_id2)
        if self.edges.__contains__(s):
            n1 = self.getNode(node_id1)
            n2 = self.getNode(node_id2)
            n1.exit.pop(node_id2)
            n2.enter.pop(node_id1)
            self.edges.pop(s)
            self.mc += 1
            return True
        return False

    def __str__(self):
        return "DiGraph: " + str(self.nodes)

    def __repr__(self):
        return str(self)
