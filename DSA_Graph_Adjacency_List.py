# implementing graph using adjacency list
graph = {}


# add new node to graph
def add_node(vertices):
    if vertices in graph:
        print('node is in graph')
    else:
        graph[vertices] = []


# add edge undirected unweighted graph
def add_edge(vertices1, vertices2):
    if vertices1 not in graph:
        print(vertices1, 'is not in graph')
    if vertices2 not in graph:
        print(vertices2, 'is not in graph')
    else:
        graph[vertices1].append(vertices2)
        graph[vertices2].append(vertices1)


add_node('A')
add_node('B')
add_edge('A', 'B')
print(graph)
