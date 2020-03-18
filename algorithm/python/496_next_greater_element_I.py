class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def find_next_greater(pos: int) -> int:
            index = -1
            for i in range(len(nums2)):
                if nums2[i] == nums1[pos]:
                    index = i
            if index == -1:
                return -1
            res = 0
            for i in range(index+1, len(nums2)):
                if nums2[i] > nums1[pos]:
                    res = nums2[i]
                    break
            else:
                res = -1
            return res

        res = []
        for i in range(len(nums1)):
            res.append(find_next_greater(i))
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
