class Solution(object):
    def subsets(self, nums):
        self.result = [[]]
        self.__subsets(nums, [])
        return self.result

    def __subsets(self, remain, subSet) :
        if len(remain) == 0 :
            return
        else :
            newSubSet = subSet[:]
            newSubSet.append(remain[0])
            self.result.append(newSubSet)

            self.__subsets(remain[1:], subSet)
            self.__subsets(remain[1:], newSubSet)

solution = Solution()
print(solution.subsets([1,2,3]))