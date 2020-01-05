class Solution(object):
    def sortColors(self, nums):
        start = 0
        end = len(nums) - 1

        idx = start
        while idx <= end and start <= end :
            num = nums[idx]

            if num == 0 :
                nums[idx] = nums[start]
                nums[start] = 0
                start = start + 1
                idx = start
            elif num == 2 :
                nums[idx] = nums[end]
                nums[end] = 2
                end = end - 1
            else :
                idx = idx + 1
