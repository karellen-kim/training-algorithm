class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        gIdx = 0
        sIdx = 0
        g.sort()
        s.sort()
        count = 0

        while gIdx < len(g) and sIdx < len(s) :
            if g[gIdx] <= s[sIdx] :
                gIdx += 1
                sIdx += 1
                count += 1
            else :
                sIdx += 1

        return count

solution = Solution()
assert solution.findContentChildren([1,2,3], [1,1]) == 1
assert solution.findContentChildren([1,2], [1,2,3]) == 2
