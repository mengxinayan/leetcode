class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lower_paragraph = paragraph.lower()
        lower_paragraph = lower_paragraph.replace('!', ' ')
        lower_paragraph = lower_paragraph.replace('?', ' ')
        lower_paragraph = lower_paragraph.replace("'", ' ')
        lower_paragraph = lower_paragraph.replace(',', ' ')
        lower_paragraph = lower_paragraph.replace(';', ' ')
        lower_paragraph = lower_paragraph.replace('.', ' ')
        words = lower_paragraph.split()
        word_times = {}
        for word in words:
            if word not in word_times:
                word_times[word] = 1
            else:
                word_times[word] += 1
        banned_set = set(banned)
        for banned_word in banned_set:
            if banned_word in word_times:
                word_times.pop(banned_word)
        max_times = 0
        res = []
        for key, value in word_times.items():
            if value > max_times:
                res = key
                max_times = value
            else:
                pass
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
