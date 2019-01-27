from collections import defaultdict

class VisitMarker:
    def __init__(self, size):
        self.visited = [False for i in range(size)]
        self.recStack = [False for i in range(size)]

    def visit(self, v):
        self.visited[v] = True
        self.recStack[v] = True

    def isVisited(self, v):
        return self.visited[v]

    def isVisitedRecStack(self, v):
        return self.recStack[v]

    def unvisitedRecStack(self, v):
        self.recStack[v] = False

    def toString(self):
        visitIndexes = []
        for i in range(len(self.visited)):
            if self.visited[i] == True:
                visitIndexes.append(str(i))
        return ",".join(visitIndexes)

def isCyclic(n, graph):
    marker = VisitMarker(n)
    for v in list(graph):
        if marker.isVisited(v) == False:
            if checkCyclicInVertex(graph, v, marker) == True:
                return True
    return False

def checkCyclicInVertex(graph, v, marker):
    marker.visit(v)

    for nextVertex in graph[v]:
        if marker.isVisited(nextVertex) == False :
            if checkCyclicInVertex(graph, nextVertex, marker) == True :
                return True
        elif marker.isVisitedRecStack(nextVertex) == True:
            return True
    marker.unvisitedRecStack(v)
    return False

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    inputs = [
        [1, "2 2", "0 1 0 0"],
        [0, "4 3", "0 1 1 2 2 3"],
        [0, "29 4", "6 21 17 12 2 11 9 11"],
        [1, "84 87", "9 19 29 31 10 72 57 73 2 19 62 67 83 70 24 78 16 16 59 56 75 9 2 26 26 55 43 19 5 42 66 54 17 51 1 28 79 58 57 81 33 35 20 73 62 44 23 78 17 82 7 8 8 9 74 74 64 73 9 69 32 75 80 5 82 81 73 77 12 3 30 45 38 51 74 56 51 14 7 24 12 14 32 60 63 23 50 43 12 60 68 0 7 64 46 6 18 35 39 70 38 70 71 33 77 62 45 0 76 8 25 44 62 13 21 41 76 71 40 45 3 25 45 11 45 47 57 19 39 52 5 33 78 77 22 71 11 68 28 3 32 53 3 11 66 24 52 59 52 9 60 11 74 61 62 75 25 35 11 64 44 56 13 38 49 76 26 16 60 10 59 8 63 63"],
        [0, "88 13", "12 28 67 17 0 26 30 11 38 85 57 60 57 15 75 31 65 80 75 19 68 67 73 84 63 86"]
    ]
    for i in range(len(inputs)):
        n, e = list(map(int, inputs[i][1].strip().split()))
        arr = list(map(int, inputs[i][2].strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)