graph = [
    [0, 5, float('inf'), 6, float('inf')],
    [5, 0, 9, float('inf'), 7],
    [float('inf'), 9, 0, float('inf'), 9],
    [6, float('inf'), float('inf'), 0, 5],
    [float('inf'), 7, 9, 5, 0]
]

def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(len(graph))}
    D[start_vertex] = 0

    unvisited_vertices = list(range(len(graph)))

    while unvisited_vertices:
        min_vertex = None
        for vertex in unvisited_vertices:
            if min_vertex is None:
                min_vertex = vertex
            elif D[vertex] < D[min_vertex]:
                min_vertex = vertex

        for neighbor_index, weight in enumerate(graph[min_vertex]):
            if weight != float('inf'):
                alternative_route = D[min_vertex] + weight
                if alternative_route < D[neighbor_index]:
                    D[neighbor_index] = alternative_route

        unvisited_vertices.remove(min_vertex)

    return D

shortest_paths = dijkstra(graph, 0)
shortest_path_to_V3 = shortest_paths[2]

print(f"The shortest path from V1 to V3 is {shortest_path_to_V3}")