class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        ans = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i+1 < len(nums)-1 and i-1 >= 0:
                    if (nums[i] > nums[i+2]) and (nums[i-1] > nums[i+1]):
                        ans = False
                        break
        if count > 1:
            ans = False
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
