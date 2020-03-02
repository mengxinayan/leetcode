# Solution 1

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch_dict = {}
        for i in range(len(t)):
            if t[i] not in ch_dict:
                ch_dict[t[i]] = 1
            else:
                ch_dict[t[i]] += 1
        res = ''
        for i in range(len(s)):
            if s[i] in ch_dict:
                if ch_dict[s[i]] == 1:
                    del ch_dict[s[i]]
                else:
                    ch_dict[s[i]] -= 1
            else:
                res = s[i]
                break
        else:
            res = list(ch_dict.keys())[0]
        return res


# Solution 2

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum2 = 0
        for i in range(len(s)):
            sum1 += ord(s[i])
        for i in range(len(t)):
            sum2 += ord(t[i])
        return chr(sum2 - sum1)
