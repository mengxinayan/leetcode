class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def list_to_dict(nums: List[int]) -> dict:
            ans = {}
            for i in range(len(nums)):
                if nums[i] not in ans:
                    ans[nums[i]] = 1
                else:
                    ans[nums[i]] += 1
            return ans
        
        def cal_intersection(num_dict: dict, nums: List[int]) -> List[int]:
            ans = []
            for i in range(len(nums)):
                if nums[i] in num_dict:
                    ans.append(nums[i])
                    if num_dict[nums[i]] == 1:
                        del num_dict[nums[i]]
                    else:
                        num_dict[nums[i]] -= 1
            return ans

        if (len(nums1) == 0) or (len(nums2) == 0):
            return []
        if len(nums1) <= len(nums2):
            return cal_intersection(list_to_dict(nums2), nums1)
        else:
            return cal_intersection(list_to_dict(nums1), nums2)

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
