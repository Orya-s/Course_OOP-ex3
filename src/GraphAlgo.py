from typing import List
from DiGraph import DiGraph
from DiGraph import NodeData
import json
import queue
import sys

from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> DiGraph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph()
        with open(file_name, 'r') as json_path:
            json_dict = json.load(json_path)
        for node in json_dict["Nodes"]:
            id = node["id"]
            pos = node["pos"]
            self.graph.add_node(id, pos)
        for edge in json_dict["Edges"]:
            src = edge["src"]
            dest = edge["dest"]
            w = edge["w"]
            self.graph.add_edge(src, dest, w)
        return True

    def save_to_json(self, file_name: str) -> bool:
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
        if self.graph is None:
            return []
        if not self.graph.nodes.__contains__(id1):
            return []
        for n in self.graph.nodes:
            node = self.graph.getNode(n)
            node.info = "none"
            node.tag = sys.float_info.max
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
        tempexit = []
        for node in self.graph.nodes:
            if self.graph.getNode(node).visited:
                tempexit.append(self.graph.getNode(node))

        for n in self.graph.nodes:
            node = self.graph.getNode(n)
            node.info = "none"
            node.tag = sys.float_info.max
            node.visited = False
        node = self.graph.getNode(id1)
        checkQ.put(node)
        node.visited = True
        while not checkQ.empty():
            temp = checkQ.get()
            for nodes in temp.enter:
                if not self.graph.getNode(nodes).visited:
                    checkQ.put(self.graph.getNode(nodes))
                    self.graph.getNode(nodes).visited = True
        tempenter = []
        for node in self.graph.nodes:
            if self.graph.getNode(node).visited:
                tempenter.append(self.graph.getNode(node))

        ans = []
        for node in tempenter:
            if tempexit.__contains__(node):
                ans.append(node)
        return ans

    def connected_components(self) -> List[list]:
        ans = []
        for node in self.graph.nodes:
            if not self.graph.getNode(node).visited:
                add = self.connected_component(node)
                ans.append(add)
        return ans

    def plot_graph(self) -> None:
        pass

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
