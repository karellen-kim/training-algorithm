class Solution(object):
    def climbStairs(self, n):
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        
        for step in range(3, n + 1) :
            memo[step] = memo[step - 1] + memo[step - 2]
        
        return memo[n]
