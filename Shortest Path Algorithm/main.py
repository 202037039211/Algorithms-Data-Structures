# Sample graph represented as an adjacency list with weighted edges
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Initialize all distances to infinity, except the starting node (0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Tracks paths for each node
    paths = {node: [] for node in graph}
    paths[start] = [start]
    
    # List of unvisited nodes
    unvisited = set(graph.keys())
    
    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=lambda node: distances[node])
        
        # Iterate over neighbors of the current node
        for neighbor, distance in graph[current]:
            new_distance = distances[current] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Update the path to the current neighbor
                paths[neighbor] = paths[current] + [neighbor]
        
        # Remove the current node from the unvisited set
        unvisited.remove(current)
    
    # Determine which targets to print (all nodes or a specific one)
    targets_to_print = [target] if target else graph
    
    for node in targets_to_print:
        if node == start:
            continue  # Skip the starting node
        print(f'\n{start} to {node} distance: {distances[node]}')
        print(f'Path: {" -> ".join(paths[node])}')
    
    return distances, paths

# Example call: Find shortest paths from node 'A' to all other nodes
shortest_path(my_graph, 'A')
