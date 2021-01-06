# OOP-ex3
### Ex3 contains the following classes:
- NodeData- representing a vertex in the graph.
- DiGraph- implementing GraphInterface- representing a directed weighted graph.
- GraphAlgo- implementing GraphAlgoInterface interface.
- paintGraph- implementing the painting of the graph.

## Graph implementation
DiGraph class represents a directed weighted graph, represented by a dictionary. <br />
The reason we chose to represent the graph in a dictionary is because it allows easy access to each node in the graph, therefor questions
like whether two nodes are connected and how many edges are in the graph can be answered in O(1). Adding a new node to the graph, or
connecting two nodes in the graph with an edge, can also be done easily in O(1).  Connecting simply requires adding each of the nodes 
to the other node's neighbors list with the wanted weight, and removing an edge requires removing each of the nodes from the other node's 
neighbors list. 

## Algorithms
GraphAlgo class represents the regular Graph Theory algorithms including:
1. load_from_json(file)
2. save_to_json(file)
3. shortestPath(int src, int dest) -> (float, list)
4. connected_component(node_id) -> list
5. connected_components() -> List[list]
6. plot_graph()

### The Dijkstra algorithm
In order to find the distance of the shortest path in the graph we used the Dijkstra algorithm, which allows to find the shortest path in a directed weighted graph in 
a fast and efficient way.          
For more information on the algorithm: https://brilliant.org/wiki/dijkstras-short-path-finder/

![Weighted Graph](https://ds055uzetaobb.cloudfront.net/brioche/uploads/ydOEDFABWr-graph1.png?width=2400)

### The BFS algorithm
Breadth first search is a general technique of traversing a graph. Breadth first search will always find the shortest path first. In this type of search
the state space is represented in form of a tree. The nodes of the tree represent the start value, various intermediate states, and the final state. In this
search a queue data structure is used, and it is level by level traversal. Breadth first search expands nodes in order of their distance from the root. It is a
path finding algorithm that is capable of always finding the solution if one exists. The solution which is found is always the optional solution.  <br />
Algorithm:
Step 1: Place the root node inside the queue.  <br />
Step 2: If the queue is empty then stops and return failure.  <br />
Step 3: If the front node of the queue is a goal node then stop and return success.  <br />
Step 4: Remove the front node from the queue. Process it and find all its neighbors that are in ready state then place them inside the queue in any order.  <br />
Step 5: Go to Step 3.  <br />
Step 6: Exit.  <br />




## Clone repository:
```
$ git clone https://github.com/Orya-s/OOP-ex3.git 
```


See our [Wiki] for full documentation, examples, operational details and other information.



[Wiki]: https://github.com/Orya-s/OOP-ex3/wiki 
