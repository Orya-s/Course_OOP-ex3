from typing import List
from DiGraph import DiGraph
import json

from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        self.graph = g
        # self.edges = g.edges

    def get_graph(self) -> DiGraph:
        return self

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name) -> bool:
        edgeload = []
        vertices = []
        for edgeKey in self.graph.edges:
            weight = self.graph.edges[edgeKey]
            srcDest = edgeKey.split("-->")
            edgeload.insert(int(srcDest[0]), int(srcDest[1]))
            print(edgeload)

        # with open('graph.json', 'w') as json_path:
        #     json.dump("src: " + srcDest[0] + "dest: " + srcDest[1], json_path)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
