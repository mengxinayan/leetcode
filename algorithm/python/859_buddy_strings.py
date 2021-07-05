class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        diff_chs = []
        if A == B:
            ch_set = set()
            for ch in A:
                if ch in ch_set:
                    return True
                else:
                    ch_set.add(ch)

        for i in range(len(A)):
            if A[i] != B[i]:
                diff_chs.append([A[i], B[i]])
        if (len(diff_chs) == 2) and (diff_chs[0][0] == diff_chs[1][1]) and (diff_chs[1][0] == diff_chs[0][1]):
            return True
        else:
            return False

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
