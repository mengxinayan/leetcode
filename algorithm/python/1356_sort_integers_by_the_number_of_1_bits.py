class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def num_of_1(num: int) -> int:
            ans = 0
            while num != 0:
                if num % 2 == 1:
                    ans += 1
                num //= 2
            return ans
        
        arr_bits = []
        for num in arr:
            arr_bits.append([num, num_of_1(num)])
        arr_bits.sort(key = lambda x: (x[1], x[0]))
        ans = []
        for i in range(len(arr_bits)):
            ans.append(arr_bits[i][0])
        return ans

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
