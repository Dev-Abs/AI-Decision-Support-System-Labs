from collections import deque

graph = {
    'E': ['A', 'B'],
    'B': ['D', 'A', 'E'],
    'A': ['E', 'B', 'D'],
    'D': ['B', 'A','C'],
    'C': ['D']
}


def visit(start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)


print("bfs 'D':")
visit('D')
