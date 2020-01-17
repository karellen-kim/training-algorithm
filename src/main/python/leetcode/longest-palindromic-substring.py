class Solution(object):
    def longestPalindrome(self, s):

        maxPalindrome = (0, 0, 0)
        for idx, ch in enumerate(s) :
            first = self.getPalindromeLength(s, idx, idx)
            second = self.getPalindromeLength(s, idx, idx + 1)

            if first[0] > maxPalindrome[0] and first[0] > second[0] :
                maxPalindrome = first
            elif second[0] > maxPalindrome[0] and second[0] > first[0] :
                maxPalindrome = second

        return s[maxPalindrome[1]:maxPalindrome[2]]

    def getPalindromeLength(self, s, l, r) :
        while l >= 0 and r <= len(s) - 1 :
            if s[r] == s[l] :
                l -= 1
                r += 1
            else :
                break

        return (r - (l + 1), l + 1, r)

sol = Solution()
print(sol.longestPalindrome("abccecbe"))
print(sol.longestPalindrome("abccecce"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("bb"))
