class NodeData:

    def __init__(self, id: int, pos: tuple = None, enterNodes: dict = None,exitNodes: dict = None):
        self.id = id
        enterNodes = {}  # the list of edges coming into this node
        exitNodes = {}  # the list of edges coming from this node
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
           # self.exitNodes[other.id.__str__()] = other

    def removeNi(self, other):
        if self.exitNodes.__contains__(other.id):
            self.exitNodes.pop(other.id, other)
            other.enterNodes.pop(self.id, self)

    def __str__(self):
        return "NodeData: " + str(self.id)

    def __repr__(self):
        return str(self)


def main():
    n0 = NodeData(0)
    n1 = NodeData(1)
    n0.addNi(n1)
    print(n0.getNi())
    print(n1.getNi())


if __name__ == '__main__':
    main()
