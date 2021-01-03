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
        with open('graph.json', 'w') as json_path:
            for edge in self.graph.edges.keys():
                print(type(edge))
                # print(s.split("-->", ))
                # str2 = str1.split("-->")
                # print(str2)
                    # print(json.dump(edge, json_path))
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
