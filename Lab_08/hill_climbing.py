import math 


class Node:
    def __init__(self, state, parent, actions, heuristics, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.heuristics = heuristics
        self.totalCost = totalCost


def hillClimbing():

    graph = {
        "A": Node("A", None, [("F", 1)], (0, 0), 0),
        "B": Node("B", None, [("C", 1), ("G", 1)], (0, 2), 0),
        "C": Node("C", None, [("B", 1), ("D", 1)], (0, 3), 0),
        "D": Node("D", None, [("C", 1), ("E", 1)], (0, 4), 0),
        "E": Node("E", None, [("D", 1)], (0, 5), 0),
        "F": Node("F", None, [("A", 1), ("H", 1)], (1, 0), 0),
        "G": Node("G", None, [("B", 1), ("J", 1)], (1, 2), 0),
        "H": Node("H", None, [("F", 1), ("I", 1), ("M", 1)], (2, 0), 0),
        "I": Node("I", None, [("H", 1), ("J", 1), ("N", 1)], (2, 1), 0),
        "J": Node("J", None, [("I", 1), ("G", 1)], (2, 2), 0),
        "K": Node("K", None, [("P", 1), ("L", 1)], (2, 4), 0),
        "L": Node("L", None, [("K", 1), ("Q", 1)], (2, 5), 0),
        "M": Node("M", None, [("H", 1), ("N", 1), ("R", 1)], (3, 0), 0),
        "N": Node("N", None, [("S", 1), ("I", 1)], (3, 1), 0),
        "O": Node("O", None, [("U", 1)], (3, 3), 0),
        "P": Node("P", None, [("O", 1), ("Q", 1)], (3, 4), 0),
        "Q": Node("Q", None, [("L", 1), ("P", 1), ("V", 1)], (3, 5), 0),
        "R": Node("R", None, [("M", 1), ("S", 1)], (4, 0), 0),
        "S": Node("S", None, [("N", 1), ("T", 1)], (4, 1), 0),
        "T": Node("T", None, [("S", 1), ("U", 1), ("W", 1)], (4, 2), 0),
        "U": Node("U", None, [("T", 1)], (4, 3), 0),
        "V": Node("V", None, [("Q", 1), ("Y", 1)], (4, 5), 0),
        "W": Node("W", None, [("T", 1)], (5, 2), 0),
        "X": Node("X", None, [("Y", 1)], (5, 4), 0),
        "Y": Node("Y", None, [("X", 1), ("V", 1)], (5, 5), 0),
    }

    initialState = "O"
    goalState = "Y"
    parentnode = initialState
    parentCost = math.sqrt(
        (graph[goalState].heuristics[1] - graph[initialState].heuristics[1]) ** 2
        + (graph[goalState].heuristics[0] - graph[initialState].heuristics[0]) ** 2
    )

    explored = []
    solution = []
    minChildCost = parentCost - 1
    while parentnode != goalState:
        bestnode = parentnode
        minChildCost = parentCost
        explored.append(parentnode)
        for child in graph[parentnode].actions:
            if child[0] not in explored:
                childCost = math.sqrt(
                    (graph[goalState].heuristics[1] - graph[child[0]].heuristics[1])
                    ** 2
                    + (graph[goalState].heuristics[0] - graph[child[0]].heuristics[0])
                    ** 2
                )
                if childCost < minChildCost:
                    bestnode = child[0]
                    minChildCost = childCost
        if bestnode == parentnode:
            break
        else:
            parentnode = bestnode
            parentCost = minChildCost
            solution.append(parentnode)
    return solution


solution = hillClimbing()
print(solution)