class Solution:
	def findLucky(self, arr: List[int]) -> int:
		
		count = {}
		for n in arr :
			count[n] = count.get(n, 0) + 1
		
		n = -1
		for k, v in count.items() :
			if k == v : 
				n = max(n, k)
		
		return n
