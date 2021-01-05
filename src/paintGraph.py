import random

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
            if self.graph.getNode(node).pos is None:
                counter = 0
                a = 0
                b = 0
                for node1 in self.graph.getNode(node).getNi():
                    if not self.graph.getNode(node1).pos is None:
                        counter += 1
                        a += self.graph.getNode(node1).pos[0]
                        b += self.graph.getNode(node1).pos[1]
                        if counter == 5:
                            break
                if counter == 1:
                    self.graph.getNode(node).pos = (a + 6, b + 6)
                if counter == 0:
                    self.graph.getNode(node).pos = (
                        random.randint(0, len(self.graph.nodes)), random.randint(0, len(self.graph.nodes)))
                if counter > 1:
                    self.graph.getNode(node).pos = (a / counter, b / counter)
            n = self.graph.getNode(node)
            nodes.append(n.id)
            x.append(n.pos[0])
            y.append(n.pos[1])
            if len(self.graph.nodes) < 1000:
                plt.annotate(str(node), xy=(n.pos[0] , n.pos[1]), size=8, c="r")
        plt.scatter(x, y, c='black', s= 5)

    def drawedges(self):
        x = []
        y = []
        i = 0
        colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'gold', 'pink']
        for edge in self.graph.edges:
            srcDest = edge.split("-->")
            w = self.graph.edges[edge]
            x.append(self.graph.getNode(int(srcDest[0])).pos[0])
            y.append(self.graph.getNode(int(srcDest[0])).pos[1])
            x.append(self.graph.getNode(int(srcDest[1])).pos[0])
            y.append(self.graph.getNode(int(srcDest[1])).pos[1])
            colour = colours[(i % 10)]
            # plt.arrow((self.graph.getNode(int(srcDest[0])).pos[0]), (self.graph.getNode(int(srcDest[0])).pos[1]),
            #           ((self.graph.getNode(int(srcDest[1])).pos[0]) - (self.graph.getNode(int(srcDest[0])).pos[0])),
            #           ((self.graph.getNode(int(srcDest[1])).pos[1]) - (self.graph.getNode(int(srcDest[0])).pos[1])),
            #           head_width=0.7, head_length=0.7, color=colour)
            plt.plot(x, y, color=colour)
            x1 = self.graph.getNode(int(srcDest[0])).pos[0]
            y1 = self.graph.getNode(int(srcDest[0])).pos[1]
            x2 = self.graph.getNode(int(srcDest[1])).pos[0]
            y2 = self.graph.getNode(int(srcDest[1])).pos[1]
            if len(self.graph.edges) < 100:
                if x1 > x2:
                    plt.annotate("{:.2f}".format(w), xy=((x1 + x2) / 2, (y1 + y2) / 2), size=6, c="b")
                else:
                    plt.annotate("{:.2f}".format(w), xy=((x1 + x2) / 2 , (y1 + y2) / 2), size=6, c="g")

            x.clear()
            y.clear()
            i = i + 1
        plt.show()
