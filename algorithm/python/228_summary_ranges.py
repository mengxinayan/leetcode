class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            ans = []
            start = pre = nums[0]
            for i in range(1, len(nums)):
                curr = nums[i]
                if curr == pre + 1:
                    pre = curr
                else:
                    if start == pre:
                        ans.append(str(start))
                    else:
                        ans.append(str(start)+'->'+str(pre))
                    start = pre = curr
            if start == pre:
                ans.append(str(start))
            else:
                ans.append(str(start)+'->'+str(pre))
            return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

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
