class Solution(object):
    def validPalindrome(self, s):
        head = 0
        tail = len(s) - 1

        while head < tail :
            if s[head] != s[tail] :
                return self.isPalindrome(s[head + 1:tail + 1]) or self.isPalindrome(s[head:tail])
            else :
                head += 1
                tail -= 1

        return True

    def isPalindrome(self, s) :
        head = 0
        tail = len(s) - 1

        while head < tail :
            if s[head] != s[tail] :
                return False
            head += 1
            tail -= 1

        return True
