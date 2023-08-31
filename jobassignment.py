import heapq
INF = float('inf')
N = 4

class Node:
    def __init__(self, workerID, jobID, assigned, parent=None):
        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.workerID = workerID
        self.jobID = jobID
        self.assigned = assigned.copy()

def newNode(x, y, assigned, parent=None):
    node = Node(x, y, assigned, parent)
    node.assigned[y] = True
    return node

def calculateCost(costMatrix, x, y, assigned):
    cost = 0
    available = [True] * N

    for i in range(x + 1, N):
        minval = INF
        minIndex = -1

        for j in range(N):
            if not assigned[j] and available[j] and costMatrix[i][j] < minval:
                minIndex = j
                minval = costMatrix[i][j]

        cost += minval
        available[minIndex] = False

    return cost

def printAssignments(minNode):
    if minNode.parent is None:
        return

    printAssignments(minNode.parent)
    print(f"Assign Worker {chr(minNode.workerID + ord('A'))} to Job {minNode.jobID}")

def findMinCost(costMatrix):
    pq = []
    assigned = [False] * N
    root = newNode(-1, -1, assigned)
    root.pathCost = root.cost = 0
    root.workerID = -1

    heapq.heappush(pq, (root.cost, root))

    while pq:
        _, minNode = heapq.heappop(pq)
        i = minNode.workerID + 1

        if i == N:
            printAssignments(minNode)
            return minNode.cost

        for j in range(N):
            if not minNode.assigned[j]:
                child = newNode(i, j, minNode.assigned, minNode)
                child.pathCost = minNode.pathCost + costMatrix[i][j]
                child.cost = child.pathCost + calculateCost(costMatrix, i, j, child.assigned)
                heapq.heappush(pq, (child.cost, child))

# costMatrix represents the cost of assigning each worker to each job
costMatrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

print("Optimal Cost is", findMinCost(costMatrix))
