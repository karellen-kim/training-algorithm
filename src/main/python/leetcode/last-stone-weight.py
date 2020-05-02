import heapq

class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		list = []
		
		for stone in stones :
			heapq.heappush(list, stone * -1)
		
		while len(list) > 1 :
			m = heapq.heappop(list) * -1
			n = heapq.heappop(list) * -1
			
			if m - n != 0 :
				heapq.heappush(list, (m - n) * -1)
			#print("m={}, n={}, m-n={}, list={}".format(m, n, m-n, list))
		
		return heapq.heappop(list) * -1 if list else 0		
		
