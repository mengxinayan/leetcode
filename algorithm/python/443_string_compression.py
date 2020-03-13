class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        tmp = ''
        count = 0
        i = 0
        while i != len(chars):
            if tmp != chars[i]:
                if count >= 10:
                    chars.pop(i-1)
                    while count != 0:
                        chars.insert(i-1, str(count % 10))
                        count = count // 10
                tmp = chars[i]
                i += 1
                count = 1
            else:
                if count == 1:
                    count += 1
                    chars[i] = str(count)
                    i += 1
                else:
                    count += 1
                    chars[i-1] = str(count)
                    chars.pop(i)
        if count >= 10:
            chars.pop(i-1)
            while count != 0:
                chars.insert(i-1, str(count % 10))
                count = count // 10
        return len(chars)

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
