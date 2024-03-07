# subjects = []
# marks = []
# result = {}

# for i in range(2):
#     subject = input("Enter subject name: ")
#     mark = float(input("Enter it's marks: "))
#     subjects.append(subject)
#     marks.append(mark)

# for i in range(2):
#     result[subjects[i]] = marks[i]

# print(result)

   








# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         self.graph[u].append(v)

#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])
#         visited.add(start)

#         while queue:
#             vertex = queue.popleft()
#             print(vertex, end=" ")

#             for neighbour in self.graph[vertex]:
#                 if neighbour not in visited:
#                     queue.append(neighbour)
#                     visited.add(neighbour)

# # Example usage:
# g = Graph()
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 5)
# g.add_edge(2, 6)
# g.add_edge(4, 7)
# g.add_edge(4, 8)
# g.add_edge(5, 9)
# g.add_edge(5, 10)
# g.add_edge(7, 11)
# g.add_edge(7, 12)

# print("BFS Traversal starting from vertex 2:")
# g.bfs(1)








from collections import defaultdict

class Graph:
    def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph[vertex])

# Define the graph G
G = {
    'A': ['B', 'E', 'C'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# Create a Graph object and add edges from G
g = Graph()
for vertex, neighbors in G.items():
    for neighbor in neighbors:
        g.add_edge(vertex, neighbor)

# Perform BFS traversal starting from vertex 'C'
print("BFS Traversal starting from vertex 'C':")
g.bfs('C')