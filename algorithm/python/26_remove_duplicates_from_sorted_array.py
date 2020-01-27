class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tmp = nums[0]
        res = 1
        length = len(nums)
        for i in range(1, length):
            if tmp != nums[res]:
                tmp = nums[res]
                res = res + 1
            else:
                nums.pop(res)
        return res