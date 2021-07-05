# Solution 1: sorted string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = []
        for string in strs:
            strs_sorted.append(''.join(sorted(string)))
        string_dict = {}
        for i in range(len(strs)):
            if strs_sorted[i] not in string_dict:
                string_dict[strs_sorted[i]] = [strs[i]]
            else:
                string_dict[strs_sorted[i]].append(strs[i])
        ans = []
        for value in string_dict.values():
            ans.append(value)
        return ans


# Solution 2: count number

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def count_str(string: str) -> tuple:
            ans = [0 for i in range(26)]
            for ch in string:
                ans[ord(ch) - ord('a')] += 1
            return tuple(ans)
        
        count_str_dict = {}
        for string in strs:
            tmp_tuple = count_str(string)
            if tmp_tuple not in count_str_dict:
                count_str_dict[tmp_tuple] = [string]
            else:
                count_str_dict[tmp_tuple].append(string)
        ans = []
        for value in count_str_dict.values():
            ans.append(value)
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
