import sys
sys.setrecursionlimit(10000)

################################################################################
# Time Limit Exceeded Solution : BFS
################################################################################

class TimeLimitExceededSolution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        self.NOT_FOUND = -1
        self.dst = dst
        self.K = K
        self.connectedFlights = self.initConnectedFlights(n, flights, src, dst, K)
        return self.search(src, 0, 0)

    def search(self, index, cost, depth):
        if depth > (self.K + 1) :
            return self.NOT_FOUND
        elif index == self.dst :
            return cost
        else :
            list = []
            for child in self.connectedFlights[index] :
                childCost = self.search(child[0], cost + child[1], depth + 1)
                if childCost != -1 :
                    list.append(childCost)
            return self.min(list)

    def initConnectedFlights(self, n, flights, src, dst, K):
        connectedFlights = [[] for i in range(n)]

        for flight in flights :
            index = flight[0]
            childIndex = flight[1]
            cost = flight[2]
            connectedFlights[index].append((childIndex, cost))
        return connectedFlights

    def min(self, list):
        if len(list) == 0 :
            return self.NOT_FOUND
        else :
            return min(list)

solutionV1 = TimeLimitExceededSolution()
cost = solutionV1.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print(cost)


################################################################################
# Accepted Solution : Dijkstra's Algorithm
################################################################################

class Solution(TimeLimitExceededSolution) :
    def findCheapestPrice(self, n, flights, src, dst, K):
        self.NOT_FOUND = 0
        self.dst = dst
        self.K = K
        self.connectedFlights = self.initConnectedFlights(n, flights, src, dst, K)
        self.costs = [[self.NOT_FOUND, 0] for i in range(n)]
        self.visited = [False for i in range(n)]

        self.search(src)
        cost = self.getCost(dst)
        if cost == self.NOT_FOUND :
            return -1
        else :
            return cost

    def search(self, index):
        self.visited[index] = True

        currentCost = self.getCost(index)
        currentStopCount = self.getStopCount(index)

        for nextStop in self.connectedFlights[index] :
            nextStopIndex = nextStop[0]
            if self.visited[nextStopIndex] == False :
                nextStopCost = nextStop[1]
                totalCost = currentCost + nextStopCost

                if currentStopCount <= self.K and (self.getCost(nextStopIndex) == self.NOT_FOUND or self.getCost(nextStopIndex) > totalCost) :
                    self.setCost(nextStopIndex, totalCost, currentStopCount + 1)
                self.search(nextStopIndex)

    def setCost(self, index, cost, stopCount):
        self.costs[index] = [cost, stopCount]

    def getCost(self, index):
        return self.costs[index][0]

    def getStopCount(self, index):
        return self.costs[index][1]

solutionV2 = Solution()
#cost = solutionV2.findCheapestPrice(17,
#                                  [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
#                                  , 13, 4, 13)
print(cost)

cost = solutionV2.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
print(cost)