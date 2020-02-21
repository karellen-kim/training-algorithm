class Solution(object):
	def rob(self, nums):
		
		if len(nums) == 0 :
			return 0
		elif len(nums) < 3 :
			return max(nums)
		
		moneyFrom0 = nums[0:]
		moneyFrom1 = nums[0:]
		maxMoney = max(nums[0], nums[1])
		length = len(nums)
		
		for idx in range(2, length) : 
			num = nums[idx]
			
			if idx != length - 1 : 
				for i in range(0, idx - 2 + 1) :
					moneyFrom0[idx] = max(moneyFrom0[idx], num + moneyFrom0[i])
		
			for i in range(1, idx - 2 + 1) :
				moneyFrom1[idx] = max(moneyFrom1[idx], num + moneyFrom1[i])
		
			maxMoney = max(maxMoney, moneyFrom0[idx], moneyFrom1[idx])
			
		return maxMoney
