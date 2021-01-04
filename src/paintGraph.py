from DiGraph import DiGraph
import matplotlib.pyplot as plt

class paintGraph:

    def __init__(self, g: DiGraph):
        self.graph = g

    def drawnodes(self):
        nodes = []
        x = []
        y = []
        for node in self.graph.nodes:
            n = self.graph.getNode(node)
            nodes.append(n.id)
            x.append(n.pos[0])
            y.append(n.pos[1])
            plt.annotate(str(node), xy=(n.pos[0], n.pos[1]))
        plt.scatter(x, y, )

    def drawedges(self):
        x = []
        y = []
        i = 0
        colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'gold', 'pink']
        for edge in self.graph.edges:
            srcDest = edge.split("-->")
            x.append(self.graph.getNode(int(srcDest[0])).pos[0])
            y.append(self.graph.getNode(int(srcDest[0])).pos[1])
            x.append(self.graph.getNode(int(srcDest[1])).pos[0])
            y.append(self.graph.getNode(int(srcDest[1])).pos[1])
            colour = colours[(i % 10)]
            plt.arrow((self.graph.getNode(int(srcDest[0])).pos[0]), (self.graph.getNode(int(srcDest[0])).pos[1]),
                      (self.graph.getNode(int(srcDest[1])).pos[0])-(self.graph.getNode(int(srcDest[0])).pos[0]), (self.graph.getNode(int(srcDest[1])).pos[1])-(self.graph.getNode(int(srcDest[0])).pos[1]),
                      head_width=1, head_length=1, color=colour)
            # plt.plot(x, y, color=colour)
            x.clear()
            y.clear()
            i = i+1
        plt.show()
