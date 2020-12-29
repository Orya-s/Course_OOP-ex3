# This is a sample Python script.
import matrix
from NodeData import NodeData


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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
