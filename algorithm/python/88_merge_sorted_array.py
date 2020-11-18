# Solution 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            # Remove extra zeros at the end
            # 去除末尾多余的0
            for tmp in range(n):
                nums1.pop()
            for i in range(n):
                nums1.append(nums2[i])
        else:
            for tmp in range(n):
                nums1.pop()
            i = j = 0
            while i != m and j != n:
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    i += 1
                    j += 1
                    # a new element is inserted, the length of nums1 is increased by one, that is, m = m + 1
                    # 因为插入了新元素，nums1长度要增加一，即m=m+1
                    m += 1 
                else:
                    i += 1
            if i == m:
                for k in range(j, n):
                    nums1.append(nums2[k])


# Solution 2, easy to understand, but poor efficiency

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        else:
            # Remove extra zeros at the end
            # 去除末尾多余的0
            for tmp in range(n):
                nums1.pop()
            for i in range(n):
                nums1.append(nums2[i])
            nums1.sort()

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
