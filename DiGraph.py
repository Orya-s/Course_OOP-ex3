from GraphInterface import GraphInterface
#from NodeData import NodeData


class NodeData:

    enterNodes= {}
    exitNodes= {}

    def __init__(self, id: int, pos: tuple = None, enterNodes= None, exitNodes= None):
        self.id = id
        # if exitNodes is None:
        #     exitNodes = {}  # the list of edges coming from this node
        # if enterNodes is None:
        #     enterNodes = {}  # the list of edges coming into this node
        # self.exitNodes= exitNodes
        # self.enterNodes= enterNodes
        self.nodeTag = 0
        self.nodeInfo = ""
        self.tag = 0

    def getNi(self) -> dict:
        return self.exitNodes

    def getParents(self):
        return self.enterNodes

    def hasNi(self, key: int):
        return self.exitNodes.__contains__(key)

    def hasParent(self, key: int):
        return self.enterNodes.__contains__(key)

    def addNi(self, other):
        if not (self.exitNodes.__contains__(other.id)):
            self.exitNodes[other.id] = other
            other.enterNodes[self.id] = self
            #self.exitNodes[other.id.__str__()] = other

    def removeNi(self, other):
        if self.exitNodes.__contains__(other.id):
            self.exitNodes.pop(other.id, other)
            other.enterNodes.pop(self.id, self)

    def __str__(self):
        return "NodeData: " + str(self.id)

    def __repr__(self):
        return str(self)






class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}  # the list of nodes in the graph
        self.edges = {}
        self.mc = 0

    def getNode(self, id: int):
        if self.nodes.__contains__(id):
            return NodeData(self.nodes.get(id))

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    # def add_edge(self, id1: int, id2: int, weight: float):
    #     if not (self.nodes.__contains__(id1) or self.nodes.__contains__(id2)):
    #         return False
    #     s = (id1, "-->", id2)
    #     if self.edges.__contains__(s) and self.edges[s] == weight:
    #         return False
    #     self.edges[s] = weight
    #     n = self.getNode(id1)
    #     ni = self.getNode(id2)
    #     n.exitNodes[id2] = ni
    #     ni.enterNodes[id1] = n
    #     print(n.getNi())
    #     return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not (self.nodes.__contains__(id1) or self.nodes.__contains__(id2)):
            return False
        s = (id1, "-->", id2)
        if self.edges.__contains__(s) and self.edges[s] == weight:
            return False
        self.edges[s] = weight

        n = self.getNode(id1)
        ni = self.getNode(id2)
        # if not self.edges.__contains__(s):
        #  n.addNi(ni)
        n.exitNodes[id2] = ni
        ni.enterNodes[id1] = n
        print("                ", n.getNi())  ##### delete

        # print(ni.getParents())
        # print(ni.getNi())
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.__contains__(node_id):
            return False
        nodeTemp = NodeData(node_id)
        self.nodes[node_id] = nodeTemp
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.__contains__(node_id):
            node = self.getNode(node_id)
            for temp in node.getNi():
                print("ni: ", temp)

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
    n1 = NodeData(1)
    n2 = NodeData(2)
    g = DiGraph()
    g.add_node(1)
    g.add_node(2)
    print(g.nodes)
    n1.addNi(n2)
    print(n1.getNi())
    print(g.add_edge(1, 2, 1))
    print(n1.hasNi(2))
    print(n1.getNi())

    # print(n1.getNi())
    # print(n2.getNi())
    # print(g.edges)


if __name__ == '__main__':
    main()
