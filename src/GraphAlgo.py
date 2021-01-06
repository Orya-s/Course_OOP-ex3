from typing import List

from DiGraph import DiGraph
from DiGraph import NodeData
from paintGraph import *
import json
import queue
import sys

from GraphAlgoInterface import GraphAlgoInterface

visitDict = {}


class GraphAlgo(GraphAlgoInterface):
    """
  This class represents a directed weighted Graph Theory algorithms including:
  1. load_from_json(file)
  2. save_to_json(file)
  3. shortestPath(int src, int dest) -> (float, list)
  4. connected_component(node_id) -> list
  5. connected_components() -> List[list]
  6. plot_graph()
    """

    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> DiGraph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        This method loads a graph to this graph algorithm.
        :param file_name: file name
        :return: true - iff the graph was successfully loaded.
        """
        self.graph = DiGraph()
        with open(file_name, 'r') as json_path:
            json_dict = json.load(json_path)
        for node in json_dict["Nodes"]:
            id = node["id"]
            if type(node["pos"]) is list:
                pos = node["pos"]
            elif not node["pos"] is None:
                posStr = (node["pos"]).split(",")
                pos = (float(posStr[0]), float(posStr[1]))
            else:
                pos = None
            self.graph.add_node(id, pos)
        for edge in json_dict["Edges"]:
            src = edge["src"]
            dest = edge["dest"]
            w = edge["w"]
            self.graph.add_edge(src, dest, w)
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
       Saves this weighted directed graph to the given file name.
        :param file_name - the file name.
        :return: true - iff the file was successfully saved.
        """
        dict = {}
        edgeload = []
        vertices = []
        for edgeKey in self.graph.edges:
            temp = {}
            srcDest = edgeKey.split("-->")
            temp["src"] = int(srcDest[0])
            temp["w"] = self.graph.edges[edgeKey]
            temp["dest"] = int(srcDest[1])
            edgeload.append(temp)

        for nodeKey in self.graph.nodes:
            temp = {"id": nodeKey, "pos": self.graph.getNode(nodeKey).pos}
            vertices.append(temp)

        dict["Edges"] = edgeload
        dict["Nodes"] = vertices

        with open(file_name, 'w') as json_path:
            json.dump(dict, json_path)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        :param id1: The start node id
        :param id2: The end node id
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if not self.graph.nodes.__contains__(id1) or not self.graph.nodes.__contains__(id2):
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        w = (self.dijkstra(id1, id2))
        if w == -1:
            return float('inf'), []
        self.graph.getNode(id2)
        path = self.getPath(id1, id2)
        return w, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        Notes: If the graph is None or id1 is not in the graph, the function should return an empty list []
        :param id1: The node id
        :return: The list of nodes in the SCC
        """
        if self.graph is None:
            return []
        if not self.graph.nodes.__contains__(id1):
            return []
        for n in self.graph.nodes:
            node = self.graph.getNode(n)
            node.visited = False
        node = self.graph.getNode(id1)
        checkQ = queue.Queue()
        checkQ.put(node)
        node.visited = True
        while not checkQ.empty():
            temp = checkQ.get()
            for nodes in temp.getNi():
                if not self.graph.getNode(nodes).visited:
                    checkQ.put(self.graph.getNode(nodes))
                    self.graph.getNode(nodes).visited = True

        ans = []
        node = self.graph.getNode(id1)
        checkQ.put(node)

        while not checkQ.empty():
            temp = checkQ.get()
            for nodes in temp.enter:
                if self.graph.getNode(nodes).visited:
                    checkQ.put(self.graph.getNode(nodes))
                    self.graph.getNode(nodes).visited = False
                    ans.append(nodes)

        if not ans.__contains__(id1):
            ans.append(id1)

        finalans = []
        ans.sort()
        for n in ans:
            finalans.append(self.graph.getNode(n))
            visitDict[n] = self.graph.getNode(n)

        return finalans

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        Notes: If the graph is None the function returns an empty list []
        :return: The list all SCC
        """
        visitDict.clear()
        ans = []
        for node in self.graph.nodes:
            if not visitDict.__contains__(node):
                add = self.connected_component(node)
                ans.append(add)
        return ans

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        :return: None
        """
        d = paintGraph(self.graph)
        d.drawnodes()
        d.drawedges()

    def dijkstra(self, id1: int, id2: int):
        q = queue.PriorityQueue()
        for n in self.graph.nodes:
            node = self.graph.getNode(n)
            node.info = "none"
            node.tag = sys.float_info.max
            node.visited = False
        start = self.graph.getNode(id1)
        start.tag = 0.0
        q.put((start.tag, start.id, start))
        while not q.empty():
            current = q.get()
            curr = current[2]
            if not curr.visited:
                curr.visited = True
                if curr.id == id2:
                    return curr.tag
                for nei in self.graph.getNode(curr.id).exit:
                    e = self.graph.getNode(nei)
                    if not e.visited:
                        dist = curr.tag + self.graph.edges[str(curr.id) + "-->" + str(nei)]
                        if dist < e.tag:
                            e.tag = dist
                            e.info = curr.id
                            q.put((e.tag, e.id, e))
        return -1

    def getPath(self, id1: int, id2: int):
        node = self.graph.getNode(id2)
        path = []
        while node.id != id1:
            path.append(node.id)
            info = node.info
            node = self.graph.getNode(info)
        path.append(id1)
        path.reverse()
        return path
