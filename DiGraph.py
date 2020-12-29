from GraphInterface import GraphInterface
from NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}  # the list of nodes in the graph
        self.edges = {}
        self.mc = 0

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
        self.edges[id1, "-->", id2] = weight
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.__contains__(node_id):
            return False
        nodeTemp = NodeData(node_id, pos)
        self.nodes[node_id] = nodeTemp
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.__contains__(node_id):




            self.nodes.pop(node_id)
            return True
        return False


    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def __str__(self):
        return "DiGraph: " + str(self.nodes)

    def __repr__(self):
        return str(self)
