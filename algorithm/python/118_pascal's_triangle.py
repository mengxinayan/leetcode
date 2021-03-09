class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def cal_next(nums: List[int]) -> List[int]:
            ans = [0 for i in range( len(nums)+1 )]
            ans[0] = 1
            ans[-1] = 1
            for i in range(1, len(nums)):
                ans[i] = nums[i] + nums[i-1]
            return ans

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ans = [[1], [1,1]]
            for i in range(numRows-2):
                tmp = cal_next(ans[-1])
                ans.append(tmp)
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
