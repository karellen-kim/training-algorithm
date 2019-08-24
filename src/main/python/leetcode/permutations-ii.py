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

        used = set()
        for idx, num in enumerate(remain) :
            if (num in used) == False :
                used.add(num)
                nextRemain = remain[:idx] + remain[idx+1:]
                self.permuteRecursivly(nextRemain, selected + [num])

solution = Solution()
print(solution.permuteUnique([1,1,2]))
