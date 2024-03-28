import heapq

class Graph:
    def __init__(self, graph_dict):
        self.graph = graph_dict

    def heuristic(self, node, goal):
        # Define a simple heuristic function.
        # In this case, we'll use a dictionary to store the heuristic values for each node.
        heuristic_values = {"a": 3, "b": 2, "c": 2, "d": 1, "e": 0}
        return heuristic_values[node]

    def a_star(self, start, goal):
        open_list = [(0, start)]  # (f_score, node)
        closed_set = set()
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        parent = {}

        while open_list:
            f_score, current = heapq.heappop(open_list)
            if current == goal:
                path = []
                while current in parent:
                    path.append(current)
                    current = parent[current]
                path.append(start)
                return path[::-1]  # Return reversed path
            closed_set.add(current)
            for neighbor, weight in self.graph[current].items():
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
        return None  # No path found

# Define the graph
graph_dict = {
    "a": {"b": 4, "c": 3},
    "b": {"c": 3, "a": 4, "d": 5},
    "c": {"a": 3, "b": 2, "d": 1},
    "d": {"b": 5, "c": 1, "e": 2},
    "e": {"d": 2}
}

graph = Graph(graph_dict)

# Run A* search
start_node = "a"
goal_node = "e"
path = graph.a_star(start_node, goal_node)

if path:
    print("Shortest path:", path)
    print("Length of shortest path:", len(path) - 1)  # Subtract 1 to get the number of edges
else:
    print("No path found.")




# Write A* pseudo code and match this algorithm.