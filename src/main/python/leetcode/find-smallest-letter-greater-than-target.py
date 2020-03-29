from typing import List
import bisect

class Solution:
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:	
		nums = list([ord(item) for item in letters])
		nums.sort()
		lastIdx = len(nums) - 1
		
		targetNum = ord(target)
		idx = bisect.bisect_right(nums, targetNum)
		
		idx = min(idx, lastIdx)
		
		if nums[idx] <= targetNum :
			if idx == lastIdx :
				idx = 0
			else :
				idx = idx + 1
				
		return chr(nums[idx])
