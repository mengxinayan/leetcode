class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        self.str_times_dict = {}

        def process_str(string: str) -> None:
            times_str = string.split()
            times = times_str[0]
            words = times_str[1].split('.')
            for i in range(len(words)-1-1, -1, -1):
                words[i] += '.' + words[i+1]
            for word in words:
                if word not in self.str_times_dict:
                    self.str_times_dict[word] = int(times)
                else:
                    self.str_times_dict[word] += int(times)
        
        for string in cpdomains:
            process_str(string)
        ans = []
        for key, value in self.str_times_dict.items():
            ans.append(str(value) + ' ' + key)
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
