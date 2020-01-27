class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        lens = []
        for i in range(len(strs)):
            lens.append(len(strs[i]))
        minlen = min(lens)
        res = ''
        for i in range(minlen):
            ch = strs[0][i]
            falg = True
            for j in range(1, len(strs)):
                if ch != strs[j][i]:
                    falg = False
            if falg == True:
                res += ch
            else:
                break
        return res