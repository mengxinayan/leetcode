class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if (i >= 1) and (nums[i] == nums[i-1]):
                continue
            for j in range(i+1, len(nums)-2):
                if (j > i+1) and (nums[j] == nums[j-1]):
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp_sum < target:
                        left += 1
                    elif tmp_sum > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while (left < right) and (nums[left+1] == nums[left]):
                            left += 1
                        while (left < right) and (nums[right-1] == nums[right]):
                            right -= 1
                        left += 1
                        right -= 1
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2022  mengxinayan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
