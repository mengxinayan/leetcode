# Solution 1: Brute force solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def find_next_greater(pos: int) -> int:
            index = -1
            for i in range(len(nums2)):
                if nums2[i] == nums1[pos]:
                    index = i
            if index == -1:
                return -1
            ans = 0
            for i in range(index+1, len(nums2)):
                if nums2[i] > nums1[pos]:
                    ans = nums2[i]
                    break
            else:
                ans = -1
            return ans

        ans = []
        for i in range(len(nums1)):
            ans.append(find_next_greater(i))
        return ans


# Solution 2: Using stack

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_next_greater_num = {}
        for i in range(0, len(nums2)):
            while (len(stack) != 0) and (nums2[i] > stack[-1]):
                num_next_greater_num[stack[-1]] = nums2[i]
                stack.pop()
            if (len(stack) == 0) or (nums2[i] <= stack[-1]):
                stack.append(nums2[i])
        ans = []
        for i in range(0, len(nums1)):
            if nums1[i] in num_next_greater_num:
                ans.append(num_next_greater_num[nums1[i]])
            else:
                ans.append(-1)
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
