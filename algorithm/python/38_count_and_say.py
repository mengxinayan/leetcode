class Solution:
    def countAndSay(self, n: int) -> str:

        def read(string: str) -> str:
            tmp = ''
            num = 0
            res = ''
            for i in range(0, len(string)):
                if string[i] == tmp:
                    num += 1
                else:
                    if i != 0:
                        res = res + str(num) + tmp
                    tmp = string[i]
                    num = 1
            res = res + str(num) + tmp
            return res
        
        res = '1'
        for i in range(n-1):
            res = read(res)
        return res