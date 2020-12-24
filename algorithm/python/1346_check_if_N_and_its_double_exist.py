class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Because i != j, so the array has at least two 0s to meet the requirements
        if arr.count(0) >= 2:
            return True
        arr_set = set(arr)
        res = True
        for num in arr:
            if (num != 0) and ((num/2 in arr_set) or (num*2 in arr_set)):
                break
        else:
            res = False
        return res

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
