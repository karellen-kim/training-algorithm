class Solution(object):
	def isAnagram(self, s, t):
		list = [0 for i in range(0, self.toNum('z') + 1)]
		
		for ch in s :
			num = self.toNum(ch)
			list[num] = list[num] + 1
		
		for ch in t :
			num = self.toNum(ch)
			if list[num] <= 0 :
				return False
			else :
				list[num] = list[num] - 1
			
		return sum(list) == 0
			
		
	def toNum(self, ch) :
		return ord(ch) - ord('a')
		
		
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "cat"))
print(sol.isAnagram("zlap", "kcqx"))
