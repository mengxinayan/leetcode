class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_times = {}
        for num in arr1:
            if num not in num_times:
                num_times[num] = 1
            else:
                num_times[num] += 1
        ans = []
        for num in arr2:
            times = num_times[num]
            for i in range(times):
                ans.append(num)
            del num_times[num]
        others = list(num_times.keys())
        if len(others) == 0:
            return ans
        others.sort()
        for num in others:
            times = num_times[num]
            for i in range(times):
                ans.append(num)
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
