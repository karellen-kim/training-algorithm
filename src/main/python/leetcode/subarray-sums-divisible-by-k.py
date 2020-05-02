class Solution:
	def subarraysDivByK(self, A: List[int], K: int) -> int:
		
		sums = {}
		contSum = 0
		count = 0
		
		for i1, num in enumerate(A) :
			contSum += num
			
			if contSum % K == 0 :
					count += 1
					
			count += sums.get(contSum % K, 0)
			sums[contSum % K] = sums.get(contSum % K, 0) + 1
		
		return count
		
