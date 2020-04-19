import sys

class Solution:
	def find132pattern(self, nums: List[int]) -> bool:	
		
		list = []
		minNum = sys.maxsize
		for n in nums :
			# keep big number in list : 5, 4, 3
			while list and list[-1][0] <= n :
				list.pop()
			
			if list and list[-1][1] < n :
				return True
					
			minNum = min(minNum, n)
			list.append((n, minNum))
		
		return False

