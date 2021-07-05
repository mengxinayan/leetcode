# Solution 1: Generate

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_ch_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], \
                    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], \
                    '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for ch in digits:
            ans = [pre + curr for pre in ans for curr in num_ch_dict[ch]]
        return ans


# Solution 2: Backtracing

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def backtracking(tmp: str, index: int):
            if index == len(digits):
                ans.append(tmp)
            else:
                for ch in num_ch_dict[digits[index]]:
                    tmp += ch
                    backtracking(tmp, index+1)
                    tmp = tmp[:len(tmp)-1]

        num_ch_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], \
                    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], \
                    '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = []
        backtracking('', 0)
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
