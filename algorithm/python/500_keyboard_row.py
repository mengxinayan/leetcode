class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        def is_in_one_row(word: str) -> bool:
            if len(word) == 0:
                return True
            res = False
            if word[0] in set1:
                for i in range(1, len(word)):
                    if word[i] not in set1:
                        break
                else:
                    res = True
            elif word[0] in set2:
                for i in range(1, len(word)):
                    if word[i] not in set2:
                        break
                else:
                    res = True
            elif word[0] in set3:
                for i in range(1, len(word)):
                    if word[i] not in set3:
                        break
                else:
                    res = True
            else:
                pass
            return res

        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        res = []
        for i in range(len(words)):
            if is_in_one_row(words[i]) == True:
                res.append(words[i])
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
