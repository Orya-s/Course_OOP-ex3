class NodeData:
    #_nodeId = 0
    #_nodeTag = 0
    #_nodeInfo = ""
    #_enterNodes = {}  # the list of edges coming into this node
    #_exitNodes = {}  # the list of edges coming from this node

    def __init__(self, id: int, pos:tuple=None):
        self.id = id
        self.enterNodes = {}  # the list of edges coming into this node
        self.exitNodes = {}  # the list of edges coming from this node
        self.nodeTag = 0
        self.nodeInfo = ""
        self.tag = 0

    def getNi(self):
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

    def removeNi(self, other):
        if self.exitNodes.__contains__(other.id):
            self.exitNodes.pop(other.id, other)
            other.enterNodes.pop(self.id, self)

    def __str__(self):
        return "NodeData: " + str(self.id)

    def __repr__(self):
        return str(self)




#def main():
#    n1 = NodeData(1)
#    print(n1)

#if __name__ == '__main__':
#    main()
