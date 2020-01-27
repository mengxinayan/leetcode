class Solution:
    def isValid(self, s: str) -> bool:
        # 只输入一个右括号"]"
        if len(s) == 0:
            return True
        chs = []
        res = False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                chs.append(s[i])
            elif s[i] == ')':
                if len(chs) == 0 or chs[-1] != '(':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            elif s[i] == ']':
                if len(chs) == 0 or chs[-1] != '[':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            elif s[i] == '}':
                if len(chs) == 0 or chs[-1] != '{':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            else:
                pass
        if len(chs) == 0:
            res = True
        return res