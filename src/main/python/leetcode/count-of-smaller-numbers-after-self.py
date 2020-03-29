import bisect

class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		
		result = [0 for i in range(len(nums))]
		sorted = []
		for i in range(len(nums)-1, -1, -1) :
			idx = bisect.bisect_left(sorted, nums[i])
			sorted.insert(idx, nums[i])
			result[i] = idx
			
		return result
