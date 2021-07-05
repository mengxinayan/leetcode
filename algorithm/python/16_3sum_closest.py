class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = min_diff = float('inf')
        for i in range(len(nums)-2):
            # Some details
            if ans == target:
                break
            if (i >= 1) and (nums[i] == nums[i-1]):
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                tmp_diff = abs(tmp_sum - target)
                if tmp_diff < min_diff:
                    min_diff = tmp_diff
                    ans = tmp_sum
                if tmp_sum < target:
                    left += 1
                elif tmp_sum > target:
                    right -= 1
                else:
                    ans = target
                    break
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

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
