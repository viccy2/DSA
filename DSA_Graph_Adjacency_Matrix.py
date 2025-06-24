# Graph using Adjacency Matrix

nodes = []
graph = []


# insert new node into graph
def add_node(vertices):
    global count_node
    if vertices in nodes:
        print('node exist in Graph')
    else:
        count_node += 1
        nodes.append(vertices)
        for i in graph:
            i.append(0)
        row = []
        for i in range(count_node):
            row.append(0)
        graph.append(row)


# add edge between nodes
# for undirected graph
def add_edge_undirected(vertices1, vertices2):
    if vertices1 not in nodes:
        print(vertices1, 'is not in graph')
    if vertices2 not in nodes:
        print(vertices2, 'is not in graph')
    else:
        idx1 = nodes.index(vertices1)
        idx2 = nodes.index(vertices2)
        graph[idx1][idx2] = 1
        graph[idx2][idx1] = 1


# for undirected weighted graph
def add_edge_undirected_w(vertices1, vertices2, cost):
    if vertices1 not in nodes:
        print(vertices1, 'is not in graph')
    if vertices2 not in nodes:
        print(vertices2, 'is not in graph')
    else:
        idx1 = nodes.index(vertices1)
        idx2 = nodes.index(vertices2)
        graph[idx1][idx2] = cost
        graph[idx2][idx1] = cost


# for directed graph
def add_edge_directed(vertices1, vertices2):
    if vertices1 not in nodes:
        print(vertices1, 'is not in graph')
    if vertices2 not in nodes:
        print(vertices2, 'is not in graph')
    else:
        idx1 = nodes.index(vertices1)
        idx2 = nodes.index(vertices2)
        graph[idx1][idx2] = 1


# for directed weighted graph
def add_edge_directed_w(vertices1, vertices2, cost):
    if vertices1 not in nodes:
        print(vertices1, 'is not in graph')
    if vertices2 not in nodes:
        print(vertices2, 'is not in graph')
    else:
        idx1 = nodes.index(vertices1)
        idx2 = nodes.index(vertices2)
        graph[idx1][idx2] = cost


# delete node in graph
def delete_node(vertices):
    global count_node
    if vertices not in nodes:
        print('node not in graph')
    else:
        count_node = count_node - 1
        idx1 = nodes.index(vertices)
        nodes.remove(vertices)
        graph.pop(idx1)
        for i in graph:
            i.pop(idx1)


# remove edge from node for undirected unweighted graph
def delete_edge(vertices1, vertices2):
    if vertices1 not in nodes:
        print(vertices1, 'is not in graph')
    if vertices2 not in nodes:
        print(vertices2, 'is not in graph')
    else:
        idx1 = nodes.index(vertices1)
        idx2 = nodes.index(vertices2)
        graph[idx1][idx2] = 0
        graph[idx2][idx1] = 0


# print adjacency matrix
def print_graph():
    for i in range(count_node):
        for j in range(count_node):
            print(format(graph[i][j], "<3"), end=" ")
        print()


count_node = 0
add_node('A')
add_node('B')
add_node('C')
add_edge_undirected('A', 'B')
add_edge_undirected_w('A', 'C', 12)
delete_edge('A', 'C')
delete_edge('A', 'B')
print(nodes)
print(graph)
print_graph()
