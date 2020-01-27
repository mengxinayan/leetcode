class Solution:
    def reverse(self, x: int) -> int:
        '''
        32 bit signed integer
        2^31-1 = 2147483647
        -2^31 = -2147483648
        '''
        if x == 0:
            return 0
        falg = 1
        nums = list(str(x))
        if nums[0] == '-':
            falg = -1
            nums = nums[1:]
        nums.reverse()
        while(nums[0] == '0'):
            nums = nums[1:]
        res = int(nums[0])
        for i in range(1, len(nums)):
            res = res * 10 + int(nums[i])
        res = res * falg
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            return res
