# This is a sample Python script.
import matrix
from NodeData import NodeData
from DiGraph import DiGraph


# import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

n1 = NodeData(1)
n2 = NodeData(2)
n3 = NodeData(3)


print(n1.id)
print(n1.getNi())
n1.addNi(n2)
n1.addNi(n3)
print(n1.getNi())
n1.removeNi(n2)
print(n1.getNi())
print(n3.hasParent(n1.id))
n1.removeNi(n3)
print(n3.hasParent(n1.id))


g = DiGraph()
print(g.nodes)
g.add_node(n1.id, None)
print(g.v_size())
print(g.add_edge(n1.id,n2.id,2))
print(g.edges)
print(g.add_edge(n1.id,n2.id,1))
print(g.edges)
print(g.e_size())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
