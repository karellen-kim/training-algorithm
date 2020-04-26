class Solution:
	def nextGreaterElements(self, nums: List[int]) -> List[int]:
		
		stack = []
		result = [0 for i in range(len(nums))]
		
		for count in range(len(nums) * 2 - 1, -1, -1) :
			idx = count % len(nums)
			num = nums[idx]	
			
			while stack and num >= stack[-1] :
				stack.pop()
			
			result[idx] = stack[-1] if stack else -1
			stack.append(num)
			
		return result
		
