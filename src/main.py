import queue
import numpy as np
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def main():
    g = DiGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 1, 1)
    g.add_edge(3, 2, 1)
    g.add_edge(6, 2, 1)
    g.add_edge(7, 4, 1)
    g.add_edge(8, 1, 1)
    g.add_edge(5, 7, 1)
    g.add_edge(4, 3, 1)
    g1 = GraphAlgo(g)
    t = g1.save_to_json("graph.json")
    g2 = GraphAlgo()
    g2.load_from_json("graph.json")
    #print(g2.graph.edges)
    q = queue.PriorityQueue()
    t3 = g.getNode(3).tag
    t1 = g.getNode(1).tag
    print(t3)
    print(t1)
    t1 = g.getNode(1).tag = 0.5
    q.put((t3, g.getNode(3)))
    q.put((t1, g.getNode(1)))
   # q.put((g.getNode(2).tag, g.getNode(2)))

    while not q.empty():
        print(q.get())

    print(g.edges[str(1) + "-->" + str(2)])


if __name__ == '__main__':
    main()
