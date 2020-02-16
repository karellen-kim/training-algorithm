class Solution(object):
	def rob(self, nums):
		if len(nums) == 0 :
			return 0
		elif len(nums) < 3 :
			return max(nums)
			
		result = nums[0:]
		maxMoney = max(nums[0], nums[1])
		
		for idx in range(2, len(nums)) :
			num = nums[idx]
			
			for i in range(0, idx - 2 + 1) :
				result[idx] = max(result[idx], num + result[i])
		
			maxMoney = max(maxMoney, result[idx])

		return maxMoney
