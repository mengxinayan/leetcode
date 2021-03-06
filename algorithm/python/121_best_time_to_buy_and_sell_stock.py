class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: # Don't Forget this case!
            return 0
        res = curr = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if (start <= prices[i]) :
                curr = max(curr, prices[i]-start)
            else:
                start = prices[i]
                res = max(res, curr)
                curr = 0
        res = max(res, curr)
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
