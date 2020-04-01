class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		mem = 0
		for num in nums :
			mem = mem ^ num
		
		return mem
