import heapq

# def aStar(graph, heuristic, start, goal):
#     open_set = [(0, start)]
#     came_from = {}
#     g_score = {node: float('inf') for node in graph}
#     g_score[start] = 0

#     while open_set:
#         _, current = heapq.heappop(open_set)

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             return path[::-1]

#         for neighbor, cost in graph[current].items():
#             tentative_g_score = g_score[current] + cost
#             if tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score = tentative_g_score + heuristic[neighbor]
#                 heapq.heappush(open_set, (f_score, neighbor))

#     return None



def aStar(graph, heuristic, start, goal):
    open_set = [(0, start)]  # Initialize the priority queue with the start node
    came_from = {}  # Keeps track of the parent node for each node in the shortest path
    g_score = {node: float('inf') for node in graph}  # The actual cost from the start node to each node
    g_score[start] = 0  # Cost from start to start is 0

    while open_set:
        _, current = heapq.heappop(open_set)  # Pop the node with the lowest f_score from the priority queue

        if current == goal:
            # If the current node is the goal, reconstruct and return the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path (from start to goal)

        # Explore neighbors of the current node
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost  # Calculate the tentative g_score
            if tentative_g_score < g_score[neighbor]:
                # If this path to the neighbor is better than any previous one, update the records
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]  # Calculate the f_score for the neighbor
                heapq.heappush(open_set, (f_score, neighbor))  # Add the neighbor to the open set

    return None  # If the open set is empty and goal not reached, no path exists




# Example usage:
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'D': 2}
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

start_node = 'A'
goal_node = 'E'

shortest_path = aStar(graph, heuristic, start_node, goal_node)
print("Shortest Path:", shortest_path)