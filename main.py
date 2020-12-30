import matrix
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from DiGraph import NodeData
# import numpy as np


def main():
    n1 = NodeData(1)
    n2 = NodeData(2)
    print("should print {} :  ", n1.getNi())

    g = DiGraph()
    print("should print {} :  ", g.nodes)
    g.add_node(n1.id)
    print(g.nodes)
    g.add_node(n2.id)
    print(g.nodes)
    g.add_edge(n1.id, n2.id, 1)
    print(g.edges)
    print(n1.exitNodes)

    # print("has ni : ",n1.hasNi(n2.id))
    # print("exit nodes : ",n1.exitNodes)
    #
    # print(g.edges)
    # print(g.add_edge(n1.id,n2.id,1))
    # print(g.edges)
    # print(g.e_size())
    # print(n1.exitNodes, "   exit")
    # print(n1.getNi())
    # print("parent ", n2.getParents())




if __name__ == '__main__':
    main()




