from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, initial, next):
        self.graph[initial].append(next)

    def dfs(self, start, end, visited=[], path=[]):
        visited = visited + [start]

        if start == end:
            return path + [start]

        shortest_path = None
        for vertex in self.graph[start]:
            if vertex not in visited:
                new_path = self.dfs(vertex, end, visited, path + [start])
                if new_path:
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        shortest_path = new_path

        return shortest_path

sirGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A','E'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'C'],
    'F': ['C', 'G', 'H', 'I'],
    'G': ['D', 'F', 'J'],
    'H': ['F'],
    'I': ['F'],
    'J': ['G'],
}

myGraph = Graph()

for vertex, neighbors in sirGraph.items():
    for neighbor in neighbors:
        myGraph.addEdge(vertex, neighbor)


print("Shortest path from A to J:", " -> ".join(myGraph.dfs('A', 'J')))


# print("Shortest path from A to I:", " -> ".join(myGraph.dfs('A', 'I')))
