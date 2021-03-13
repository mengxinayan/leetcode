class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k < 0:
            pass
        else:
            num_times = {}
            for i in range(len(nums)):
                if nums[i] not in num_times:
                    num_times[nums[i]] = 1
                else:
                    if num_times[nums[i]] == 1:
                        num_times[nums[i]] += 1
                    else:
                        pass
            keys = set(nums)
            if k == 0:
                for key in keys:
                    if num_times[key] > 1:
                        ans += 1
            else:
                for key in keys:
                    del num_times[key]
                    if key + k in num_times:
                        ans += 1
                    if key - k in num_times:
                        ans += 1
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
