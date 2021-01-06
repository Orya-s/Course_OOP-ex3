from GraphInterface import GraphInterface


class NodeData:
    """This class represents a NodeData in a directed weighted graph."""

    def __init__(self, key: int, pos: tuple = None, enter=None, exit=None):
        self.id = key
        self.pos = pos
        if enter is None:
            self.enter = {}
        if exit is None:
            self.exit = {}
        self.info = ""
        self.tag = 0.0
        self.visited = False

    def getNi(self):
        """
        Returns the number of vertices going out of this node
        """
        return self.exit

    def getParents(self):
        """
        Returns the number of vertices coming to this node
        """
        return self.enter

    def hasNi(self, key: int):
        """
        This function returns whether the selected node has an edge to the nodeData with the given key
        :param key: of ni
        """
        return self.exit.__contains__(key)

    def hasParent(self, key: int):
        """
        This function returns whether the selected nodeData has an edge to this node
        :param key: of parent
        """
        return self.enter.__contains__(key)

    def __str__(self):
        return "NodeData: " + str(self.id)

    def __repr__(self):
        return str(self)

    def __cmp__(self, other):
        return other.tag < self.tag


class DiGraph(GraphInterface):
    """This class implements GraphInterface, represents a directed weighted graph."""

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def getNode(self, key: int) -> NodeData:
        return self.nodes.get(key)

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return len(self.edges)

    def get_all_v(self) -> dict:
        """returns a dictionary of all the nodes in the Graph, each node is represented using a pair (key, node_data)"""
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        in_edges = {}
        for ni in self.getNode(id1).enter:
            s = str(ni) + "-->" + str(id1)
            in_edges[ni] = self.edges[s]
        return in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id, each node is represented using a pair (key,
        weight)
        """
        out_edges = {}
        for ni in self.getNode(id1).exit:
            s = str(id1) + "-->" + str(ni)
            out_edges[ni] = self.edges[s]
        return out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 == id2:
            return False
        if not self.nodes.__contains__(id1) or not self.nodes.__contains__(id2):
            return False
        s = str(id1) + "-->" + str(id2)
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
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        If the node id already exists the node will not be added
        """
        if self.nodes.__contains__(node_id):
            return False
        node = NodeData(node_id, pos)
        self.nodes[node_id] = node
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        If the node id does not exists the function will do nothing
        """
        if self.nodes.__contains__(node_id):
            node = self.getNode(node_id)
            for temp in node.enter:
                ni = self.getNode(temp)
                ni.exit.pop(node_id)
                s = str(temp) + "-->" + str(node_id)
                self.edges.pop(s)
            for temp in node.exit:
                ni = self.getNode(temp)
                ni.enter.pop(node_id)
                s = str(node_id) + "-->" + str(temp)
                self.edges.pop(s)

            self.nodes.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        If such an edge does not exists the function will do nothing
        """
        s = str(node_id1) + "-->" + str(node_id2)
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

    def __eq__(self, other):
        if len(self.nodes) != len(other.nodes):
            return False
        if len(self.edges) != len(other.edges):
            return False
        for node in self.nodes:
            if not other.nodes.__contains__(node):
                return False
        for edge in self.edges:
            if not other.edges.__contains__(edge):
                return False
        return True
