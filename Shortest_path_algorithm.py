my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B',4), ('D',7)],
    'D': [('A',1), ('C',7)]
}

def shortest_pass(gragh, start):
    unvisited = []
    distances = {}
    for node in gragh:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float("inf")
    print(f"Unvisited: {unvisited}\nDistances: {distances}")
    
shortest_pass(my_graph, "A")