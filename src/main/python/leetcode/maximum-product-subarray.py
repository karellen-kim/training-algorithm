class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0 :
            return 0

        maxProductSum = nums[0]
        maxNum = nums[0]
        minNum = nums[0]

        for num in nums[1:] :
            list = [num, maxNum * num, minNum * num]

            curMax = max(list)
            if curMax > maxProductSum :
                maxProductSum = curMax

            maxNum = max(list)
            minNum = min(list)

        return maxProductSum