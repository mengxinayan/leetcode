class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def backtracking(cost: int, begin: int):
            if (abs(cost - target) < abs(self.ans - target)) or ((abs(cost - target) == abs(self.ans - target)) and (cost < self.ans)):
                self.ans = cost
            if (cost > target) or (begin == len(toppingCosts)):
                return
            backtracking(cost + 0 * toppingCosts[begin], begin+1)
            backtracking(cost + 1 * toppingCosts[begin], begin+1)
            backtracking(cost + 2 * toppingCosts[begin], begin+1)
        
        self.ans = float('inf')
        for cost in baseCosts:
            backtracking(cost, 0)
        return self.ans

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
