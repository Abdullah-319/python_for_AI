import heapq

def aStar(graph, heuristicValues, startNode, goalNode):
    openSet = [(0, startNode)] 
    visitedNodes = {}  
    gScore = {node: float('inf') for node in graph}  
    gScore[startNode] = 0 

    while openSet:
        _, currentNode = heapq.heappop(openSet) 

        if currentNode == goalNode:
            path = []
            while currentNode in visitedNodes:
                path.append(currentNode)
                currentNode = visitedNodes[currentNode]
            path.append(startNode)
            pathCost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))  
            return path[::-1], pathCost 

        for neighbor, cost in graph[currentNode].items():
            tempScore = gScore[currentNode] + cost
            if tempScore < gScore[neighbor]:
                visitedNodes[neighbor] = currentNode
                gScore[neighbor] = tempScore
                finalScore = tempScore + heuristicValues[neighbor] 
                heapq.heappush(openSet, (finalScore, neighbor)) 

    return None, None

myGraph = {
    'A': {'B': 6, 'C': 9, 'E': 1},
    'B': {'A': 6, 'E': 4, 'D': 3},
    'C': {'A': 9, 'F': 2, 'G': 3},
    'D': {'B': 3, 'E': 5, 'F': 7},
    'E': {'A': 1, 'B': 4, 'D': 5, 'F': 6},
    'F': {'C': 2, 'D': 7, 'E': 6},
    'G': {'C': 3},
}

heuristicValues = {
    'A': 7,
    'B': 5,
    'C': 5,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 0,
}

startNode = 'A'
goalNode = 'G'

shortestPath, totalCost = aStar(myGraph, heuristicValues, startNode, goalNode)
print("Shortest Path:", shortestPath)
print("Total Cost:", totalCost)
