class Solution:
    def toGoatLatin(self, S: str) -> str:
        self.vowel_letter = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        def process_word(word: str, index: str) -> str:
            if word[0] in self.vowel_letter:
                word += 'ma'
            else:
                first_letter = word[0]
                word = word[1:] + first_letter + 'ma'
            word += 'a' * (index + 1)
            return word
        
        words = S.split()
        ans = ''
        for i in range(len(words)):
            if i != len(words) - 1:
                ans = ans + process_word(words[i], i) + ' '
            else:
                ans += process_word(words[i], i)
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
