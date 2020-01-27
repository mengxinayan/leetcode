class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '': # 第一次漏掉了这种情况
            return 0
        res = 0
        index = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                index = i
                break
        for i in range(index, -1, -1):
            if s[i] != ' ':
                res += 1
            else:
                break
        return res