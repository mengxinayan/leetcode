class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length):
            if nums[res] == val:
                nums.pop(res)
            else:
                res = res + 1
        return res