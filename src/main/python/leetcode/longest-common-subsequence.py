class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		memo = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
		
		for i, ch1 in enumerate(text1) :
			for j, ch2 in enumerate(text2) :
					curI = i + 1
					curJ = j + 1
				
					if ch1 == ch2 :			
						memo[curI][curJ] = memo[curI - 1][curJ - 1] + 1
					else :
						memo[curI][curJ] = max(memo[curI-1][curJ], memo[curI][curJ - 1])
						
		return memo[len(text1)][len(text2)]
