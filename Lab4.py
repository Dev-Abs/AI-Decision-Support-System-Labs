# # Task 1, 2
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("pop from empty stack")
#
#
# def dfs_recursive(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end=' ')
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)
#
# def dfs_iterative(graph, start):
#     visited = set()
#     stack = Stack()
#     stack.push(start)
#     while not stack.is_empty():
#         vertex = stack.pop()
#         if vertex not in visited:
#             print(vertex, end=' ')
#             visited.add(vertex)
#             for neighbor in graph[vertex]:
#                 if neighbor not in visited:
#                     stack.push(neighbor)
#
# # Graph 1
# graph1 = {
#     6: [4],
#     4: [5, 3],
#     5: [1, 2, 4],
#     1: [2, 5],
#     2: [3, 1, 5],
#     3: [2, 4]
# }
#
# # Graph 2
# graph2 = {
#     'E': ['B', 'A'],
#     'B': ['A', 'E', 'D'],
#     'A': ['D', 'B', 'E'],
#     'D': ['C', 'A', 'B'],
#     'C': ['D']
# }
#
# print("DFS Recursive for Graph 1 starting from node 6:")
# dfs_recursive(graph1, 6)
# print("\nDFS Iterative for Graph 1 starting from node 6:")
# dfs_iterative(graph1, 6)
#
# print("\nDFS Recursive for Graph 2 starting from node E:")
# dfs_recursive(graph2, 'E')
# print("\nDFS Iterative for Graph 2 starting from node E:")
# dfs_iterative(graph2, 'E')

# Task 3
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         print(node.value, end=' ')
#         pre_order(node.left)
#         pre_order(node.right)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value, end=' ')
#         in_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value, end=' ')
#
# # Construct Tree 1
# tree1 = TreeNode(1)
# tree1.left = TreeNode(2)
# tree1.right = TreeNode(3)
# tree1.left.left = TreeNode(4)
# tree1.left.right = TreeNode(5)
# tree1.left.left.left = TreeNode(6)
# tree1.left.right.left = TreeNode(7)
# tree1.left.right.right = TreeNode(8)
#
# # Construct Tree 2
# tree2 = TreeNode(50)
# tree2.left = TreeNode(17)
# tree2.right = TreeNode(76)
# tree2.left.left = TreeNode(9)
# tree2.left.right = TreeNode(23)
# tree2.left.left.right = TreeNode(14)
# tree2.left.left.right.left = TreeNode(12)
# tree2.left.right.left = TreeNode(19)
# tree2.right.left = TreeNode(54)
# tree2.right.left.right = TreeNode(72)
# tree2.right.left.right.left = TreeNode(67)
#
# print("Tree 1 Pre-Order Traversal:")
# pre_order(tree1)
# print("\nTree 1 In-Order Traversal:")
# in_order(tree1)
# print("\nTree 1 Post-Order Traversal:")
# post_order(tree1)
#
# print("\n\nTree 2 Pre-Order Traversal:")
# pre_order(tree2)
# print("\nTree 2 In-Order Traversal:")
# in_order(tree2)
# print("\nTree 2 Post-Order Traversal:")
# post_order(tree2)


# Task 4
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")


def dfs_image(image, start_pixel):
    rows = len(image)
    cols = len(image[0])

    # Find the coordinates of the start pixel (150)
    start_position = None
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == start_pixel:
                start_position = (i, j)
                break
        if start_position:
            break

    if start_position is None:
        print("Start pixel not found in the image.")
        return

    visited = set()
    stack = Stack()
    stack.push(start_position)

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while not stack.is_empty():
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            print(image[x][y], end=' ')

            # Explore the 4-connected neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    stack.push((nx, ny))


# Image represented as a 2D list
image = [
    [150, 2, 5],
    [80, 145, 45],
    [74, 102, 165]
]

# Start DFS traversal from pixel 150
print("DFS traversal starting from pixel 150:")
dfs_image(image, 150)

