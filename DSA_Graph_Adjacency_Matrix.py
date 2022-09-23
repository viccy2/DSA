# implementing Graph using Adjacency Matrix

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


# print adjacency matrix
def print_graph():
    for i in range(count_node):
        for j in range(count_node):
            print(graph[i][j], end=" ")
        print()


count_node = 0
add_node('A')
add_node('B')
add_node('C')
print(nodes)
print(graph)
print_graph()
