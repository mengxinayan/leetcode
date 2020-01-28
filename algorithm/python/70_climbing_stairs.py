class Solution:
    def climbStairs(self, n: int) -> int:
        # F(n) = F(n-1) + F(n-2) (if n > 2)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            nums = [0, 1, 2]
            for i in range(3, n+1):
                nums.append(nums[i-1] + nums[i-2])
            return nums[n]