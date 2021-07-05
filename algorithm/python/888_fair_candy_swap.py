class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        def cal_exchange_size(arr1: List[int], arr2: List[int]) -> List[int]:
            # Assume that sum(arr1)>= sum(arr2) holds in this function
            # 假设该函数中 sum(arr1)>= sum(arr2) 成立
            diff = sum(arr1) - sum(arr2)
            arr2_set = set(arr2)
            ans = []
            for size in arr1:
                if (size - diff//2) in arr2_set:
                    ans = [size, size - diff//2]
                    break
            return ans
        
        ans = []
        if sum(A) >= sum(B):
            ans = cal_exchange_size(A, B)
        else:
            ans = cal_exchange_size(B, A)
            ans.reverse()
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
