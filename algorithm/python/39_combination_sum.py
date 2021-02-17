class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtracking(tmp_sum: int, tmp_combination: List[int], begin: int):
            if tmp_sum == target:
                res.append(tmp_combination[:])
            elif tmp_sum > target:
                pass
            else:
                for i in range(begin, len(candidates)):
                    if tmp_sum + candidates[i] > target:
                        pass
                    else:
                        tmp_combination.append(candidates[i])
                        tmp_sum += candidates[i]
                        backtracking(tmp_sum, tmp_combination, i)
                        tmp_sum -= candidates[i]
                        tmp_combination.pop()

        candidates_set = set(candidates)
        res = []
        backtracking(0, [], 0)
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
