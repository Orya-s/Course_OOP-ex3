from DiGraph import DiGraph


def main():
    g = DiGraph()
    g.add_node(1)
    g.add_node(2)
    print(g)
    print(g.add_edge(1, 2, 1))
    print(g.add_edge(2, 1, 1))
    print(g.getNode(1).exit)
    print(g.getNode(2).enter)
    print(g.remove_node(2))
    print(g.getNode(1).exit)
    print(g.getNode(1).enter)
    g.add_node(2)
    print(g.add_edge(1, 2, 1))
    print(g.remove_edge(1, 2))
    print(g.edges)
    print(g.getNode(1).exit)
    print(g.getNode(2).enter)


if __name__ == '__main__':
    main()
