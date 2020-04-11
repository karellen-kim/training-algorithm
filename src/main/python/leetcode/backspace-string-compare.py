class Solution:
	def backspaceCompare(self, S: str, T: str) -> bool:
		return self.showing(S) == self.showing(T)
		
	def showing(self, str) :
		stack = []
		for ch in str :
			if ch == '#' :
				if len(stack) != 0 :
					stack.pop()
			else :
				stack.append(ch)
		
		return "".join(stack)
