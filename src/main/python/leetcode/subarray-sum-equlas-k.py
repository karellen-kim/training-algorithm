class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		
		sumDic = collections.Counter()
		
		sum = 0
		count = 0
		for num in nums :
			sum += num
			
			diff = sum - k
			if diff == 0 and sumDic[0] == 0 :
				sumDic[0] = 1
			
			count += sumDic[diff]
			sumDic[sum] += 1
		
		return count
