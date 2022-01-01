# Solution 1

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            else:
                ans += len(word)
        return ans


# Solution 2

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        def str_to_list(string: str) -> dict:
            ans = {}
            for ch in string:
                if ch not in ans:
                    ans[ch] = 1
                else:
                    ans[ch] += 1
            return ans
        
        def is_good(word: str, chars_dict: dict) -> bool:
            str_dict = str_to_list(word)
            ans = False
            for ch in str_dict.keys():
                if (ch in chars_dict) and (chars_dict[ch] >= str_dict[ch]):
                    pass
                else:
                    break
            else:
                ans = True
            return ans

        ans = 0
        chars_dict = str_to_list(chars)
        for word in words:
            if is_good(word, chars_dict) == True:
                ans += len(word) 
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
