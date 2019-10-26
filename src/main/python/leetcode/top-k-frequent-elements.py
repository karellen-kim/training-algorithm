class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums :
            map[num] = map.get(num, 0) + 1

        result = sorted(map, key=lambda x : map[x], reverse=True)
        return result[:k]

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))