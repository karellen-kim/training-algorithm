import heapq
import sys

class Pos :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def right(self):
        right = Pos(self.x+1, self.y)
        return right
    def down(self):
        down = Pos(self.x, self.y+1)
        return down
    def __str__(self):
        return "x=%d, y=%d" % (self.x, self.y)
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


# Simple : Find all Path
# Time Limit Exceeded Solution
class Solution1(object):
    def __init__(self):
        self.grid = None
        self.maxX = None
        self.maxY = None

    def minPathSum(self, grid):
        self.grid = grid
        self.maxX = len(grid)
        self.maxY = len(grid[0])
        curPos = Pos(0, 0)
        return self.__minPathSum(curPos, self.grid[curPos.x][curPos.y])

    def __minPathSum(self, curPos, weight):
        if self.isEndPos(curPos) :
            return weight

        weights = [sys.maxsize]
        nextPositions = self.next(curPos)

        for nextPos in nextPositions :
            nextWeight = weight + self.grid[nextPos.x][nextPos.y]
            heapq.heappush(weights, self.__minPathSum(nextPos, nextWeight))
        return heapq.heappop(weights)

    def next(self, pos):
        list = []
        right = pos.right()
        down = pos.down()

        if self.isValidPos(right) :
            list.append(right)
        if self.isValidPos(down) :
            list.append(down)
        return list

    def isValidPos(self, pos):
        return pos.x < self.maxX and pos.y < self.maxY

    def isEndPos(self, pos):
        if pos.x == self.maxX - 1 and pos.y == self.maxY - 1 :
            return True
        else :
            return False

grid1 = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
solution = Solution1()
print(solution.minPathSum(grid1))

class Node :
    def __init__(self, pos, weight, parent):
        self.pos = pos
        self.weight = weight
        self.parent = parent
        self.visited = False
    def __str__(self):
        return "x=%d, y=%d, weight=%d, visited=%s" % (self.pos.x, self.pos.y, self.weight, self.visited)
    def __lt__(self, other):
        return other != None and self.weight < other.weight

# A*
class Solution2(object) :
    def __init__(self):
        self.grid = None
        self.width = None
        self.height = None
        self.nodePriority = []
        self.distancePerNode = {} # 노드별 거리

    def minPathSum(self, grid) :
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])
        start = Pos(0, 0)
        node = Node(start, grid[0][0], None)
        heapq.heappush(self.nodePriority, (node.weight, node))

        while self.isDestination(node) == False : # 목적지가 아닐 때까지 반복
            node = self.getMinimunDistanceNode() # 방문하지 않은 노드중 가장 작은 짧은 노드를 찾는다
            neighbors = self.getDistanceOfNeighbors(node) # 연결된 다른 노드와 해당 노드까지의 거리 값을 가져온다
            self.upsertDistancePerNode(neighbors) # 노드별 거리에 업데이트한다
            node.visited = True # 현재 노드는 가장 짧은 경로로 이미 방문되었음

        end = Pos(self.width - 1, self.height - 1)
        return self.distancePerNode[end].weight

    def isDestination(self, node):
        return node.pos.x == self.width - 1 and node.pos.y == self.height - 1

    def getMinimunDistanceNode(self):
        priority, value = heapq.heappop(self.nodePriority)
        return value

    def upsertDistancePerNode(self, neighbors):
        for new in neighbors :
            old = self.distancePerNode.get(new.pos, None)
            if old == None :
                heapq.heappush(self.nodePriority, (new.weight, new))
            if old == None or old.weight > new.weight :
                self.distancePerNode[new.pos] = new

    def getDistanceOfNeighbors(self, node):
        list = []
        candidates = [node.pos.right(), node.pos.down()]
        for cur in candidates :
            if self.isValid(cur) :
                n = Node(cur, node.weight + self.grid[cur.x][cur.y], node)
                list.append(n)
        return list

    def isValid(self, node):
        return node.x < self.width and node.y < self.height

