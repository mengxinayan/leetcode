class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int start = 0;
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (map.containsKey(ch) == true) {
                maxLength = (map.size() > maxLength) ? map.size() : maxLength;
                i = map.get(ch) + 1;
                map.clear();
            } else {
                map.put(ch, i);
                i++;
            }
        }
        // Determine there is no repeating characters
        maxLength = (map.size() > maxLength) ? map.size() : maxLength;
        return maxLength;
    }
}

/**
 * This is my personal record of solving Leetcode Problems. 
 * If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
 * Copyright (C) 2020-2021  mengxinayan
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */