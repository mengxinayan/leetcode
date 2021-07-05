class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        def cal_license_letters(licensePlate: str) -> List[str]:
            ans = []
            for ch in licensePlate.lower():
                if ch.isalpha() == True:
                    ans.append(ch)
            return ans
        
        def check_word_valid(license_letters: List[str], word: str) -> bool:
            word_letter_dict = {}
            for ch in word:
                if ch not in word_letter_dict:
                    word_letter_dict[ch] = 1
                else:
                    word_letter_dict[ch] += 1
            ans = True
            for i in range(len(license_letters)):
                if license_letters[i] in word_letter_dict:
                    if word_letter_dict[license_letters[i]] == 1:
                        word_letter_dict.pop(license_letters[i])
                    else:
                        word_letter_dict[license_letters[i]] -= 1
                else:
                    ans = False
                    break
            return ans
        
        license_letters = cal_license_letters(licensePlate)
        ans = ''
        ans_len = 16
        for i in range(len(words)):
            if (check_word_valid(license_letters, words[i]) == True) and (len(words[i]) < ans_len):
                ans = words[i]
                ans_len = len(words[i])
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