grid2 = [
    [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
    [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
    [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
    [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
    [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
    [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
    [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
    [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
    [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
    [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
    [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
    [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]
]

solution = Solution2()
print(solution.minPathSum(grid1))
print(solution.minPathSum(grid2))

# A*
class Solution2_1(object) :
    def __init__(self):
        self.grid = None
        self.width = None
        self.height = None
        self.nodePriority = []
        self.distancePerNode = {} # 노드별 거리

    def minPathSum(self, grid) :
        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])
        start = (0, 0)
        node = (start, grid[0][0], None)
        pos, weight, parent = node
        heapq.heappush(self.nodePriority, (weight, node))

        while self.isDestination(node) == False : # 목적지가 아닐 때까지 반복
            node = self.getMinimunDistanceNode() # 방문하지 않은 노드중 가장 작은 짧은 노드를 찾는다
            neighbors = self.getDistanceOfNeighbors(node) # 연결된 다른 노드와 해당 노드까지의 거리 값을 가져온다
            self.upsertDistancePerNode(neighbors) # 노드별 거리에 업데이트한다

        end = (self.width - 1, self.height - 1)
        pos, weight, parent = self.distancePerNode[end]
        return weight

    def isDestination(self, node):
        (x, y), weight, parent = node
        return x == self.width - 1 and y == self.height - 1

    def getMinimunDistanceNode(self):
        priority, value = heapq.heappop(self.nodePriority)
        return value

    def upsertDistancePerNode(self, neighbors):
        for new in neighbors :
            pos, weight, parent = new

            old = self.distancePerNode.get(pos, None)
            if old == None :
                heapq.heappush(self.nodePriority, (weight, new))
            if old == None or old[1] > weight :
                self.distancePerNode[pos] = new

    def getDistanceOfNeighbors(self, node):
        (x, y), weight, parent = node
        list = []
        candidates = [(x+1, y), (x, y+1)]
        for cur in candidates :
            if self.isValid(cur) :
                n = (cur, weight + self.grid[cur[0]][cur[1]], node)
                list.append(n)
        return list

    def isValid(self, pos):
        x, y = pos
        return x < self.width and y < self.height
grid1 = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
grid2 = [
    [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
    [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
    [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
    [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
    [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
    [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
    [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
    [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
    [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
    [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
    [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
    [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]
]

solution = Solution2_1()
print(solution.minPathSum(grid1))
print(solution.minPathSum(grid2))

class Grid :
    X = 0
    Y = 1
    def __init__(self, grid):
        self.grid = grid
    def getWeight(self, pos):
        return self.grid[pos[self.X]][pos[self.Y]]
    def neighbors(self, pos):
        list = []
        for n in [(pos[self.X] + 1, pos[self.Y]), (pos[self.X], pos[self.Y] + 1)] :
            if n[self.X] < len(self.grid) and n[self.Y] < len(self.grid[0]) :
                list.append(n)
        return list

# Refactoring
class Solution2_2 :
    WEIGHT = 0

    def minPathSum(self, G) :
        return self.shorteast(G, (0,0), (len(G)-1, len(G[0])-1))

    def shorteast(self, G, start, end) :
        grid = Grid(G)
        visited = {}
        shorteast = {}
        cur = start
        q = [(grid.getWeight(cur), cur, [cur])]

        while q :
            (weight, cur, path) = heapq.heappop(q)

            for n in grid.neighbors(cur) :
                if n not in visited :
                    newWeight = weight + grid.getWeight(n)
                    if n not in shorteast :
                        heapq.heappush(q, (newWeight, n, path + [n]))
                    if n not in shorteast or newWeight < shorteast[n][self.WEIGHT] :
                        shorteast[n] = (newWeight, n, path + [n])
            visited[cur] = True
        return shorteast[end][self.WEIGHT]

solution = Solution2_2()
print(solution.minPathSum(grid1))
print(solution.minPathSum(grid2))

# Best
class Solution3 :
    def minPathSum(self, grid) :
        row = len(grid)
        col = len(grid[0])
        for i in range(1, row) :
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(1, col) :
            grid[0][j] = grid[0][j - 1] + grid[0][j]
        for i in range(1, row) :
            for j in range(1, col) :
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][col-1]

solution = Solution3()
print(solution.minPathSum(grid1))
print(solution.minPathSum(grid2))