class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		commonPrefix = []
		idx = 0	
		
		while True :
			if self.compare(strs, idx) :
				commonPrefix.append(strs[0][idx])
				idx += 1
			else :
				break

		return "".join(commonPrefix)

	def compare(self, strs: List[str], idx: int) :
		ch = None
		for i in range(0, len(strs)) :
			str = strs[i]
			if idx >= len(str) : 
				return False
				
			if ch == None :
				ch = str[idx]
			elif ch != str[idx] :
				return False	
			
		return True if ch != None else False
				
