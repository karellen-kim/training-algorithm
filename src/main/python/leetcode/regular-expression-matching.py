import sys
sys.setrecursionlimit(1000)

# star 없는 경우
class Solution_V1(object):
    def isMatch(self, str, pattern):
        if not pattern :
            return not str
        elif pattern[0] == str[0] or pattern[0] == '.' :
            return self.isMatch(str[1:], pattern[1:])
        else :
            return False

solution = Solution_V1()
assert solution.isMatch("aa", "a") == False
assert solution.isMatch("aa", ".a") == True
assert solution.isMatch("aabc", ".a.c") == True

# start 포함
class Solution_V2(object):
    def isMatch(self, str, pattern):
        if not pattern :
            return not str
        elif pattern[0] == '*':
            if not str :
                return self.isMatch(str, pattern[1:])
            else :
                return self.isMatch(str[1:], pattern)
        elif pattern[0] == '.' :
            return self.isMatch(str[1:], pattern[1:])
        elif pattern[0] == str[0] :
            return self.isMatch(str[1:], pattern[1:])
        else :
            return False

solution = Solution_V2()
assert solution.isMatch("aa", "a") == False
assert solution.isMatch("aa", ".a") == True
assert solution.isMatch("aa", "a*") == True
assert solution.isMatch("aab", "c*a*b") == True
assert solution.isMatch("mississippi", "mis*is*p*.") == True
