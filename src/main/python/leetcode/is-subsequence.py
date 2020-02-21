class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		length = len(s)
		if length	== 0 :
			return True
		
		idx = 0
		for ch in t :
			if s[idx] == ch :
				idx += 1
				
				if idx == length :
					return True
		
		return False

