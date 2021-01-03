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
    g1.save_to_json("graph")

if __name__ == '__main__':
    main()
