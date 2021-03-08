class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(tmp: List[int], begin: int):
            if len(tmp) == len(nums):
                ans.append(tmp[:])
            else:
                for i in range(len(nums)):
                    if visited[i] == True:
                        pass
                    if (i > 0) and (nums[i] == nums[i-1]) and (visited[i-1] == False):
                        continue
                    if visited[i] == False:
                        tmp.append(nums[i])
                        visited[i] = True
                        begin += 1
                        backtracking(tmp, begin)
                        tmp.pop()
                        visited[i] = False
                        begin -= 1

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            nums.sort()
            visited = [False for i in range(len(nums))]
            ans = []
            backtracking([], 0)
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
