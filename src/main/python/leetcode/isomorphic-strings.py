class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t) :
            return False

        map = {}
        for idx in range(len(s)) :
            mappedChar = map.get(s[idx])
            if mappedChar == None :
                map[s[idx]] = t[idx]

            if t[idx] != map[s[idx]] :
                return False

        return True

solution = Solution()
print(solution.isIsomorphic("egg", "addee"))
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))
print(solution.isIsomorphic("ab", "aa"))
