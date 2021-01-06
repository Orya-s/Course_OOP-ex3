from unittest import TestCase
from paintGraph import *
from DiGraph import DiGraph, NodeData
from GraphAlgo import GraphAlgo

import unittest
import random
from GraphAlgo import GraphAlgo
import time


class MyTestCase(unittest.TestCase):

    def test_time_100_graphs(self):
        print("__________________________________________________________________--")
        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("100_nodes.json")
        end_load = time.time()
        print("TIME- LOAD:   loading 100 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(42, 22))
        end__shortest_path = time.time()
        print("TIME- PATH:   shortest path 100 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(82).__sizeof__())
        print("cc= ", len(G.connected_component(82)))
        end_connected_component = time.time()
        print("TIME- CC:   connected_component 100 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print(
            "TIME- CCS:   connected_components 100 node graph: " + (end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("TIME- ALL:   all 100 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_10000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("10000_nodes.json")
        end_load = time.time()
        print("TIME- LOAD:   loading 10000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(8125, 7725))
        end__shortest_path = time.time()
        print("TIME- PATH:   shortest path 10000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(8125).__sizeof__())
        end_connected_component = time.time()
        print(
            "TIME- CC:   connected_component 10000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("TIME- CCS:   connected_components 10000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("TIME- ALL:   all 10000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_100000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("100000_nodes.json")
        end_load = time.time()
        print("TIME- LOAD:   loading 100000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(67596, 99996))
        end__shortest_path = time.time()
        print("TIME- PATH:   shortest path 100000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(99996).__sizeof__())
        end_connected_component = time.time()
        print(
            "TIME- CC:   connected_component 100000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("TIME- CCS:   connected_components 100000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("TIME- ALL:   all 100000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")

    def test_time_1000000_graphs(self):
        print("__________________________________________________________________--")

        G = GraphAlgo(None)
        start_all = time.time()

        start_load = time.time()
        G.load_from_json("1000000_nodes.json")
        end_load = time.time()
        print("TIME- LOAD:   loading 1000000 node graph: " + (end_load - start_load).__str__())

        start_shortest_path = time.time()
        print(G.shortest_path(786296, 99996))
        end__shortest_path = time.time()
        print("TIME- PATH:   shortest path 1000000 node graph: " + (end__shortest_path - start_shortest_path).__str__())

        start_connected_component = time.time()
        print(G.connected_component(99996).__sizeof__())
        end_connected_component = time.time()
        print(
            "TIME- CC:   connected_component 1000000 node graph: " + (end_connected_component - start_connected_component).__str__())

        start_connected_components = time.time()
        print(G.connected_components().__sizeof__())
        end_connected_components = time.time()
        print("TIME- CCS:   connected_components 1000000 node graph: " + (
                    end_connected_components - start_connected_components).__str__())

        end_all = time.time()
        print("TIME- ALL:   all 100000 node graph : " + (end_all - start_all).__str__())
        print("__________________________________________________________________--")



