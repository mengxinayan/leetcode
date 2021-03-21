class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def number_of_soldiers(arr: List[int]) -> int:
            ans = 0
            for num in arr:
                if num == 1:
                    ans += 1
                else:
                    break
            return ans
        
        row_soldiers = []
        i = 0
        for arr in mat:
            row_soldiers.append([i, number_of_soldiers(arr)])
            i += 1
        row_soldiers.sort(key=lambda x : x[1])
        ans = []
        for i in range(k):
            ans.append(row_soldiers[i][0])
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
