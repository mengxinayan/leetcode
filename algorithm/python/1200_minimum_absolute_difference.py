class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr_set = set(arr)
        sorted_arr = sorted(arr)
        min_diff = float('inf')
        for i in range(len(arr)-1):
            min_diff = min(min_diff, sorted_arr[i+1]-sorted_arr[i])
        ans = []
        for key in sorted_arr:
            if (key - min_diff) in arr_set:
                ans.append([key, key-min_diff])
            if (key + min_diff) in arr_set:
                ans.append([key, key+min_diff])
            arr_set.remove(key)
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
