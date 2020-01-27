class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1 = len(haystack)
        length2 = len(needle)
        if length1 > length2:
            res = -1
            for i in range(0, length1-length2+1):
                # Why '+1'? -> "aab" "ab"
                if haystack[i:i+length2] == needle:
                    res = i
                    break
            return res
        elif length1 == length2:
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            return -1