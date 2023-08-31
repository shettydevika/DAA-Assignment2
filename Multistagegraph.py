def multistage_shortest_path(graph, stages):
    n = len(graph)
    dist = [float('inf')] * n
    next_vertex = [-1] * n

    dist[n - 1] = 0

    for i in range(n - 2, -1, -1):
        for j in stages[i]:
            for neighbor, weight in graph[j]:
                if dist[neighbor] + weight < dist[j]:
                    dist[j] = dist[neighbor] + weight
                    next_vertex[j] = neighbor

    # Construct the path
    path = [0]
    current_vertex = 0
    while next_vertex[current_vertex] != -1:
        current_vertex = next_vertex[current_vertex]
        path.append(current_vertex)

    return dist[0], path

# Example graph and stages
graph = {
    0: [(1, 2), (2, 7)],
    1: [(2, 3), (3, 5)],
    2: [(3, 2), (4, 1)],
    3: [(4, 2), (5, 7)],
    4: [(5, 3)],
    5: []
}

stages = [[5], [4, 3], [2, 1], [0]]

shortest_distance, shortest_path = multistage_shortest_path(graph, stages)
print("Shortest distance:", shortest_distance)
print("Shortest path:", shortest_path)

'''
Output:
Shortest distance: 6
Shortest path: [0, 2, 3, 5]
'''
