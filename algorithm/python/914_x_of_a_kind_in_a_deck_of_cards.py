class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        '''
        NOTE: Allow two sets of cards to have the same number.
        For example: deck = [1,1,1,1,2,2], Possible partition [1,1],[1,1],[2,2]
        
        允许有两组卡牌，他们的数字是相同的。
        比如：deck = [1,1,1,1,2,2], 分组情况 [1,1],[1,1],[2,2]
        '''
        
        def cal_gcd(num1: int, num2: int) -> int:
            tmp = 0
            while num2 != 0:
                tmp = num1 % num2
                num1 = num2
                num2 = tmp
            return num1

        num_times = {}
        for num in deck:
            if num in num_times:
                num_times[num] += 1
            else:
                num_times[num] = 1
        times = list(num_times.values())
        if len(times) == 1:
            if times[0] >= 2:
                return True
            else:
                return False
        else:
            arr_gcd = cal_gcd(times[0], times[1])
            for i in range(2, len(times)):
                arr_gcd = cal_gcd(arr_gcd, times[i])
            if arr_gcd >= 2:
                return True
            else:
                return False

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
