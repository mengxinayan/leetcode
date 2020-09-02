class Solution:
    def longestWord(self, words: List[str]) -> str:

        def check_valid(string: str, words_set: set) -> bool:
            res = True
            for i in range(1, len(words)):
                if string[:i] not in words_set:
                    res = False
                    break
            return res
        
        # 因为 Python 中的排序是稳定的，所以先按照字典序排序
        # Because sorting in Python is stable. So first lexicographically sort
        words.sort()
        words.sort(key=len, reverse=True)
        words_set = set(words)
        res = ''
        for i in range(len(words)):
            if check_valid(words[i], words_set) == True:
                res = words[i]
                break
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
