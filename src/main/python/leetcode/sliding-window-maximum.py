import heapq

class Solution(object):
    def maxSlidingWindow(self, numbers, windowSize):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(numbers) == 0 or windowSize == 0 :
            return []

        result = []

        maxHeap = []
        # 최초 윈도우 사이즈 만큼 추가한다
        for i in range(0, windowSize) :
            heapq.heappush(maxHeap, (numbers[i] * -1, i * -1))
        maxValue = maxHeap[0]
        result.append(maxValue[0] * -1)

        for idx in range(windowSize, len(numbers)) :
            heapq.heappush(maxHeap, (numbers[idx] * -1, idx * -1))
            cur = maxHeap[0]
            while len(maxHeap) > 0 :
                indexOfMaxValue = cur[1] * -1
                if indexOfMaxValue < idx - windowSize + 1 :
                    cur = heapq.heappop(maxHeap)
                else :
                    break
            result.append(cur[0] * -1)

        return result

solution = Solution()
result = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(result)