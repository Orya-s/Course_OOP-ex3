from unittest import TestCase
from paintGraph import *
from DiGraph import DiGraph, NodeData
from GraphAlgo import GraphAlgo

import unittest
import random
from GraphAlgo import GraphAlgo
import time


class MyTestCase(unittest.TestCase):
   # def test_save_big_graphs(self):
        # global g
        # g = DiGraph()
        # x = 1000000
        # for i in range(x):
        #     g.add_node(NodeData(id=i).id)
        #     g.get_node(i).myLocation = (random.uniform(0.0, 60.0), random.uniform(0.0, 50.0), 0.0)
        #
        # for j in range(x):
        #     g.add_edge(j, (j + 2050) % x, random.uniform(0.0, 20.0))
        #     # g.add_edge(j, int(random.uniform(0, x)), random.uniform(0.0, 20.0))
        #
        # global ga
        #
        # ga = GraphAlgo(g)
        #
        # ga.save_to_json("1000000_nodes.json")
        # print("nodes - ", ga.my_g.node_size, " edges - ", ga.my_g.edge_size)

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


if __name__ == '__main__':
    unittest.main()












#
# def randomGraph(nodes: int):
#     graph = DiGraph()
#     for i in range(nodes):
#         graph.add_node(i)
#         graph.getNode(i).pos = (random.randint(0, nodes), random.randint(0, nodes))
#     for i in range(int(nodes / 3)):
#         graph.add_edge(random.randint(0, nodes), i, random.randint(1, 5))
#     return graph
#
#
#
# class test_Compare(TestCase):
#     def test_plot_graph(self):
#         graph = randomGraph(1000000)
#         ga = GraphAlgo(graph)
#         ga.save_to_json("1000000N_333333E.json")
#         ga.load_from_json("1000000N_333333E.json")
#         #print(ga.connected_components())
#
#


