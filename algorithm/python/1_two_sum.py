class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List_dic = {}
        for i in range(0, len(nums)):
            List_dic[nums[i]] = i
        for i in range(0, len(nums)):
            res = List_dic.get(target-nums[i], -1)
            if res != -1 and res != i:
                return [i, res]
