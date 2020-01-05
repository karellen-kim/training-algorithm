import heapq

class Solution(object):
    def kClosest(self, points, K):
        list = []

        for idx, point in enumerate(points) :
            dist = (point[0] * point[0] + point[1] * point[1])

            if len(list) >= K and (list[0][0] * -1) > dist :
                heapq.heappop(list)

            if len(list) < K :
                heapq.heappush(list, (dist * -1, idx))

        closest = []
        while list :
            maxVal = heapq.heappop(list)
            closest.append(points[maxVal[1]])

        return closest
