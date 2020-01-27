class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            if digits[0] == 9:
                return [1, 0]
            else:
                return [digits[0]+1]
        nums = digits[:] # Promise won't change digits
        nums[len(nums)-1] += 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == 10:
                nums[i] = 0
                nums[i-1] += 1
            else:
                break
        else:
            if nums[0] == 10: # [10, 0, 0]
                nums[0] = 0
                nums.insert(0, 1)
        return nums