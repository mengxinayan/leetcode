class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        res = True
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                res = False
        return res
