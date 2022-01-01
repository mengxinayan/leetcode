class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # len(nums1) < len(set2)
        def cal(nums1: List[int], set2: set) -> List[int]:
            ans = []
            for i in range(len(nums1)):
                if nums1[i] in set2:
                    ans.append(nums1[i])
            return ans
        
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) <= len(set2):
            return cal(list(set1), set2)
        else:
            return cal(list(set2), set1)

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2022  mengxinayan

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
