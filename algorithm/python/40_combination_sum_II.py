class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(tmp_sum: int, tmp_combination: List[int], begin: int):
            if tmp_sum == target:
                ans.append(tmp_combination[:])
            elif tmp_sum > target:
                pass
            else:
                for i in range(begin, len(candidates)):
                    # Remove duplicate solutions
                    if (i > begin) and (candidates[i] == candidates[i-1]):
                        continue
                    if tmp_sum + candidates[i] > target:
                        pass
                    else:
                        tmp_combination.append(candidates[i])
                        tmp_sum += candidates[i]
                        backtracking(tmp_sum, tmp_combination, i+1)
                        tmp_sum -= candidates[i]
                        tmp_combination.pop()

        candidates.sort()
        candidates_set = set(candidates)
        ans = []
        backtracking(0, [], 0)
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
