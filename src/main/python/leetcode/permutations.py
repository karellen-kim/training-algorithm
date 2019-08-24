class Solution(object):
    def __init__(self):
        self.permutations = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permuteRecursivly(nums, [])
        return self.permutations

    def permuteRecursivly(self, remain, selected):
        if len(remain) == 0 :
            self.permutations.append(selected)

        for idx, num in enumerate(remain) :
            nextRemain = remain[:idx] + remain[idx+1:]
            self.permuteRecursivly(nextRemain, selected + [num])

solution = Solution()
print(solution.permuteUnique([1,1,2]))
